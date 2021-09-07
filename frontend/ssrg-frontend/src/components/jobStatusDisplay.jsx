import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";
import ReportViewer from "./reactReportViewer.jsx";


export default function JobStatusDisplay(props) {
    const [mode, setMode] = useState(false);


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
function reportViewer(){
  if (!props.state.localeCompare("complete")){
    return <ReportViewer></ReportViewer>;
  }
  else{
    return "No Job Report Available";
  }
}

      if (mode){
        return (
      
      <div className="CardOutline" id={card}>
        <div className="CardHeader">
      <div className="CardHeadingLeft"><div className={props.state}></div></div> 
      <div className="CardHeadingMid"><div className="headingDivInner">Job #{props.refn} </div> </div>
      <div className="CardHeadingRight" ><button id={control} onClick={()=>setMode(!mode)}className="Expand">-</button></div> 
      </div>
      <div className="CardContent" id={content}>

     <div className="reportTitle">{props.heading} <br></br> {props.dateTime}</div> 
     <div className="reportContent">{props.content}</div> 

    
     <div className="reportPDFViewer"> 
  {reportViewer()}
     </div> 

      </div>

      </div>
      
      
        );
      }
      else{
        return (
      
          <div className="CardOutline" id={card}>
            <div className="CardHeader">
          <div className="CardHeadingLeft"><div id="colorIdentifier" className={props.state}></div></div> 
          <div className="CardHeadingMid"><div className="headingDivInner">Job #{props.refn} - {props.dateTime}</div> </div>
          <div className="CardHeadingRight" ><button id={control} onClick={()=>setMode(!mode)}className="Expand">+</button></div> 
          </div>
          <div className="CardContent" id={content}></div>
          </div>
          
          
            );
      }
    }
        





