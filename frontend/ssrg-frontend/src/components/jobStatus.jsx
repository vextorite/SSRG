import {React, useState, useEffect} from "react";
import "../component-styles/jobStatusDisplay.css";
import JobComponent from './jobStatusDisplay.jsx';


export default function JobStatus(props) {


  const [doneData,setDoneData] = useState([]);
  const [pendingData,setPendingData] = useState([]);
  const [errorData,setErrorData] = useState([]);

    useEffect(()=> {
        loadDoneData();
    },[]);

    useEffect(()=> {
      loadPendingData();
  },[]);

  useEffect(()=> {
    loadErrorData();
},[]);

    const loadDoneData = async () =>{
        await fetch("http://127.0.0.1:8000/api/jobstatus/done")
        .then(response => response.json())
        .then(receivedDoneData => setDoneData(receivedDoneData))
    }

    const loadPendingData = async () =>{
      await fetch("http://127.0.0.1:8000/api/jobstatus/pending")
      .then(response => response.json())
      .then(receivedPendingData => setPendingData(receivedPendingData))
  }

  const loadErrorData = async () =>{
    await fetch("http://127.0.0.1:8000/api/jobstatus/failed")
    .then(response => response.json())
    .then(receivedErrorData => setErrorData(receivedErrorData))
}

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle">View job statuses</div>
<div className="displayComponentPanel"> 

{doneData.map(doneDateMapped => (
<JobComponent key={doneDateMapped.id} id={doneDateMapped.id} dateTime={doneDateMapped.uploadDate} state="complete" refn={doneDateMapped.id}></JobComponent>
))}

{pendingData.map(pendingDateMapped => (
<JobComponent key={pendingDateMapped.id} id={pendingDateMapped.id} dateTime={pendingDateMapped.uploadDate} state="pending" refn={pendingDateMapped.id} heading="Job Pending" content={"This submission report is still pending an outcome from MOSS."} attachments={"Submitted Attachments: "+pendingDateMapped.files}></JobComponent>
))}

{errorData.map(errorDateMapped => (
<JobComponent key={errorDateMapped.id} id={errorDateMapped.id} dateTime={errorDateMapped.uploadDate} state="error" refn={errorDateMapped.id} heading="Job Error" content="This submission failed due to a MOSS error." attachments={"Submitted Attachments: "+errorDateMapped.files}></JobComponent>
))}

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