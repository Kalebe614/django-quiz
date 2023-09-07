//Questions

let idCurrentQuestion = 1 //Current position

//Get total number of questions
const totalQuestions = document.getElementById('total-questions')
const total = parseInt(totalQuestions.getAttribute('data-total'))

const counter = document.getElementById("current-counter") //Span Counter of current question

let btnNext = document.getElementById('btn-next') //Button Next

let currentQuestion = document.getElementById(`number-${idCurrentQuestion}`); //Div Current Question


let linksQuestions = document.querySelectorAll('.questions a.link-questions'); //Links questions

//Call the next question
btnNext.onclick = function(event) {

    event.preventDefault()

    //If it is the last question, show the result
    if (idCurrentQuestion == total) {
        addUserAnswer(totalTime())//Add the user answer and the time
        window.location.href = '/result'
    } else {
        addUserAnswer()//Add the user answer
        showNextQuestion()//Show the next question
    }

}

//Hide the answered question and show the next question
function showNextQuestion() {

    activeLinks() //Active links
    
    disableBtnNext() //Disable btnNext

    currentQuestion.setAttribute('class', 'hidden-question') //Hidden the question

    idCurrentQuestion += 1 //Update currrent question

    counter.innerHTML = idCurrentQuestion //Update current counter

    currentQuestion = document.getElementById(`number-${idCurrentQuestion}`)

    currentQuestion.setAttribute('class', 'show-question')
}

//Define the selected question and disable the other questions
linksQuestions.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault()

        this.classList.add('clicked') //Define the selected question

        disableLinks() //Disable all other links

        enableBtnNext() //Enable the next question
    })
})

//Disable all links in the questions
function disableLinks() {
    linksQuestions.forEach(links => {
        links.classList.add('disabled')
    })
}

//Activate all links in the questions
function activeLinks() {
    linksQuestions.forEach(links => {
        links.classList.remove('disabled')
    })
}

//Total Time
function totalTime(){
    hoursDisplay = String(hours).padStart(2, '0')
    minutesDisplay = String(minutes).padStart(2, '0')
    secondsDisplay = String(seconds).padStart(2, '0')
  return String (hoursDisplay+':'+minutesDisplay+':'+secondsDisplay)
}

//Add answer 
function addUserAnswer(totalTime){
  
   let answerUser = document.querySelector(`.clicked[data-numb-answer="${idCurrentQuestion}"]`);
   //Get the ID of the Question
   let question = document.querySelector(`.quest-number-${idCurrentQuestion}`).getAttribute('data-numb-question')

   const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)[1];

   console.log(idCurrentQuestion, answerUser.textContent,totalTime)
   //Axios
    axios.post('/api/quiz/', {
      question: question,
      answer: answerUser.textContent,
      total_time: totalTime,
    }, {
      headers: {
        'X-CSRFToken': csrfToken,
      }
    })
    .then(function (response) {

    })
    .catch(function (error) {
      console.log(error);
     
    });
}

function disableBtnNext(){
  btnNext.classList.add('btn-disabled')
}

function enableBtnNext(){
  btnNext.setAttribute('class','')
}

// Timer
let hours = 0;
let minutes = 0;
let seconds = 0;

function updateTimer() {
    seconds++
    if (seconds >= 60) {
        seconds = 0
        minutes++
        if (minutes >= 60) {
            minutes = 0
            hours++
        }
    }

    const hoursDisplay = String(hours).padStart(2, '0')
    const minutesDisplay = String(minutes).padStart(2, '0')
    const secondsDisplay = String(seconds).padStart(2, '0')

    document.getElementById("hours").textContent = hoursDisplay
    document.getElementById("minutes").textContent = minutesDisplay
    document.getElementById("seconds").textContent = secondsDisplay
}

setInterval(updateTimer, 1000)

//Start the timer
document.addEventListener("DOMContentLoaded", function () {
  updateTimer()
});