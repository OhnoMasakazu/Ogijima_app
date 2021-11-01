document.addEventListener("DOMContentLoaded", () => {
    const today = new Date();
    const today_year = today.getFullYear();
    document.getElementById('copyright_year').innerText = today_year;

});