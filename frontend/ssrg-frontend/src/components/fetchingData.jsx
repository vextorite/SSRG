import {React, useState, useEffect} from "react";
import "../component-styles/jobStatusDisplay.css";

export default function FetchingData(props) {


    const [data,setData] = useState([]);

    useEffect(()=> {
        loadData();
    },[]);

    const loadData = async () =>{
        await fetch("http://localhost:5555")
        .then(response => response.json())
        .then(receivedData => setData(receivedData))
    }

    console.log(data);
  return (


<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle"></div>
<br></br>
show fetched data here

<br></br>

{data.map(user => (
<div key={user.id}>{user.name}</div>
))}


</div>
</div>
  
  );
}