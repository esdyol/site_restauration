
  function showSignup(event) {
    event.preventDefault();
    document.getElementById("login-box").classList.remove("active");
    document.getElementById("signup-box").classList.add("active");
  }

  function showLogin(event) {
    event.preventDefault();
    document.getElementById("signup-box").classList.remove("active");
    document.getElementById("login-box").classList.add("active");
  }

  // Active par défaut le formulaire Connexion
  window.addEventListener("DOMContentLoaded", () => {
    document.getElementById("login-box").classList.add("active");
  });


  let count = 0;

  function ajouterAuPanier(nomPlat) {
    count++;
    document.getElementById('panier-count').textContent = count;
    console.log(nomPlat + " ajouté au panier.");
    // Tu peux stocker les plats ici si besoin :
    // panier.push(nomPlat);
  }

  function afficherPanier() {
    alert("Vous avez " + count + " article(s) dans votre panier.");
  }
