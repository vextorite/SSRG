import {React, useState} from "react";
import "../component-styles/jobStatusDisplay.css";
import JobComponent from './jobStatusDisplay.jsx';


export default function JobStatus(props) {

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle">View job statuses</div>
<div className="displayComponentPanel"> 
<JobComponent id="1" refn="2408154501" state="pending" heading="Job Pending" content="This submission report is still pending an outcome from MOSS. [Submitted Attachments: 'CSC3002F Assignment 7']"></JobComponent>
<JobComponent id="2" refn="2308195002" state="complete" heading="Job Success" content="This submission report has been generated successfully. [Submitted Attachments: 'CSC3002F Assignment 6']"></JobComponent>
<JobComponent id="3" refn="2308195001" state="complete" heading="Job Success" content="This submission report has been generated successfully. [Submitted Attachments: 'CSC3002F Assignment 5']"></JobComponent>
<JobComponent id="4" refn="2208172101" state="error" heading="Job Error" content="This submission failed due to a MOSS error: MOSS302: 'file exceeded input limitations'. [Submitted Attachments: 'CSC3002F Assignment 4']"></JobComponent>
<JobComponent id="5" refn="2208135201" state="complete" heading="Job Success" content="This submission report has been generated successfully. [Submitted Attachments: 'CSC3002F Assignment 3']"></JobComponent>
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