const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
document.addEventListener("DOMContentLoaded", function () {
  var signUpBtn = document.querySelector("#sign-up-btn");
  if (signUpBtn) {
    signUpBtn.addEventListener("click", function () {
      window.location.href = signUpBtn.getAttribute("data-url");
    });
  }
});
