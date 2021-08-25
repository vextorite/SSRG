import React from "react";
import "../component-styles/start.css";
import loginImg from "../login.png";
import signUp from "../signup.png";

export default function Buttons(props) {
  return (

  <div className = "start">
      <div className="titleText">Login or Sign Up to continue</div>
<button onClick={props.login} className="menuButton"><img className="buttonImg" src={loginImg}></img><br></br>Login</button>
<br></br>
<button onClick={props.signup} className="menuButton"><img className="buttonImg" src={signUp}></img><br></br>Sign Up</button>
 </div>
  
  );
}