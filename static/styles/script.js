const questions = [
    {
      question: "Are you looking for online or in-person activities?",
      type: "multiple-choice",
      answers: [
        { text: "Online"},
        { text: "In-person"},
        { text: "Both"},
      ]
    },
    {
      question: "How old are you?",
      type: "slider"
    },
    {
      question: "Are you looking for summer or year round activities?",
      type: "multiple-choice",
      answers: [
        { text: "Summer" },
        { text: "Year-round" },
        { text: "Both"}
      ]
    },
    {
        question: "What type of activities are you looking for?",
        type: "multiple-answer",
        answers: [
          { text: "Camps" },
          { text: "Courses" },
          { text: "Contests"}
        ]
      }
    // Add more questions here...
  ];
  
  let currentQuestionIndex = 0;
  let answers = [];
  
  const questionContainerElement = document.getElementById('question-container');
  const questionElement = document.getElementById('question');
  const answerButtonsElement = document.getElementById('answer-buttons');
  const nextButton = document.getElementById('next-btn');
  const sliderValueElement = document.getElementById('slider-value'); // Add a new element to display the slider value
  
  nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
  });
  
  function startQuiz() {
    currentQuestionIndex = 0;
    answers = [];
    nextButton.classList.add('hide');
    questionContainerElement.classList.remove('hide');
    setNextQuestion();
  }
  
  function setNextQuestion() {
    resetState();
    if (currentQuestionIndex < questions.length) {
      showQuestion(questions[currentQuestionIndex]);
    } else {
      // Quiz is finished, display results or do something else
      displayResults();
    }
  }
  
  function showQuestion(question) {
    questionElement.innerText = question.question;
    
    if (question.type === "multiple-choice") {
      const answers = question.answers;
      answers.forEach(answer => {
        const button = document.createElement('button');
        button.innerText = answer.text;
        button.classList.add('btn');
        sliderValueElement.style.display = 'none';
        button.addEventListener('click', () => selectAnswer(answer));
        answerButtonsElement.appendChild(button);
      });
    } else if (question.type === "slider") {
      const slider = document.createElement('input');
      slider.type = 'range';
      slider.min = 5;
      slider.max = 30;
      slider.value = 18; // Set a default value if needed
      slider.classList.add('slider');
      slider.classList.add('ageslider');
      sliderValueElement.style.display = 'flex';
      slider.addEventListener('input', () => {
        selectAnswer(slider.value);
        updateSliderValue(slider.value); // Update the displayed value dynamically
      });
      answerButtonsElement.appendChild(slider);
      
      sliderValueElement.innerText = slider.value; // Set the initial displayed value
    } 
    else if (question.type === "multiple-answer") {
        const answers = question.answers;
        answers.forEach(answer => {
          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.value = answer.text;
          checkbox.classList.add('checkbox');
          checkbox.addEventListener('change', () => selectAnswer(checkbox.value, checkbox.checked));
          
          const label = document.createElement('label');
          label.innerText = answer.text;
          label.classList.add('checkbox-label');
          
          const container = document.createElement('div');
          container.classList.add('checkbox-container');
          container.appendChild(checkbox);
          container.appendChild(label);
          
          answerButtonsElement.appendChild(container);
        });
      }
}


  function resetState() {
    nextButton.classList.add('hide');
    while (answerButtonsElement.firstChild) {
      answerButtonsElement.removeChild(answerButtonsElement.firstChild);
    }
  }
  
  function selectAnswer(answer, isChecked) {
    if (questions[currentQuestionIndex].type === "multiple-answer") {
      if (isChecked) {
        answers.push(answer);
      } else {
        const index = answers.indexOf(answer);
        if (index !== -1) {
          answers.splice(index, 1);
        }
      }
    } else {
      answers.push(answer);
    }
    
    nextButton.classList.remove('hide');
  }
  
  function displayResults() {
    var online = answers[0]["text"]
    sessionStorage.set("online", online)

    var age = answers[1]
    sessionStorage.set("age", age)

    
    document.getElementById("submit").click()

  }
  
  
//   function displayResults() {
//     console.log(answers)
//     fetch('/get-events') 
//     .then(response => response.json())
//     .then(data => {
//       //data is list of posts
//       //answers is a list of the answers
//       console.log(data);  // Example: Log the data to the console

//     })
//     .catch(error => {
//       console.error('Error:', error);
//     });
//   }
  
  
  function updateSliderValue(value) {
    sliderValueElement.innerText = value; // Update the displayed value of the slider

  }
  function clearAnswerButtons() {
    while (answerButtonsElement.firstChild) {
      answerButtonsElement.removeChild(answerButtonsElement.firstChild);
    }
  }

  startQuiz();
