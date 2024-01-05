const second = 1000;
const sec=document.getElementById("second");
const mse=document.getElementById("ms");
let start_date=new Date();
let interval;
let distance=0;
let distance_bef=0;
const startBtn=document.getElementById("start");
const stopBtn=document.getElementById("stop");
const resetBtn=document.getElementById("reset");
startBtn.addEventListener("click",start_time);
stopBtn.addEventListener("click", stop_time);
resetBtn.addEventListener("click", reset_time);

function fillZero(num) {
    // 1 -> 01
    return String(num).padStart(2, '0');
}

function update_time(){
    const toStr=start_date.getTime();
    const now=new Date();
    const toNow=now.getTime();
    distance=toNow-toStr;
    sec.innerText=fillZero(Math.floor(((distance_bef+distance)/second)));
    mse.innerText=fillZero(Math.floor(((distance_bef+distance)%second)/10));
}

function start_time(){
    start_date=new Date();
    interval=setInterval(update_time,1);
}

function stop_time(){
    clearInterval(interval);
    distance_bef+=distance;

    make_record()
}

function reset_time(){
    sec.innerText="00";
    mse.innerText="00";
    distance_bef=0;
}


// 여기서 부턴 기록
function make_record(){
    const rec=document.getElementsByClassName("recording_inner");
}

const recContainer=document.getElementsByClassName("record");
console.log(recContainer);
recContainer.addEventListener("click",(e)=>{
    e.target.classList.toggle("checked");
    console.log(e);
})