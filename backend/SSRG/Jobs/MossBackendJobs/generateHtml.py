def emailHtmlBody(jobUsername, jobID, jobStatus):
  '''
  Generating html body messages for emails
  The following parameters are piped into the HTML Document:
  jobUsername - Username of the account that submitted the MOSS job
  jobID - Unique identifier for submitted MOSS job
  '''
  message = f"""
    <!DOCTYPE html>
<html lang="en">



<link rel="stylesheet" type="text/css" >
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />


    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo.png" />


<style>

* {{
  margin: 0;
  padding: 0;
  border: 0;
  outline: 0;
  font-size: 100%;
  vertical-align: baseline;
  background: transparent;
}}

@font-face{{
    font-family: "Oswald";
    src: url("https://demo.ssrg.online/outcome/Oswald-Light.ttf");
  }}
  
  a{{
    color:var(--contrastColor)
  }}
  
  
  
  .App{{
    font-family: "Oswald", Arial;
    
  }}
  
  :root{{
    --mainColor:black;
    --mainColor2:rgba(22, 22, 22, 1);
    --buttonTitleContrast:rgba(53, 53, 53, 0.747);
    --mainColor2Transparency:rgba(10, 10, 10, 0.911);
    --contrastColor:white;
  }}
  
  button{{
    margin-top: 1px;
    font-size:clamp(9px, 4vw, 12px);
    background-color:var(--contrastColor);
    color:var(--mainColor);
    border-style: solid;
    border-radius: 5px;
    border-width: 1px;
    border-color: var(--mainColor);
    font-family: "Oswald", Arial;
  
  }}
  
  button:focus{{
    outline: none;
    box-shadow: none;
    -webkit-transition: background-color 1000ms linear;
    -ms-transition: background-color 1000ms linear;
    transition: background-color 1000ms linear;
  }}
  
  .switchDisplayMode{{
    color:var(--contrastColor);
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 11px;
    background-color:  rgb(46, 46, 46);
    text-align: center;
    padding: 4px 0px 5px 0px;
    height: 15px;
  }}

  .Header{{
    background-color: var(--mainColor2);
    color:var(--contrastColor);
    padding-top: 30px;
    text-align: center;
    letter-spacing: 1px;
  
  }}

  .headShotImg{{
    height: 100px;
  }}

 .title{{
     padding: 1px 0px 1px 0px;
     text-transform: uppercase;
     margin-top: 10px;
     /*background-color: var(--mainColor);*/
     background-color: rgb(46, 46, 46);
     letter-spacing: 1px;
     font-size: 13px;
     height: auto;
 }}

 .mainArea{{
   height:  100vh;
   background-image: url("https://demo.ssrg.online/outcome/tech1.jpg");
   background-size: cover;
 }}
 
 .titleText{{
  letter-spacing: 1px;
  text-transform: uppercase;
  font-size: 15px;
  font-family: "Oswald", Arial;
  color: white;
  text-align: center;
  border-radius: 6px;
  border-width: 2px;
height: 30px;
display: flex;
align-items: center;
justify-content: center;

 }}

 .notifBackground{{
   background-color: rgba(3, 3, 3, 0.904);
   width: 100%;
   height: 100%;

 }}

 .notifDiv{{
   background-color: rgba(75, 75, 75, 0.171);
   width:300px;
   height: 400px;
   padding: 30px 30px 30px 30px;
   border-radius: 15px;
   text-align: center;
   color:white;
   line-height: 220%;
   border-color: rgba(0, 117, 185, 0.233);
   border-width: 2px;
   border-style: solid;
   position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
 }}

 .StatusIconSpace{{
   width: 100%;

   height: 150px;
   margin-bottom: 10px;

 }}

 .done{{
   height:100px;
   width:100px;
  background-image:url("https://demo.ssrg.online/outcome/done.png");
  background-size: contain;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
 }}

 .pending{{
  height:100px;
  width:100px;
 background-image:url("https://demo.ssrg.online/outcome/load.gif");
 background-size: contain;
 border-radius: 50%;
 position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}}
.error{{
  height:100px;
  width:100px;
 background-image:url("https://demo.ssrg.online/outcome/err.png");
 background-size: contain;
 position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}}

.RedirectButton{{
  background-color: rgb(70, 70, 70);
border-color: white;
border-width: 1px;
border-style: solid;
padding: 5px 10px 5px 10px;
margin-bottom: 10px;
color:white;
}}

.RedirectButton:hover{{
  background-color: rgba(0, 148, 233, 0.37);
}}

.RedirectDiv{{
  margin-top: 10px;
  background-color: rgba(56, 56, 56, 0.253);
  border-radius: 12px;
  border-color: rgb(90, 90, 90);
  border-style: solid;
  border-width: 1px;
}}

.notifTitle{{
  font-size: 20px;
  color:rgb(0, 162, 255);
  margin-bottom: 5px;
}}

.notifDate{{
  font-size: 13px;
  color:rgb(148, 148, 148);
}}


</style>

    <title>SSRG Notification</title>
 

  <div class="App">

    <div id="header">
      <div class="Header">

        <a href="https://localhost:8000/"><img alt="SSRG Logo" class = "headShotImg" src = "https://demo.ssrg.online/Assets/logo.svg" ></img></a><br></br>
     
         <b>Automated Software Similarity
     Report Generator </b>
        
         <div class = "title">
         Sashen Naidoo - Sanele Hlongwane - Suvanth Ramruthen
         </div>
       
         </div>
    </div>
    

    <div id="main" class="mainArea" >
<div class="notifBackground">

<div class="notifDiv">

  <div class="StatusIconSpace">

    <div class="{jobStatus}"></div> <! can be "done", "error", "pending" ––> 
  </div>



  <div class="notifTitle">Hello, {jobUsername} </div>

  Thank you for submitting a job with us!
  <br>
  Your job is currently {jobStatus}
  <br>
  <div class="notifDate">[Latest update for {jobID}]</div>

  <div class="RedirectDiv">
  View your job status at SSRG Online
  <br>
  <a href="http://localhost:8000" target="_blank"><button class="RedirectButton">SSRG Online</button></a>
</div>


</div>

</div>
    </div>
    
  
  
     <div id="footer">
  
     <div class="switchDisplayMode">
      Powered by SSRG Email notification system
  
       </div>
  
     </div>
  
  
          </div>
        
          <script>window.onload = window.onresize = function (){{document.getElementById("main").style.height=(window.innerHeight-(document.getElementById("header").clientHeight+document.getElementById("footer").clientHeight))+"px";}}   </script>
      </html>
            """
  return message

