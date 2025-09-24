// static/diary/js/page-fade.js
console.log("page-fade loaded");

document.addEventListener("DOMContentLoaded", () => {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity .35s ease";
    requestAnimationFrame(() => { document.body.style.opacity = "1"; });
});
