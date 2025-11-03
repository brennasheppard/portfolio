const toggle = document.getElementById('dark-toggle');
toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    toggle.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
        e.preventDefault();
        document.querySelector(anchor.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
});

async function loadProjects() {
    const response = await fetch('https://api.github.com/users/brennasheppard/repos?sort=updated&per_page=6');
    const repos = await response.json();
    const list = document.getElementById('project-list');
    list.innerHTML = repos.map(repo => `
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow">
            <h3 class="text-xl font-bold">${repo.name}</h3>
            <p>${repo.description || 'Documentation or implementation project'}</p>
            <a href="${repo.html_url}" class="text-blue-500 hover:underline" target="_blank">View on GitHub</a>
        </div>
    `).join('');
}
loadProjects();
