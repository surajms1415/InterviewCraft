document.addEventListener('DOMContentLoaded', () => {
    // Theme toggle
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        // Check local storage
        const currentTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);
        themeToggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';

        themeToggle.addEventListener('click', () => {
            const theme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
        });
    }
});
