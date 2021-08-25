import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";

export default function JobStatusDisplay(props) {
    const [mode, setMode] = useState(false);

    function getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
    }

var card= ("Ecard"+props.id);
var content= ("Econtent"+props.id);
var control= ("EExpandContract"+props.id);

    if ((document.getElementById("Ecard"+props.id)!=null)&&(document.getElementById("EExpandContract"+props.id)!=null)){
        switch (mode){
          case false:
              document.getElementById(card).style.height= "40px";
              document.getElementById(content).style.visibility="hidden";
              document.getElementById(control).innerHTML="+";
              break;
          case true:
             document.getElementById(("Ecard"+props.id)).style.height= "auto";
             document.getElementById(("Econtent"+props.id)).style.visibility="visible";
             document.getElementById(("EExpandContract"+props.id)).innerHTML="-";
             break;
        }
      }


      if (mode){
        return (
      
      <div className="CardOutline" id={card}>
        <div className="CardHeader">
      <div className="CardHeadingLeft"><div className={props.state}></div></div> 
      <div className="CardHeadingMid"><div className="headingDivInner">Job #{props.refn}</div> </div>
      <div className="CardHeadingRight" ><button id={control} onClick={()=>setMode(!mode)}className="Expand">+</button></div> 
      </div>
      <div className="CardContent" id={content}>


      </div>

      </div>
      
      
        );
      }
      else{
        return (
      
          <div className="CardOutline" id={card}>
            <div className="CardHeader">
          <div className="CardHeadingLeft"><div id="colorIdentifier" className={props.state}></div></div> 
          <div className="CardHeadingMid"><div className="headingDivInner">Job #{props.refn}</div> </div>
          <div className="CardHeadingRight" ><button id={control} onClick={()=>setMode(!mode)}className="Expand">+</button></div> 
          </div>
          <div className="CardContent" id={content}></div>
          </div>
          
          
            );
      }
    }
        