def comparissonFrameConstructor(path0, path1,i, fRoot):
  '''
  Generating html to display the comparison of MOSS source code
  The following parameters are piped into the HTML Document:
  path0 - Path of first MOSS file in comparison
  path1 - Path of second MOSS file in comparison
  Parameters fRoot and i is used to generate the path where we will save the generated html file
  The parameters correspond to the following:
  fRoot - path to the job directory
  i - Integer value used to label comparisson html documents
  '''
  htmlMessage=f"""
        <!DOCTYPE html>
<html lang="en">

<style>

    .containerMain{{
        height: 90%;
        background-color: purple;
        display: flexbox;
    }}

    .menu{{
        float:left;
        width:50%;
        height: 100%;
    }}

    .box{{
        float:left;
        width:50%;
        height: 100%;
    }}


* {{
  margin: 0;
  padding: 0;
  border: 0;
  outline: 0;
  font-size: 100%;
  vertical-align: baseline;
  background: transparent;
}}

@font-face{{
    font-family: "Oswald";
    src: url("https://demo.ssrg.online/outcome/Oswald-Light.ttf");
  }}
  
  a{{
    color:var(--contrastColor)
  }}
  
  
  
  .App{{
    font-family: "Oswald", Arial;
    
  }}
  
  :root{{
    --mainColor:black;
    --mainColor2:rgba(22, 22, 22, 1);
    --buttonTitleContrast:rgba(53, 53, 53, 0.747);
    --mainColor2Transparency:rgba(10, 10, 10, 0.911);
    --contrastColor:white;
  }}
  
  button{{
    margin-top: 1px;
    font-size:clamp(9px, 4vw, 12px);
    background-color:var(--contrastColor);
    color:var(--mainColor);
    border-style: solid;
    border-radius: 5px;
    border-width: 1px;
    border-color: var(--mainColor);
    font-family: "Oswald", Arial;
  
  }}
  
  button:focus{{
    outline: none;
    box-shadow: none;
    -webkit-transition: background-color 1000ms linear;
    -ms-transition: background-color 1000ms linear;
    transition: background-color 1000ms linear;
  }}
  
  .switchDisplayMode{{
    color:var(--contrastColor);
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 11px;
    background-color:  rgb(46, 46, 46);
    text-align: center;
    padding: 4px 0px 5px 0px;
    height: 15px;
  }}

  .Header{{
    background-color: var(--mainColor2);
    color:var(--contrastColor);
    padding-top: 30px;
    text-align: center;
    letter-spacing: 1px;
  
  }}

  .headShotImg{{
    height: 100px;
  }}

 .title{{
     padding: 1px 0px 1px 0px;
     text-transform: uppercase;
     margin-top: 10px;
     background-color: rgb(46, 46, 46);
     letter-spacing: 1px;
     font-size: 13px;
     height: auto;
     z-index: 10;
 }}

 .mainArea{{
   height:  100vh;
   background-image: url("https://demo.ssrg.online/outcome/tech1.jpg");
   background-size: cover;
   display: flex;
   justify-content: center;
   align-items: center;
 }}
 
 .titleText{{
  letter-spacing: 1px;
  text-transform: uppercase;
  font-size: 15px;
  font-family: "Oswald", Arial;
  color: white;
  text-align: center;
  border-radius: 6px;
  border-width: 2px;
height: 30px;
display: flex;
align-items: center;
justify-content: center;

 }}

.HeaderMain{{
    text-align: center;
    background-color: rgba(5, 5, 5, 0.575);
    color:rgb(255, 255, 255);
    padding: 10px 0px 10px 0px;
    border-bottom-color: rgb(138, 138, 138);
    border-bottom-style: solid;
    border-bottom-width: 3px;
    margin-bottom: 5px;
}}

.mainContainerWrapper{{
    height: 80%;
    width:80%;
    border-radius: 15px;
    background-color: rgba(5, 5, 5, 0.575);
    padding: 5px 20px 10px 20px;
    border-color: rgb(138, 138, 138);
    border-style: solid;
    border-width: 2px;
}}

</style>


<meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />


    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo.png" />


    <title>SSRG Notification</title>
 

    <div class="App">
  
      <div id="header">
        <div class="Header">
  
          <a href="https://localhost:8000/"><img alt="SSRG Logo" class = "headShotImg" src = "https://demo.ssrg.online/Assets/logo.svg" ></img></a><br></br>
       
           <b>Automated Software Similarity
       Report Generator </b>
          
           <div class = "title">
           Sashen Naidoo - Sanele Hlongwane - Suvanth Ramruthen
           </div>
         
           </div>
      </div>
      
  
      <div id="main" class="mainArea" >
       <div class="mainContainerWrapper">
        <div class="HeaderMain">Job Comparison</div>

    <div class="containerMain">
        

<div class="menu">
    
<iframe  src="{path0}" frameborder="0" style="overflow:hidden;height:100%;width:100%" name="iframe_a" frameborder="1" scrolling="yes" width="100%" height="100%">
<p>Your browser does not support iframes.</p>
</iframe>
</div>
<div class="box">
<iframe frameborder="0" style="overflow:hidden;height:100%;width:100%" src="{path1}" name="iframe_b" frameborder="1" scrolling="yes" width="100%" height="100%">
</iframe>
</div>

</div>
</div>
</div>
    
  
  
<div id="footer">

<div class="switchDisplayMode">
    BUILT WITH DJANGO, PYTHON & CELERY

  </div>

</div>


     </div>
   
     <script>window.onload = window.onresize = function (){{document.getElementById("main").style.height=(window.innerHeight-(document.getElementById("header").clientHeight+document.getElementById("footer").clientHeight))+"px";}}   </script>
 </html>
        """
  f = open(f'{fRoot}/Comaprison_Record_{i}.html', 'w')
  f.write(htmlMessage)
  f.close