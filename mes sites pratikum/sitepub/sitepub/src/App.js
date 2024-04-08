// App.js
import React, { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Annonces from "./components/Annonces";
import logo from "./logo.png";
import "./App.css";

function App() {
  // Exemple de données pour les annonces populaires et les catégories
  const [anciennesAnnonces, setAnciennesAnnonces] = useState([
    {
      id: 1,
      titre: "Annonce Ancienne 1",
      description: "Description de l'annonce ancienne 1",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 2,
      titre: "Annonce Ancienne 2",
      description: "Description de l'annonce ancienne 2",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 3,
      titre: "Annonce Ancienne 3",
      description: "Description de l'annonce ancienne 3",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 4,
      titre: "Annonce Ancienne 4",
      description: "Description de l'annonce ancienne 4",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 5,
      titre: "Annonce Ancienne 5",
      description: "Description de l'annonce ancienne 5",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 6,
      titre: "Annonce Ancienne 6",
      description: "Description de l'annonce ancienne 6",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 7,
      titre: "Annonce Ancienne 7",
      description: "Description de l'annonce ancienne 7",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 8,
      titre: "Annonce Ancienne 8",
      description: "Description de l'annonce ancienne 8",
      image: "https://via.placeholder.com/150",
    },
  ]);

  const annoncesPopulaires = [
    {
      id: 1,
      titre: "Annonce 1",
      description: "Description de l'annonce 1",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 2,
      titre: "Annonce 2",
      description: "Description de l'annonce 2",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 3,
      titre: "Annonce 3",
      description: "Description de l'annonce 3",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 4,
      titre: "Annonce 4",
      description: "Description de l'annonce 4",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 5,
      titre: "Annonce 5",
      description: "Description de l'annonce 5",
      image: "https://via.placeholder.com/150",
    },
  ];

  const categories = ["Voitures", "Immobilier", "Emploi", "Électronique"];

  const handleAfficherAnnonce = (id) => {
    // Logique pour afficher l'annonce avec l'ID donné
    console.log("Afficher l'annonce avec l'ID :", id);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Bienvenue chez MAN-PUB</p>
        <a
          className="App-link"
          href="#"
          target="_blank"
          rel="noopener noreferrer"
        >
          Votre annonce gratuit
        </a>
      </header>

      {/* Barre de recherche des annonces */}
      <div className="SearchBar">
        <input type="text" placeholder="Rechercher une annonce..." />
        <button>Rechercher</button>
      </div>

      {/* Boutons des catégories */}
      <div className="Categories">
        {categories.map((category) => (
          <button key={category} className="Category-link">
            {category}
          </button>
        ))}
      </div>

      {/* Section des annonces populaires */}
      <section className="Section">
        <h2>Annonces Populaires</h2>
        <div className="Annonces">
          {annoncesPopulaires.map((annonce) => (
            <div key={annonce.id} className="Annonce">
              <img src={annonce.image} alt={annonce.titre} />
              <h3>{annonce.titre}</h3>
              <p>{annonce.description}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Section des anciennes annonces */}
      <section className="Section">
        <h2>Anciennes Annonces</h2>
        <div className="AnciennesAnnonces">
          {anciennesAnnonces.map((annonce) => (
            <div key={annonce.id} className="AncienneAnnonce">
              <img src={annonce.image} alt={annonce.titre} />
              <h3>{annonce.titre}</h3>
              <p>{annonce.description}</p>
              <button onClick={() => handleAfficherAnnonce(annonce.id)}>
                Afficher l'annonce
              </button>
            </div>
          ))}
        </div>
      </section>
      <footer className="Footer">
        <p>© 2024 MAN-PUB. Tous droits réservés.</p>
        <p>
          Site réalisé par <a href="#">M.ABASSA</a>
        </p>
      </footer>
    </div>
  );
}

export default App;
