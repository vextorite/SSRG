
import React from "react";
import "../component-styles/header.css";
import uct from "../uct.png";

export default function Header() {
  return (
    <div className="Header">

    <img alt="UCT CS Dept Logo" className = "headShotImg" src = {uct}  ></img><br></br>

    <b> Capstone Project (2021) 
      <br></br>University of Cape Town - Department of Computer Science
      <br></br>"An Automated Software Similarity
Report Generator for CS Assignments" </b>
   
    <div className = "title">
    Sashen Naidoo - Sanele Hlongwane - Suvanth Ramruthen
    </div>
  
    </div>

  );
  }