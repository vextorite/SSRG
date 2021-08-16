import React from "react";
import "../component-styles/loginSignUp.css";
import signUpImg from "../signup.png";
export default function signUp(props) {
  return (

<div className="loginMain">
<button onClick={props.back} className="backBtn">Return to home</button>
<div className="loginInner">
<div className="loginInputLabel">Username</div>
    <input className ="loginInput"></input>
    <br></br>
    <div className="loginInputLabel">Password</div>
    <input type="password" className ="loginInput" ></input>
    <br></br>
    <div className="loginInputLabel">Confirm Password</div>
    <input type="password" className ="loginInput" ></input>
    <br></br>
    <button onClick={props.signup} className="loginButton"><img className="loginImg" src={signUpImg}></img>
    <br></br>
Sign Up
 </button>
    </div>
</div>
  
  );
}