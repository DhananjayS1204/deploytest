
document.getElementById('loginForm')?.addEventListener('submit', function (e) {
    e.preventDefault();
    window.location.href = '{% url "disease" %}';
});

function navigateTo(page) {
    window.location.href = page;
}
