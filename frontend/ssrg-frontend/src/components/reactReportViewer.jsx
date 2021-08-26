import React from "react";
import sample1 from "../Sample-1.jpg";
import sample2 from "../Sample-2.jpg";
import "../component-styles/reactReportViewer.css";

export default function ReactReportViewer(props) {



  return (
<div>
<a target="_blank" href="https://demo.ssrg.online/Sample.pdf"><img className="sampleDemoPDF" src={sample1}></img></a>
   <br></br>
   <a target="_blank" href="https://demo.ssrg.online/Sample.pdf"> <img className="sampleDemoPDF" src={sample2}></img></a>
     
</div>
  
  );
}