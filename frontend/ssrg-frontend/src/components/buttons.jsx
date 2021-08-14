import React from "react";
import "../component-styles/buttons.css";

export default function Buttons(props) {
  return (

  <div className = "buttons">
<button onClick={props.about} className="menuButton">Submit a job</button>
<br></br>
<button onClick={props.skills} className="menuButton">View job status</button>
<br></br>
<button onClick={props.awards} className="menuButton">User guide</button>
 </div>
  
  );
}