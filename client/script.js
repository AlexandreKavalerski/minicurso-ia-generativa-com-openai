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

  translateButton.addEventListener("click", function () {
    traduzirCodigo();
  });

  const createButton = document.getElementById("create-button");
  const creationResult = document.getElementById("result-placeholder");

  createButton.addEventListener("click", function () {
    // Aqui você pode adicionar a lógica de criação do programa usando APIs ou JavaScript
    creationResult.textContent = "Programa criado com sucesso!";
  });
});

function get_linguagem_origem() {
  return document.querySelector("#linguagem-origem").value;
}

function get_linguagem_alvo() {
  return document.querySelector("#linguagem-alvo").value;
}

function get_codigo() {
  return document.querySelector("#input-codigo").value;
}

async function traduzirCodigo() {
  // Replace these functions with your actual data retrieval logic
  const linguagemOrigem = get_linguagem_origem();
  const linguagemAlvo = get_linguagem_alvo();
  const codigo = get_codigo();

  // Create the request body as a JavaScript object
  const data = {
    linguagem_origem: linguagemOrigem,
    linguagem_destino: linguagemAlvo,
    trecho_de_codigo: codigo,
  };

  // Convert the data object to a JSON string
  const jsonBody = JSON.stringify(data);

  try {
    const headers = {
      Accept: "application/json",
      "Content-Type": "application/json",
    };
    const url = "http://localhost:8000/traducao";

    const response = await fetch(url, {
      method: "POST",
      headers: headers,
      body: jsonBody,
    });

    if (response.ok) {
      const resultado = await response.json();
      console.log("Success:", resultado);

      const translationResult = document.getElementById("result-placeholder");
      translationResult.textContent = resultado;
    } else {
      console.error("Error:", response.statusText);
    }
  } catch (error) {
    console.error("An error occurred:", error);
  }
}
