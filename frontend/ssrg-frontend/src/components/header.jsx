
import React from "react";
import "../component-styles/header.css";
import logo from "../SSRG_logo.svg";

export default function Header() {
  return (
    <div className="Header">

   <a href="https://demo.ssrg.online/"><img alt="SSRG Logo" className = "headShotImg" src = {logo}  ></img></a><br></br>

    <b>Automated Software Similarity
Report Generator </b>
   
    <div className = "title">
    Sashen Naidoo - Sanele Hlongwane - Suvanth Ramruthen
    </div>
  
    </div>

  );
  }