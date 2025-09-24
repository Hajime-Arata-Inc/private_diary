// static/diary/js/form-helpers.js
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    forms.forEach((form) => {
    form.addEventListener("submit", (e) => {
        const btn = form.querySelector("[type=submit]");
        if (!btn) return;
        if (btn.dataset.submitted === "true") {
        e.preventDefault(); // 二重送信防止
        return;
        }
        btn.dataset.submitted = "true";
        btn.disabled = true;
        const original = btn.innerHTML;
        btn.dataset.original = original;
        btn.innerHTML = "送信中...";
        });
    });
});
