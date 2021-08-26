import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";

export default function Settings(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle">USER options</div>
<br></br>
<p> Demo: This functionality is not integrated yet. 
  <br></br>It will be available in the final version and will allow 
  users to change account settings such as their email address and upload 
  preferences.

</p>
</div>
</div>
  
  );
}