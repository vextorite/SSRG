import {React, useState} from "react";
import "../component-styles/submitJob.css";

export default function SubmitJob(props) {

function setStep1(){

    document.getElementById("langMainObj").style.visibility="visible";
document.getElementById("langMainObj").style.height="auto";
document.getElementById("DirectoryMainObj").style.visibility="hidden";
document.getElementById("DirectoryMainObj").style.height="0px";
document.getElementById("templateNameObj").style.visibility="hidden";
document.getElementById("templateNameObj").style.height="0px";
document.getElementById("fileUploadObj").style.visibility="hidden";
document.getElementById("fileUploadObj").style.height="0px";

}

function setStep2(){
document.getElementById("langMainObj").style.visibility="hidden";
document.getElementById("langMainObj").style.height="0px";
document.getElementById("DirectoryMainObj").style.visibility="visible";
document.getElementById("DirectoryMainObj").style.height="auto";
document.getElementById("templateNameObj").style.visibility="hidden";
document.getElementById("templateNameObj").style.height="0px";
document.getElementById("fileUploadObj").style.visibility="hidden";
document.getElementById("fileUploadObj").style.height="0px";
}

function setStep3(){
    document.getElementById("langMainObj").style.visibility="hidden";
    document.getElementById("langMainObj").style.height="0px";
    document.getElementById("DirectoryMainObj").style.visibility="hidden";
    document.getElementById("DirectoryMainObj").style.height="0px";
    document.getElementById("templateNameObj").style.visibility="visible";
    document.getElementById("templateNameObj").style.height="auto";
    document.getElementById("fileUploadObj").style.visibility="hidden";
    document.getElementById("fileUploadObj").style.height="0px";
    
}

function setStep4(){
    document.getElementById("langMainObj").style.visibility="hidden";
    document.getElementById("langMainObj").style.height="0px";
    document.getElementById("DirectoryMainObj").style.visibility="hidden";
    document.getElementById("DirectoryMainObj").style.height="0px";
    document.getElementById("templateNameObj").style.visibility="hidden";
    document.getElementById("templateNameObj").style.height="0px";
    document.getElementById("fileUploadObj").style.visibility="visible";
    document.getElementById("fileUploadObj").style.height="auto";
}


var language="";
var root = true;
var templateLocation ="";

 function setLang(lang){
    language=lang;
    document.getElementById("titleBox1").innerHTML="Programming language: "+language;
    setStep2();
 }

 function setRoot(state){
    root=state;
    if (root){
    document.getElementById("titleBox2").innerHTML="Submission files are in root";}
    else{
        document.getElementById("titleBox2").innerHTML="Submission files are in folders";
    }
    setStep3();
 }

 function setTemplateLocation(location){
     templateLocation=location;
     document.getElementById("titleBox3").innerHTML="The template file is: "+templateLocation;
    setStep4();
    }

    

   function refresh(){
    document.getElementById("titleBox1").innerHTML="What programming language would you like to submit?";
    document.getElementById("titleBox2").innerHTML="Where are submission files located?";
    document.getElementById("titleBox3").innerHTML="What is the name your template code file?";
        setStep1();

    }

  return (

<div className="mainSubmission">
    <div className="resetBtnDiv">
    <button onClick={()=>refresh()} className="resetBtn">Reset selections</button>
<button onClick={props.back} className="returnBtn">Return to menu</button>

</div>
    <div><div className="submitPageTitle">Create a new MOSS submission</div>
<br></br>

<div className ="submitSection1">
<div className="submitLanguageBox">
    <div id="titleBox1" className="submitLanguageBoxTitle">What programming language would you like to submit?</div> 
<div className="langMain" id="langMainObj">
<button onClick={()=>setLang("C")} className="pLang">C</button>
<button onClick={()=>setLang("CC")} className="pLang">CC</button>
<button onClick={()=>setLang("Java")} className="pLang">Java</button>
<button onClick={()=>setLang("ML")} className="pLang">ML</button>
<button onClick={()=>setLang("Pascal")} className="pLang">Pascal</button>
<button onClick={()=>setLang("Ada")} className="pLang">Ada</button>
<button onClick={()=>setLang("Lisp")} className="pLang">Lisp</button>
<button onClick={()=>setLang("Schema")} className="pLang">Schema</button>
<button onClick={()=>setLang("Haskell")} className="pLang">Haskell</button>
<button onClick={()=>setLang("Fortran")} className="pLang">Fortran</button>
<button onClick={()=>setLang("Ascii")} className="pLang">Ascii</button>
<button onClick={()=>setLang("VHDL")} className="pLang">VHDL</button>
<button onClick={()=>setLang("Perl")} className="pLang">Perl</button>
<button onClick={()=>setLang("Matlab")} className="pLang">Matlab</button>
<button onClick={()=>setLang("Python")} className="pLang">Python</button>
<button onClick={()=>setLang("Mips")} className="pLang">Mips</button>
<button onClick={()=>setLang("Prolog")} className="pLang">Prolog</button>
<button onClick={()=>setLang("Spice")} className="pLang">Spice</button>
<button onClick={()=>setLang("Visual Basic")} className="pLang">Visual Basic</button>
<button onClick={()=>setLang("C#")} className="pLang">C#</button>
<button onClick={()=>setLang("Modula2")} className="pLang">Modula2</button>
<button onClick={()=>setLang("A8086")} className="pLang">A8086</button>
<button onClick={()=>setLang("JavaScript")} className="pLang">JavaScript</button>
<button onClick={()=>setLang("PLSQL")} className="pLang">PLSQL</button>
</div>
</div>
<div className="correctAlignment"></div>
</div>

<div className="betweenDivsContainer"><div className="betweenDivs"></div></div>


<div className ="submitSection1">
<div className="submitLanguageBox">
    <div id="titleBox2" className="submitLanguageBoxTitle">Where are submission files located?</div> 
<div className="DirectoryMain"  id="DirectoryMainObj">
<button onClick={()=>setRoot(false)} className="locationButton1">Individual folders</button>
<button onClick={()=>setRoot(true)} className="locationButton2">Root Directory</button>
</div>
</div>
<div className="correctAlignment"></div>
</div>

<div className="betweenDivsContainer"><div className="betweenDivs"></div></div>

<div className ="submitSection1">
<div className="submitLanguageBox">
    <div id="titleBox3" className="submitLanguageBoxTitle">What is the name your template code file?</div> 
<div className="templateName"  id="templateNameObj">

<input id="tempLoc" className="templateNameInput"></input>
<button onClick={()=>setTemplateLocation(document.getElementById("tempLoc").value)} className="templateNameConfirm">Confirm</button>
</div>
</div>
<div className="correctAlignment"></div>
</div>

<div className="betweenDivsContainer"><div className="betweenDivs"></div></div>

<div className ="submitSection1">
<div className="submitLanguageBox">
    <div className="submitLanguageBoxTitle">Please upload your submission archive</div> 
<div className="fileUpload"  id="fileUploadObj">

do upload stuff here

<br></br>

<button className="templateNameConfirm">Start MOSS Submission</button>
</div>
</div>
<div className="correctAlignment"></div>
</div>

    </div>
</div>
  
  );
}