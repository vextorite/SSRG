import {React, useState} from "react";
import "../component-styles/settings.css";
import SettingsMenu from "./settingsMenu.jsx";
import SettingsChangeEmail from "./settingsChangeEmail.jsx";
import SettingsChangePassword from "./settingsChangePassword.jsx";

export default function Settings(props) {


const [currentScreen, setScreen]= useState(0);

function screenToShow(){
switch(currentScreen){
  case 0:
    return <SettingsMenu mail={()=>setScreen(1)} pass={()=>setScreen(2)}></SettingsMenu>;
    break;
  case 1:
    return <SettingsChangeEmail back={()=>setScreen(0)}></SettingsChangeEmail>;
    break;
  case 2:
    return <SettingsChangePassword back={()=>setScreen(0)}></SettingsChangePassword>;
    break;

}
}

  return (

<div className="mainJobs">
<button onClick={props.back} className="backBtn">Return to menu</button>
<div>
<div className="submitPageTitle">USER options</div>
<br></br>


{screenToShow()}

</div>
</div>
  
  );
}