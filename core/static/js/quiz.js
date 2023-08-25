let quizData = []
let totalIndex 
let currentQuestionIndex = 0; 
const btnNext = document.querySelector('.btn-next');
let btnOptions = document.querySelectorAll("button[class='alert option']");

const questionTitle = document.getElementById('question-quiz')

const resp1 = document.querySelector("span.response1") 
const resp2 = document.querySelector("span.response2")
const resp3 = document.querySelector("span.response3")
const resp4 = document.querySelector("span.response4")

// Load question 
window.addEventListener('load', () => {
    // Fazer uma requisição GET usando Axios
    axios.get('http://127.0.0.1:8000/api/questions/')
      .then(function (response) {
        // Armazenar os dados da API em quizData
        quizData = response.data
        totalIndex = quizData.length
        showQuestion();
      })
      .catch(function (error) {
        console.error('Erro ao obter dados da API:', error);
      });
  });

//Show Questions and define the what aswwer is correct or not 
function showQuestion() {
    answers = quizData[currentQuestionIndex].answers
    questionTitle.textContent = quizData[currentQuestionIndex].question

    resp1.textContent = answers[0].text
    resp1.setAttribute('data', answers[0].is_correct)

    resp2.textContent = answers[1].text
    resp2.setAttribute('data', answers[1].is_correct)

    resp3.textContent = answers[2].text
    resp3.setAttribute('data', answers[2].is_correct)

    resp4.textContent = answers[3].text
    resp4.setAttribute('data', answers[3].is_correct)
}


//Verifying if the question is correct or not and apply the class attribute when selected
btnOptions.forEach(opt => { opt.addEventListener('click', function(event){

      const spanData = event.currentTarget.querySelector('.text').getAttribute('data')
     
      if(spanData === 'true'){
        opt.setAttribute('class', 'alert alert-success option')
        deactiveOptions()
      }else{
        opt.setAttribute('class', 'alert alert-danger option')
        deactiveOptions()
      }
      
})})

//Redefine the class attribute and activate the buttons
function redefineAttributeClass(){
  btnOptions.forEach(btn => { 
     btn.setAttribute('class', 'alert option' )
     btn.disabled = false})
}

//Deactive all options and able the botton to next question
function deactiveOptions(){
  
  btnOptions.forEach(opt =>{opt.disabled = true})
}
//Go to next question or remove the button next if don't have more questions
btnNext.addEventListener('click', function(){
  if( currentQuestionIndex+1 >= totalIndex ){

  }else{
    currentQuestionIndex++
    redefineAttributeClass()
    showQuestion()
  }
})


//Send the result of quiz to the page result
