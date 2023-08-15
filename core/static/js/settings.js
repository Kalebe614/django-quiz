/* Settings Timer*/

let hr, min, sec, ms,
  startTimer;
let hours = document.getElementById('hr')
let minutes = document.getElementById('minute')
/* Setting Event Change about hour*/
hours.addEventListener('change', function(){
  hr = this.value
  document.querySelector("span[class='hour']").innerHTML =hr
})
minutes.addEventListener('change', function(){
  min = this.value
  document.querySelector("span[class='minute']").innerHTML =min
})

const startBtn = document.querySelector(".start"),
  stopBtn = document.querySelector(".stop"),
  resetBtn = document.querySelector(".reset");
startBtn.addEventListener("click", start);
stopBtn.addEventListener("click", stop);
resetBtn.addEventListener("click", reset);

reset(); // Initialize the timer with 5 minutes
putValue();

function start() {
  startBtn.classList.add("active");
  stopBtn.classList.remove("stopActive");
  
  if (!startTimer) {
    startTimer = setInterval(() => {
      ms--;
      if (ms < 0) {
        ms = 99;
        sec--;
        if (sec < 0) {
          sec = 59;
          min--;
          if (min < 0) {
            min = 59;
            hr--;
            if (hr < 0) {
              stop();
            }
          }
        }
      }
      putValue();
    }, 10); // 1000ms = 1s
  }
}

function stop() {
  startBtn.classList.remove("active");
  stopBtn.classList.add("stopActive");
  clearInterval(startTimer);
  startTimer = null; // Reset the timer variable
}

function reset() {
  startBtn.classList.remove("active");
  stopBtn.classList.remove("stopActive");
  clearInterval(startTimer);
  startTimer = null; // Reset the timer variable
  hr = 0;
  min = 5;
  sec = ms = 0;
}

function putValue() {
  document.querySelector(".millisecond").innerText = ms;
  document.querySelector(".second").innerText = sec;
  document.querySelector(".minute").innerText = min;
  document.querySelector(".hour").innerText = hr;
}


