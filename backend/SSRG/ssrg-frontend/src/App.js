import './App.css';

import Header from './components/header.jsx';
import Body from './components/body.jsx';

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
   reactJS-Django-Python-Celery-GITLAB 
     </div>

   </div>


        </div>
  );
}

export default App;