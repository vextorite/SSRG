import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";
import JobComponent from './jobStatusDisplay.jsx';

export default function JobStatus(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to home</button>
<div>
<div className="submitPageTitle">View job statuses</div>
<div className="displayComponentPanel"> 
<JobComponent id="1" refn="2408154501" state="pending"></JobComponent>
<JobComponent id="2" refn="2308195002" state="complete"></JobComponent>
<JobComponent id="3" refn="2308195001" state="complete"></JobComponent>
<JobComponent id="4" refn="2208172101" state="error"></JobComponent>
<JobComponent id="5" refn="2208135201" state="complete"></JobComponent>
</div>
<div className="key">
  <div>
  <div className="keyItem"><div className="keyItemTitle">Complete</div> <div className="complete"></div></div>
  <div className="keyItem"><div className="keyItemTitle">Pending</div> <div className="pending"></div></div>
  <div className="keyItem"><div className="keyItemTitle">Error</div> <div className="error"></div></div>
  </div>
</div>
</div>
</div>
  
  );
}