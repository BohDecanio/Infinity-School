document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".navigate-button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            window.location.href = "https://infinityschool.com.br/";
        });
    });
});
