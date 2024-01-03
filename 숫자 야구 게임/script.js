// 전역 변수 설정
let rep=0;
let strike=0;
let ball=0;

// 중복 없는 정답을 생성하는 함수
const ans=[];
rand_num();
function rand_num(){
    let i=0;
    while(i<3){
        let n=Math.floor(Math.random()*10);
        if(! sameNum(n)){
            ans.push(n);
            i++;
        }
    }
    function sameNum(n){
        for(let i=0; i<ans.length; i++){
            if(n===ans[i]){
                return true;
            }
        }
        return false;
    }
    return;
}

// html click 이벤트 처리 (main함수)
function check_numbers(){

    const n1=document.getElementById('number1').value;
    const n2=document.getElementById('number2').value;
    const n3=document.getElementById('number3').value;

    // 만약 요소가 비워졌을 경우
    if(n1=='' || n2=='' || n3==''){ 
        document.getElementById('number1').value=null;
        document.getElementById('number2').value=null;
        document.getElementById('number3').value=null;
        return;
    }

    // 볼 스트라이크 판정
    check(n1,n2,n3);

    // 판정을 바탕으로 result 업데이트
    update_result(n1,n2,n3);

    // 스크롤을 항상 하단으로
    let objDiv=document.querySelector('.result-display');
    objDiv.scrollTop=objDiv.scrollHeight;
    
    // 종료 조건 처리
    if(strike==3){
        print_success();
        const button=document.querySelector('.submit-button');
        button.disabled=true;
    }

    else if(rep>=9){
        print_fail();
        const button=document.querySelector('.submit-button');
        button.disabled=true;
    }

    // 값 초기화
    document.getElementById('number1').value=null;
    document.getElementById('number2').value=null;
    document.getElementById('number3').value=null;

    return;
}

// 기존에 있던 html string 에 새로운 html 추가
function update_result(n1,n2,n3){
    const container=document.querySelector('.result-display');
    const section=document.querySelectorAll('.result-display .check-result');
    
    let lst=[];

    for (let i = 0; i < section.length; i++) {
        lst.push(section[i].outerHTML);
    }
    
    // 새로운 html 만들기
    let intoSection;
    if(strike==0 && ball==0){
        intoSection=makeOutHtml(n1,n2,n3);
    }
    else{
        intoSection=makeHtml(n1,n2,n3);
    }


    lst.push(intoSection);
    container.innerHTML=lst.join('');

    return;
}

// 아웃일 경우
function makeOutHtml(n1,n2,n3){
    return `<div class="check-result">
    <div class="left">${n1} ${n2} ${n3}</div>
    :
    <div class="right">
        <div class="out num-result">O</div>
    </div>
    </div>`;
}

// 그외
function makeHtml(n1,n2,n3){
    return `<div class="check-result">
    <div class="left">${n1} ${n2} ${n3}</div>
    :
    <div class="right">
        ${strike} <div class="strike num-result">S</div>
        ${ball} <div class="ball num-result">B</div>
    </div>
    </div>`;
}

function check(n1,n2,n3){
    const arr=[n1,n2,n3];
    // 매 check 마다 스트라이크 볼 초기화
    strike=0;
    ball=0;

    for(let i=0; i<3; i++){
        const num=arr[i];

        for(let j=0; j<3; j++){
            if(num==ans[j]){
                if(i==j){
                    strike+=1;
                }
                else{
                    ball+=1;
                }
            }
        }
    }
    

    // 시도 횟수 증가
    rep=rep+1;
    return;
}


function print_fail(){
    const container=document.querySelector('.game-result');
    container.innerHTML = `<img src="fail.png"/>`;
}

function print_success(){
    const container=document.querySelector('.game-result');
    container.innerHTML = `<img src="success.png"/>`;
}