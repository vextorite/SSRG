import React,{useState} from "react";
import "../component-styles/body.css";
import Buttons from './buttons';
import Display from './genericDisplay';
import content from '../content.json';

export default function Body() {
    
    const [screen, setScreen] = useState(0);

   function screenToShow(){
switch(screen){
    case 0:
        return <Buttons about={()=>setScreen(1)} skills={()=>setScreen(2)} awards={()=>setScreen(3)} experience={()=>setScreen(4)} contact={()=>setScreen(5)}></Buttons>;
    case 1:
        return <Display returnHome={()=>setScreen(0)} cont1 = {content.aboutPage.section1.join('\n')} cont2 = {content.aboutPage.section2.join('\n')}></Display>;
    case 2:
        return <Display returnHome={()=>setScreen(0)} cont1 = {content.skillsPage.section1.join('\n')} cont2 = {content.skillsPage.section2.join('\n')}></Display>;
    case 3:
        return <Display returnHome={()=>setScreen(0)} cont1 = {content.awardsPage.section1.join('\n')} cont2 = {content.awardsPage.section2.join('\n')}></Display>;
    case 4:
        return <Display returnHome={()=>setScreen(0)} cont1 = {content.experiencePage.section1.join('\n')} cont2 = {content.experiencePage.section2.join('\n')}></Display>;
    case 5:
        return <Display returnHome={()=>setScreen(0)} cont1 = {content.contactPage.section1.join('\n')} cont2 = {content.contactPage.section2.join('\n')}></Display>;
    default:
        return <Buttons></Buttons>;
    
}
    }

  return (
  <div className="bodyStyle">
    {screenToShow()}
    </div>
  );
}