// Header.js
import React from "react";
import logo from "../logo.png";

function Header() {
  return (
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
  );
}

export default Header;
