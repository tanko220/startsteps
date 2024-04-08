// Annonces.js
import React from "react";

function Annonces({ annonces }) {
  return (
    <section className="Section">
      <h2>Annonces Populaires</h2>
      <div className="Annonces">
        {annonces.map((annonce) => (
          <div key={annonce.id} className="Annonce">
            <img src={annonce.image} alt={annonce.titre} />
            <h3>{annonce.titre}</h3>
            <p>{annonce.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Annonces;
