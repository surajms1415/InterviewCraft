import json
import os

data = [
    {
        "id": "ai-jobs",
        "topic": "1. Artificial Intelligence vs Human Jobs",
        "perspective": "To stand out in a Group Discussion (GD), you need to move beyond the obvious arguments. You need to provide structural insights that look at social psychology, economic impact, and long-term sustainability.",
        "pitches": [
            {
                "title": "The Transition from 'Task-Based' to 'Value-Based' Labor",
                "content": "\"We must realize that AI doesn't replace 'jobs'; it replaces 'tasks.' Most modern jobs are a collection of routine data processing and high-level decision-making. AI is currently absorbing the routine—the data entry, the basic coding, and the initial research. This forces the human worker to move up the value chain. For example, a lawyer no longer spends 40 hours reviewing documents (AI does that); they now spend those 40 hours on high-level litigation strategy. The 'Human Job' of the future is about being an AI Orchestrator—someone who knows how to leverage these tools to produce a 10x output.\""
            },
            {
                "title": "The Preservation of the 'Empathy Economy'",
                "content": "\"There is a massive sector of our economy that relies on Tacit Knowledge and Emotional Intelligence (EQ)—things that cannot be reduced to an algorithm. In healthcare, education, and high-stakes negotiations, the 'human touch' is the primary product. A machine can diagnose a disease with 99% accuracy, but it cannot deliver that news with the empathy required to guide a patient through recovery. As AI commoditizes logic, the market value of 'Human Empathy' and 'Ethical Judgment' will skyrocket. We aren't entering a jobless future; we are entering an Empathy Economy.\""
            },
            {
                "title": "Historical Precedence: The 'Luddite Fallacy'",
                "content": "\"Economists call the fear of total job loss the 'Luddite Fallacy.' When the ATM was introduced, people predicted the end of bank tellers. Instead, the cost of opening bank branches dropped, leading to more branches and more tellers, who shifted from counting cash to selling financial products. AI lowers the barrier to entry for complex fields. Today, someone without a CS degree can build an app using AI. This 'democratization of skill' creates a massive influx of new entrepreneurs and micro-businesses, which in turn creates a net positive gain in the global job market.\""
            },
            {
                "title": "The 'Accountability Gap' in Critical Systems",
                "content": "\"A major barrier to AI replacing humans is the Accountability Gap. In critical infrastructure—like power grids, autonomous weapon systems, or corporate auditing—society requires a 'Moral Agent' to be responsible. You cannot take an algorithm to court. For any high-stakes operation, there must be a 'Human-in-the-Loop' to sign off on decisions. AI will act as a co-pilot, but the 'Pilot's License' will always remain with a human. Therefore, AI is not a threat to the professional class; it is a sophisticated tool that necessitates a more responsible and highly skilled human supervisor.\""
            }
        ]
    },
    {
        "id": "online-education",
        "topic": "2. Online vs. Offline Education",
        "perspective": "Education is a dual process of 'Content Acquisition' and 'Character Socialization.'",
        "pitches": [
            {
                "title": "The 'Democratization' vs. 'Digital Divide' Argument",
                "content": "\"We must view online education not just as a convenience, but as the greatest leveler of the playing field in human history. It has decoupled 'Quality Education' from 'Elite Geography.' However, we cannot ignore the Digital Divide. While online platforms offer a boon to the urban elite, they risk further marginalizing those without high-speed infrastructure. Therefore, the goal isn't to replace offline schools, but to use online tools to 'bridge the gap' between the world's best content and the world's most remote student.\""
            },
            {
                "title": "Cognitive Discipline vs. Social Intelligence",
                "content": "\"Online education is excellent for Information Transfer, but it often fails at Holistic Socialization. Schools and colleges are 'micro-societies' where students learn negotiation, conflict resolution, and leadership—skills that cannot be mastered through a screen. While a student can learn 'Coding' perfectly online, they learn 'Collaborative Engineering' in an offline lab. We must transition to a Hybrid/Blended Model where we use the efficiency of online for theory and the empathy of offline for interpersonal growth.\""
            },
            {
                "title": "The Shift from 'Passive Learning' to 'Active Exploration'",
                "content": "\"Online education is forcing a shift from a 'Teacher-Centric' to a 'Learner-Centric' model. In a traditional classroom, the pace is set by the average student, which often bores the gifted and leaves behind the slow. Online platforms allow for Hyper-Personalization via AI-driven adaptive learning paths. This moves the teacher's role from being a 'Sage on the Stage' to a 'Guide on the Side,' making the student the primary driver of their own intellectual curiosity.\""
            }
        ]
    },
    {
        "id": "social-media",
        "topic": "3. Social Media – Boon or Bane?",
        "perspective": "It is a 'Cognitive Mirror'—it reflects and amplifies the user's intent.",
        "pitches": [
            {
                "title": "The Democratization of 'The Voice' (Boon)",
                "content": "\"Social media has dismantled the Gatekeepers of Information. Historically, only big media houses decided what was news. Today, a common citizen with a smartphone is a global reporter. This has led to unprecedented accountability and social activism (like disaster relief coordination or consumer rights). It is a boon because it has turned the 'Passive Consumer' of information into an 'Active Participant' in the global narrative, giving a voice to those who were historically silenced.\""
            },
            {
                "title": "The Algorithmic 'Echo Chamber' (Bane)",
                "content": "\"The primary 'bane' isn't the content, but the Algorithmic Design. Platforms are optimized for 'Engagement,' which biologically favors outrage and polarization over nuance. This creates Echo Chambers where users are only exposed to information that validates their existing biases. We are losing the 'Middle Ground' of public discourse. This 'fragmentation of truth' is a systemic risk to the fabric of a healthy democracy, as we no longer share a common set of facts.\""
            },
            {
                "title": "The 'Attention Economy' and Mental Capital (Bane)",
                "content": "\"We are currently living in an Attention Economy where our focus is the product being sold. The psychological cost is 'Cognitive Fragmentation.' The constant hit of dopamine from 'Likes' and 'Shares' creates a Validation Trap, especially among the youth, leading to a rise in anxiety and the 'Highlight Reel' effect—where we compare our daily struggles to everyone else's curated successes. The bane isn't social media itself, but our lack of 'Digital Hygiene' in a world designed to keep us addicted.\""
            },
            {
                "title": "The Rise of 'Social Commerce' and The Gig Economy (Boon)",
                "content": "\"From a purely economic standpoint, social media is a massive Job Engine. It has given birth to the 'Creator Economy' and 'Social Commerce,' allowing micro-entrepreneurs to sell products globally without a physical storefront. For a developing nation like India, this is a boon because it empowers the rural youth to monetize their talent—be it art, tutoring, or agriculture—directly to a global audience, bypassing expensive middlemen.\""
            }
        ]
    },
    {
        "id": "india-econ",
        "topic": "4. India's Economic Growth vs. Unemployment",
        "perspective": "We must transition from 'Jobless Growth' to 'Job-Led Growth' by bridging the skill-industry gap.",
        "pitches": [
            {
                "title": "The Skill-Degree Paradox",
                "content": "\"In any GD on unemployment, we must address the 'Paradox of the Unemployable Graduate.' India is degree-rich but skill-poor. Our economic growth is driven by the high-end service sector (IT, Fintech), but our education system produces generalists. To fix this, we need to shift from 'Degree-based hiring' to 'Skill-based hiring.' The solution isn't just creating any jobs, but creating Industry-Aligned roles through massive vocational integration.\""
            },
            {
                "title": "Missing the Manufacturing Bus",
                "content": "\"Historically, nations move from Agriculture to Manufacturing and then to Services. India skipped the middle step. While Services contribute 50%+ to our GDP, they absorb less than 30% of the workforce. We need to leverage the 'China Plus One' global strategy to become a manufacturing hub in semiconductors and textiles. Labor-intensive manufacturing is the only engine capable of absorbing the millions of rural youth entering the market annually.\""
            },
            {
                "title": "The MSME Multiplier Effect",
                "content": "\"While we often focus on Big Tech, the real backbone of employment is the MSME sector (Micro, Small, and Medium Enterprises). They contribute 30% to the GDP but are the largest employers after agriculture. Instead of everyone being a 'Job Seeker' at a MNC, policy-level support for MSMEs—like easier credit and reduced compliance—can turn millions of youth into 'Job Creators' in their own local communities.\""
            }
        ]
    },
    {
        "id": "youth-nation",
        "topic": "5. Role of Youth in Nation Building",
        "perspective": "Youth are not just the 'future' of the nation; they are the 'Active Drivers' of its digital and social infrastructure.",
        "pitches": [
            {
                "title": "Driving the Digital Democracy",
                "content": "\"India's youth are the primary architects of our Digital Public Infrastructure (DPI). From the adoption of UPI to the growth of E-commerce, the youth have moved India from a 'Cash-Heavy' to a 'Data-Rich' economy. By being early adopters and innovators, the youth are helping the government achieve transparency and financial inclusion, which is the bedrock of a developed nation.\""
            },
            {
                "title": "From Activism to Administration",
                "content": "\"Nation-building requires the youth to move beyond social media activism and into Civic Participation. We are seeing a trend where highly educated youth are entering the civil services, local governance, and policy think-tanks. This 'Professionalization of Politics' is vital because it brings a data-driven, modern approach to solving age-old problems like sanitation, urban planning, and public health.\""
            },
            {
                "title": "The Demographic Dividend as a Responsibility",
                "content": "\"India has the world's largest young population, but this 'Demographic Dividend' can become a 'Demographic Disaster' without a sense of Social Responsibility. Youth-led movements against social evils—like casteism, dowry, and environmental neglect—are redefining India's 'Soft Power.' Nation-building is not just about GDP; it's about the ethical and social fabric that the youth are currently re-weaving.\""
            }
        ]
    },
    {
        "id": "tech-society",
        "topic": "6. Impact of Technology on Society",
        "perspective": "Technology is a 'Force Multiplier' that enhances efficiency but challenges our biological and social limits.",
        "pitches": [
            {
                "title": "The Democratization of Access",
                "content": "\"The greatest impact of technology has been the Removal of the Middleman. Whether it's a farmer checking crop prices on an app or a student in a village learning via YouTube, technology has destroyed the 'Information Monarchy.' This democratization leads to a more equitable society where your success depends on your 'Intellectual Curiosity' rather than your 'Postal Code'.\""
            },
            {
                "title": "The Loneliness Epidemic and Cognitive Fragmentation",
                "content": "\"On the flip side, as we become more 'Connected' digitally, we are becoming more 'Isolated' socially. Technology has created a 'Loneliness Epidemic.' Moreover, the 'Infinite Scroll' and short-form content are causing 'Cognitive Fragmentation'—reducing our deep-work capacity and attention spans. We are trading 'Wisdom' for 'Information,' and this shift in how we process thought is a major systemic risk to society.\""
            },
            {
                "title": "The Surveillance State vs. Digital Liberty",
                "content": "\"Technology has given the state and corporations unprecedented power to monitor behavior. While this is a boon for national security and personalized services, it poses a threat to Individual Autonomy. Our data is our digital DNA, and the lack of digital literacy means society is being steered by algorithms rather than free will. The challenge of our generation is to ensure that technology remains a 'Servant' and doesn't become the 'Master' of our social choices.\""
            }
        ]
    },
    {
        "id": "mental-health",
        "topic": "7. Mental Health Awareness in Students/Workplace",
        "perspective": "We must move from 'Acknowledging the Problem' to 'Building Institutional Resilience.'",
        "pitches": [
            {
                "title": "The 'Hustle Culture' Trap",
                "content": "\"In a GD, we must address that modern productivity is often built on an unsustainable 'Hustle Culture.' In schools and workplaces, we celebrate the 'Burnout' as a badge of honor. This has led to a silent crisis of anxiety and depression. We need to pitch that Mental Health is a Productivity Tool, not a luxury. A mentally healthy workforce has lower turnover, higher creativity, and better long-term output. It's time to move from 'Crisis Management' to 'Preventive Care'—standardizing mental health days just as we do sick leaves.\""
            },
            {
                "title": "The Digital Mirror and Validation Trap",
                "content": "\"For students specifically, the impact of the 'Highlight Reel' effect on social media is devastating. They are constantly comparing their internal struggles with the curated, perfect lives of others. This creates a 'Perfectionism Gap' that leads to chronic stress. We need to integrate 'Digital Hygiene' and 'Emotional Literacy' into the academic curriculum. Awareness is the first step, but institutionalizing counseling services without the fear of social stigma is the second, more critical step.\""
            },
            {
                "title": "The Managerial/Parental Responsibility",
                "content": "\"The bottleneck for mental health awareness is often the leadership—be it parents or managers. There is a generational gap in how mental health is perceived. We need to pitch for 'Sensitivity Training' at the top. A student shouldn't fear their grades will be judged if they seek help, and an employee shouldn't fear their career growth will be stunted. We must build a 'Psychologically Safe' environment where vulnerability is seen as a step toward strength, not a sign of weakness.\""
            }
        ]
    },
    {
        "id": "superpower",
        "topic": "8. Is India Ready to Become a Global Superpower?",
        "perspective": "India has the 'Hard Power' and 'Soft Power,' but must fix its 'Internal Infrastructure' to sustain the status.",
        "pitches": [
            {
                "title": "The Demographic Dividend vs. Skill Gap",
                "content": "\"India's greatest strength is its median age of 28. We have the world's largest young workforce, which is a massive economic engine. However, being a 'Superpower' requires moving from a labor-supply nation to an Innovation-led nation. We are ready in terms of numbers, but we need to bridge the skill gap to ensure our youth are creators of technology, not just consumers of it. Our transition into a 5-trillion-dollar economy is the foundation of this readiness.\""
            },
            {
                "title": "Digital Public Infrastructure (DPI) as a Global Model",
                "content": "\"India is already a 'Digital Superpower.' Our India Stack (UPI, Aadhaar, ONDC) is being studied globally as a model for financial inclusion. We have leapfrogged traditional development cycles by using technology to provide services to the last mile. This 'Technological Diplomacy' gives India a unique seat at the global table, where we aren't just following Western standards but setting the standards for the Global South.\""
            },
            {
                "title": "Strategic Autonomy and Geopolitical Maturity",
                "content": "\"A superpower is defined by its ability to maintain its own interest without being a satellite of any other power. India's stance in recent global conflicts—balancing relationships with both the West and the East—demonstrates a 'Strategic Autonomy' that is a hallmark of a superpower. We are moving from being a 'Passive Spectator' to a 'Vocal Mediator' in global governance, as seen during our G20 presidency.\""
            },
            {
                "title": "The Internal Social Constraints",
                "content": "\"To conclude with a balanced view, a nation cannot be a 'Global Superpower' if it remains a 'Social Underachiever' in certain areas. We must resolve internal paradoxes—like high GDP growth alongside high malnutrition, or space exploration alongside judicial delays. True superpower status will be achieved when our Human Development Index (HDI) matches our GDP growth. We are ready on the external front; we now need a focused push on our internal social equity.\""
            }
        ]
    }
]

os.makedirs('frontend-app/src/data', exist_ok=True)
with open('frontend-app/src/data/gd_notes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print("Saved GD data")
