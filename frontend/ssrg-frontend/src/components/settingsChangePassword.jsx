import React from "react";
import "../component-styles/reactReportViewer.css";

export default function SettingsChangePassword(props) {
  return (
<div>
<div className ="submitSection1">
<div className="submitLanguageBox">
    <div id="titleBox3" className="submitLanguageBoxTitle">Change your password</div> 
<div className="templateName"  id="templateNameObj">
  <div className="separatorSettings"></div>
New password <br></br>
<input id="tempLoc" className="templateNameInput"></input>
<br></br>
<div className="separatorSettings"></div>
Confirm password <br></br>
<input id="tempLoc" className="templateNameInput"></input>
<br></br>
<div className="separatorSettings"></div>
<button className="templateNameConfirm" onClick={props.back}> back</button>
<button className="templateNameConfirm"> Confirm</button>
</div>
</div>
<div className="correctAlignment"></div>
</div>
</div>
  
  );
}