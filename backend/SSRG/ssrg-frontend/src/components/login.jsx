import React from "react";
import "../component-styles/loginSignUp.css";
import loginImg from '../login.png';
export default function login(props) {
  return (

<div className="loginMain">
  <div>
<div className="titleText">Login to continue</div>
<br></br>
  <button onClick={props.back} className="backBtn">Return to home</button>
<div className="loginInner">
  
<div className="loginInputLabel">Username</div>
    <input className ="loginInput"></input>
    <br></br>
    <div className="loginInputLabel">Password</div>
    <input type="password" className ="loginInput" ></input>
    <br></br>
    <button onClick={props.login} className="loginButton"><img className="loginImg" src={loginImg}></img>
    <br></br>
 Login
 </button>
 <br></br>
<button onClick={props.signup} className="signUpButton"> New user? Sign up</button>
</div>
    </div>
</div>
  
  );
}