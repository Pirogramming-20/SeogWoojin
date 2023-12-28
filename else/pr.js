// 3. 시간을 밀리초 단위로 변환
const second = 1000;
const minute = second * 60;
const hour = minute * 60;
const day = hour * 24;


// 1. 값을 바꿀 element를 가져오기
const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");

// 4. 두자리수로 변환하는 함수
function fillZero(num) {
  // 1 -> 01
  return String(num).padStart(2, '0');
}


// 2. 종강 날까지 남은 시간을 계산하는 함수
function getCountDown() {
  const now = new Date();
  console.log(now);

  const nowTime = now.getTime();
  console.log(nowTime);
  // 1970 1 1기준으로 ms(밀리초)단위로 나타냄
  const newYear = "02/22/2024";
  const newYearTime = new Date(newYear).getTime();
  console.log(newYearTime);

  const distance = newYearTime - nowTime;

  daysEl.innerText = fillZero(Math.floor(distance/day));
  hoursEl.innerText = fillZero(Math.floor((distance % day) /hour));
  minutesEl.innerText = fillZero(Math.floor((distance % hour) /minute));
  secondsEl.innerText =  fillZero(Math.floor((distance % minute) /second));
}

// getCountDown();

// setInterval(function, time);

setInterval(getCountDown, 1);
// getCountDown()함수를 1밀리초마다 호출