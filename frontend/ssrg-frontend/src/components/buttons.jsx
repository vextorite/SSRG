import React from "react";
import "../component-styles/buttons.css";
import submit from '../submit.png';
import guide from '../guide.png';
import report from '../report.png';
export default function Buttons(props) {
  return (

  <div className = "buttons">
    <div className="titleText">Select an option to continue</div>
<button onClick={props.about} className="menuButton"><img className="buttonImg" src={submit}></img><br></br>Submit a job</button>
<br></br>
<button onClick={props.skills} className="menuButton"><img className="buttonImg" src={report}></img><br></br>View job status</button>
<br></br>
<button onClick={props.awards} className="menuButton"><img className="buttonImg" src={guide}></img><br></br>User Options</button>
 </div>
  
  );
}