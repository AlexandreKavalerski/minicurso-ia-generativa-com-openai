document.addEventListener("DOMContentLoaded", function () {
  const translateTab = document.getElementById("translate-tab");
  const createTab = document.getElementById("create-tab");
  const translateContainer = document.getElementById("translate-container");
  const createContainer = document.getElementById("create-container");

  translateTab.addEventListener("click", function () {
    translateContainer.style.display = "block";
    createContainer.style.display = "none";
  });

  createTab.addEventListener("click", function () {
    translateContainer.style.display = "none";
    createContainer.style.display = "block";
  });

  const translateButton = document.getElementById("translate-button");
  const translationResult = document.getElementById("result-placeholder");

  translateButton.addEventListener("click", function () {
    // Aqui você pode adicionar a lógica de tradução usando APIs ou JavaScript
    translationResult.textContent = "Tradução de exemplo aqui.";
  });

  const createButton = document.getElementById("create-button");
  const creationResult = document.getElementById("result-placeholder");

  createButton.addEventListener("click", function () {
    // Aqui você pode adicionar a lógica de criação do programa usando APIs ou JavaScript
    creationResult.textContent = "Programa criado com sucesso!";
  });
});
