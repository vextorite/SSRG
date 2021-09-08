import {React, useState, useEffect} from "react";
import "../component-styles/jobStatusDisplay.css";
import JobComponent from './jobStatusDisplay.jsx';

export default function FetchingData(props) {


    const [data,setData] = useState([]);

    useEffect(()=> {
        loadData();
    },[]);

    const loadData = async () =>{
        await fetch("http://127.0.0.1:8000/api/jobstatus/done")
        .then(response => response.json())
        .then(receivedData => setData(receivedData))
    }

  return (


<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle"></div>
<br></br>
show fetched data here

<br></br>

{data.map(user => (
<JobComponent key={user.id} Uid={user.id} dateTime={user.uploadDate} state="complete" refn={user.id}></JobComponent>
))}


</div>
</div>
  
  );
}