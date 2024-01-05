const second = 1000;
const sec=document.getElementById("second");
const mse=document.getElementById("ms");
let start_date=new Date();
let interval;
let distance=0;
let distance_bef=0;
const recording=document.getElementById("recording");
const startBtn=document.getElementById("start");
const stopBtn=document.getElementById("stop");
const resetBtn=document.getElementById("reset");
startBtn.addEventListener("click",start_time);
stopBtn.addEventListener("click", stop_time);
resetBtn.addEventListener("click", reset_time);

const trash=document.getElementById("remove");
trash.addEventListener("click",remove_record);
const all=document.getElementById("record_all_check");
all.addEventListener("click", check_all);

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


    const li=document.createElement("li");
    li.setAttribute("class","recording_inner");
    const input=document.createElement("input");
    input.setAttribute("type", "checkbox");
    input.setAttribute("id","record_check");
    input.addEventListener("click", function(event){
        if(event.target.checked){ //켜졌을 때
            let Box = document.querySelectorAll('#recording #record_check');
            let all_on=true;
            for (let i in Box) {
                if(Box[i].checked == false){
                    all_on=false;
                }
            }
            if(all_on==true){
                all.checked=true;
            }
        }
        else{ //꺼졌을 때
            if (all.checked==true){
                all.checked=false;
            }
        }
    });

    const div=document.createElement("div");
    let record = sec.textContent + ":" + mse.textContent;
    div.append(record);
    div.setAttribute("class", "record_time");

    const div2=document.createElement("div");

    li.appendChild(input);
    li.appendChild(div);
    li.appendChild(div2);

    recording.appendChild(li);
}

function remove_record(){
    let checkbox = document.querySelectorAll('#recording #record_check');
    for (let i in checkbox) {
        if (checkbox[i].checked) recording.removeChild(checkbox[i].parentNode);
    }
}

function check_all(){
    let Box = document.querySelectorAll('#recording #record_check');

    if (all.checked) {
        for (var i in Box) {
          Box[i].checked = true;
        }
    } else {
        for (var i in Box) {
          Box[i].checked = false;
        }
    }
}

function check_one(evt){
    evt.current
}