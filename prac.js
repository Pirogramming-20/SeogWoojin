const dateNode=document.querySelector("#date");
const hourNode=document.querySelector("#hour");
const minuteNode=document.querySelector("#minute");
const secondNode=document.querySelector("#second");

function calculateTime(){
    const now=new Date();
    const endDate=new Date("2024-02-20:00:00:00+0900");

    const secondToMiliSec=1000;
    const minuteToMiliSec=secondToMiliSec*60;
    const hourToMiliSec=minuteToMiliSec*60;
    const dayToMiliSec=hourToMiliSec*24;


    const diffTime=endDate.getTime()-now.getTime();
    console.log(diffTime)

    const date=Math.floor(diffTime/dayToMiliSec);
    const hour=Math.floor((diffTime%dayToMiliSec)/hourToMiliSec);
    const minute=Math.floor((diffTime%hourToMiliSec)/minuteToMiliSec);
    const second=Math.floor((diffTime%minuteToMiliSec)/secondToMiliSec);

    dateNode.innerHTML = date;
    hourNode.innerHTML=hour;
    minuteNode.innerHTML=minute;
    secondNode.innerHTML=second;
}

setInterval(calculateTime,1000);
