document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');

    if (!chatBox || !chatInput || !chatSend) return;

    function addMessage(message, sender) {
        const div = document.createElement('div');
        div.classList.add('chat-message', sender);
        
        // Handle basic markdown bold and newlines
        let formattedMessage = message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        div.innerHTML = formattedMessage;
        div.style.whiteSpace = 'pre-wrap'; // Ensure line breaks exist
        
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const text = chatInput.value.trim();
        if (!text) return;

        addMessage(text, 'user');
        chatInput.value = '';

        const apiKey = localStorage.getItem('gemini_api_key');
        if(!apiKey) {
            addMessage("⚠️ Please enter and save your Gemini API Key in the Configuration box above before chatting.", 'bot');
            return;
        }

        const promptText = `You are an elite Computer Science Interview Prep AI. The user is asking a technical or HR question. 
You MUST provide a detailed, pointwise solution. Break your answer down logically. Focus on high technical depth and formatting.
User Question: ${text}`;

        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('chat-message', 'bot');
        loadingDiv.textContent = "Analyzing...";
        chatBox.appendChild(loadingDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

        async function fetchGemini(modelPath) {
            const res = await fetch(`https://generativelanguage.googleapis.com/${modelPath}?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ contents: [{ parts: [{ text: promptText }] }] })
            });
            return await res.json();
        }

        try {
            let data = await fetchGemini('v1/models/gemini-2.5-flash:generateContent');
            
            // Auto-Fallback Logic to bypass Google's free-tier throttling
            if(data.error && (data.error.code === 503 || data.error.message.toLowerCase().includes('demand'))) {
                loadingDiv.textContent = "Server busy. Rerouting to backup AI cluster...";
                data = await fetchGemini('v1beta/models/gemini-1.5-flash:generateContent');
            }

            chatBox.removeChild(loadingDiv);
            
            if(data.error) {
                addMessage(`API Error: ${data.error.message}`, 'bot');
                return;
            }
            
            let botReply = data.candidates[0].content.parts[0].text;
            addMessage(botReply, 'bot');
        } catch (err) {
            if(chatBox.contains(loadingDiv)) chatBox.removeChild(loadingDiv);
            addMessage("Failed to connect to Gemini API. Please check your internet connection or API Key.", 'bot');
            console.error(err);
        }
    }

    chatSend.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    const exportBtn = document.getElementById('export-chat-btn');
    const exportForm = document.getElementById('export-chat-form');
    const chatDataInput = document.getElementById('chat_data_input');

    if (exportBtn) {
        exportBtn.addEventListener('click', () => {
            const messages = [];
            const messageNodes = chatBox.querySelectorAll('.chat-message');
            messageNodes.forEach(node => {
                const isUser = node.classList.contains('user');
                messages.push({
                    sender: isUser ? 'You' : 'AI Assistant',
                    text: node.textContent.trim()
                });
            });
            chatDataInput.value = JSON.stringify(messages);
            exportForm.submit();
        });
    }
});
