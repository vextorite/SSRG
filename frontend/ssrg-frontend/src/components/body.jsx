import React,{useState} from "react";
import "../component-styles/body.css";
import Buttons from './buttons';
import Settings from './settings.jsx';
import Login from './login.jsx';
import SignUp from './signUp.jsx';
import Start from './start.jsx';
import SubmitJob from "./submitJob.jsx";
import JobStatus from "./jobStatus.jsx";

export default function Body() {
    
    const [screen, setScreen] = useState(10);

   function screenToShow(){
switch(screen){
    case 0:
        return <Buttons about={()=>setScreen(1)} skills={()=>setScreen(2)} awards={()=>setScreen(3)} experience={()=>setScreen(4)} contact={()=>setScreen(5)}></Buttons>;
    case 1:
        return <SubmitJob back={()=>setScreen(0)}></SubmitJob>;
    case 2:
        return <JobStatus back={()=>setScreen(0)}></JobStatus>;
    case 3:
        return <Settings back={()=>setScreen(0)}></Settings>;
    case 4:
        return <SignUp back={()=>setScreen(10)} signup={()=>setScreen(1)}></SignUp>;
    case 5:
        return <Login back={()=>setScreen(10)} login={()=>setScreen(0)} signup={()=>setScreen(4)}></Login>;
    default: 
        return <Start login={()=>setScreen(5)} signup={()=>setScreen(4)}></Start>;
    
}
    }

  return (
  <div className="bodyStyle">
    {screenToShow()}
    </div>
  );
}