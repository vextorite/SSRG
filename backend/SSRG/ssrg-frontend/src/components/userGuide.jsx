import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";

export default function UserGuide(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to home</button>
<div className="submitPageTitle">USER GUIDE</div>
</div>
  
  );
}