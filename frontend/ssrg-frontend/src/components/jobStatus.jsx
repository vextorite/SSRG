import {React, useState} from "react";
import "../component-styles/jobStatus.css";

export default function JobStatus(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to home</button>
<div className="submitPageTitle">View job statuses</div>
</div>
  
  );
}