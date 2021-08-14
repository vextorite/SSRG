import './App.css';

import Header from './components/header.jsx';
import Body from './components/body.jsx';

var dark=true;

function changeColor(){
if (dark){
  dark=false;
  lightMode();
}
else{
  dark=true;
  darkMode();
}
}

function darkMode(){
  document.getElementById("colorChangeButton").innerHTML="Day mode";
  document.documentElement.style.setProperty('--mainColor', 'black');
  document.documentElement.style.setProperty('--contrastColor', 'white');
  document.documentElement.style.setProperty('--mainColor2', 'rgb(56, 56, 56)');
  document.documentElement.style.setProperty('--mainColor2Transparency', 'rgb(56, 56, 56, 0.911)');

}

function lightMode(){
  document.getElementById("colorChangeButton").innerHTML="Night mode";
  document.documentElement.style.setProperty('--mainColor', 'white');
  document.documentElement.style.setProperty('--contrastColor', 'black');
  document.documentElement.style.setProperty('--mainColor2', 'rgb(190, 190, 190)');
  document.documentElement.style.setProperty('--mainColor2Transparency', 'rgb(190, 190, 190, 0.911)');
 
}

window.onload = window.onresize = function (){
  //on load or resize of window
  resizeBody();
}

function resizeBody() {
// function to resize the body to occupy maximum display size while maintaining header and footer on screen at all times, cannot be done properly through CSS, window.innerHeight is not equal to css "vh" on certain devices.
var header= document.getElementById("header");
var body= document.getElementById("body");
var footer= document.getElementById("footer");
var deviceHeight = window.innerHeight;
var usableArea=deviceHeight-(header.clientHeight+footer.clientHeight)
body.style.height=usableArea+"px";
}

function App() {
  return (
       <div className="App">

  <div id="header">
    <Header></Header>
  </div>
  

  <div id="body" >
   <Body></Body>
  </div>
  


   <div id="footer">

   <div className="switchDisplayMode">
   CSC3003S 2021 | NDXSAS021-HLNSAN005-RMRSUV002 | reactJS-Django-Python-Celery-MongoDB-GITLAB | <button id="colorChangeButton" onClick ={()=>changeColor()}>Day mode</button>
     </div>

   </div>


        </div>
  );
}

export default App;