import React from "react";
import "../component-styles/settingsMenu.css";

export default function SettingsMenu(props) {
  return (
<div>
<button className="buttonSettingsMenu" onClick={props.pass}>Change your password</button>
<br></br>
<button className="buttonSettingsMenu" onClick={props.mail}>Change your email address</button>
</div>
  
  );
}