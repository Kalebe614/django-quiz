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
        addUserAnswer()//Add the user answer
        showResult()
    } else {
        addUserAnswer()//Add the user answer
        showNextQuestion()//Show the next question
    }

}

//Hide the answered question and show the next question
function showNextQuestion() {

    activeLinks() //Active links
    
    disableBtnNext()

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

//Result 

//Show the final result
function showResult() {
    document.querySelector('div[class=box]').style.display = "none"
    document.querySelector('div[class=container-result]').style.display = "block"
}


function addUserAnswer(){
  
   let answerUser = document.querySelector(`.clicked[data-numb-question="${idCurrentQuestion}"]`);
   
   console.log(answerUser.textContent)
   console.log(answerUser.getAttribute('data-is-correct'))
   document.querySelector(`[class*="answer-user ${idCurrentQuestion}"]`).innerHTML = answerUser.getAttribute('data-numb-question')
  
   //Axios
   axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/quiz/',
    data: {
        "question": 2,
        "answer": "Teste Olá mundo",
        "total_time": null
    }
  });
}

function disableBtnNext(){
  btnNext.classList.add('btn-disabled')
}

function enableBtnNext(){
  btnNext.setAttribute('class','')
}