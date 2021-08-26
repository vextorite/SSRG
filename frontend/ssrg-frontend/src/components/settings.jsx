import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";

export default function Settings(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div className="submitPageTitle">USER options</div>
</div>
  
  );
}