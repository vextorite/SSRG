import React from "react";
import "../component-styles/genericDisplay.css";
import { Markup } from '../../node_modules/interweave';

export default function Display(props) {


  return (

  <div className="display">
      <Markup content={props.cont1}></Markup>
      <hr></hr>
      <Markup content={props.cont2}></Markup>
      <div className="exit"><button onClick={props.returnHome} className="Close">Close page</button></div>
  </div>
  
  );
}