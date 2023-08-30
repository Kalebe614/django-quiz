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
        showResult()
    } else {
        showNextQuestion()
    }

}

//Hide the answered question and show the next question
function showNextQuestion() {

    activeLinks() //Active links

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

