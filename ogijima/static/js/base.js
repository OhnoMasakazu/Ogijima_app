document.addEventListener("DOMContentLoaded", () => {
    const today = new Date();
    const today_year = today.getFullYear();
    document.getElementById('copyright_year').innerText = today_year;
});

//navメニュー表示切替
document.getElementById('nav_btn').onclick = function() {
    document.getElementById('header_menu_tags').classList.add('show_nav');
};

document.getElementById('close_btn').onclick = function() {
    document.getElementById('header_menu_tags').classList.remove('show_nav');
};