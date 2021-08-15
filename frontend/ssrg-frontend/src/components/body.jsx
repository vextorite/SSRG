import React,{useState} from "react";
import "../component-styles/body.css";
import Buttons from './buttons';
import Display from './genericDisplay';
import content from '../content.json';
import Login from './login.jsx';
import SignUp from './signUp.jsx';
import Start from './start.jsx';
import SubmitJob from "./submitJob.jsx";
export default function Body() {
    
    const [screen, setScreen] = useState(10);

   function screenToShow(){
switch(screen){
    case 0:
        return <Buttons about={()=>setScreen(1)} skills={()=>setScreen(2)} awards={()=>setScreen(3)} experience={()=>setScreen(4)} contact={()=>setScreen(5)}></Buttons>;
    case 1:
        return <SubmitJob></SubmitJob>;
    case 2:
        return <Display returnHome={()=>setScreen(0)} cont1 = {"view job status"} cont2 = {content.skillsPage.section2.join('\n')}></Display>;
    case 3:
        return <Display returnHome={()=>setScreen(0)} cont1 = {"user guide"} cont2 = {content.awardsPage.section2.join('\n')}></Display>;
    case 4:
        return <SignUp signup={()=>setScreen(1)}></SignUp>;
    case 5:
        return <Login login={()=>setScreen(0)} signup={()=>setScreen(4)}></Login>;
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