
import React from "react";
import "../component-styles/header.css";
import logo from "../SSRG_logo.svg";

export default function Header() {
  return (
    <div className="Header">

    <img alt="UCT CS Dept Logo" className = "headShotImg" src = {logo}  ></img><br></br>

    <b>Automated Software Similarity
Report Generator </b>
   
    <div className = "title">
    Sashen Naidoo - Sanele Hlongwane - Suvanth Ramruthen
    </div>
  
    </div>

  );
  }