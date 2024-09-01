// Health Quiz Questions
const Questions = [
  // Physical Health Questions
  {
    q: "What should you eat to keep your bones strong and healthy?",
    a: [
      { text: "Apples", isCorrect: false },
      { text: "Broccoli", isCorrect: true },
      { text: "Ice Cream", isCorrect: false },
      { text: "French Fries", isCorrect: false },
    ],
  },
  {
    q: "How many glasses of water should you drink every day to stay hydrated?",
    a: [
      { text: "1 glass", isCorrect: false },
      { text: "3 glasses", isCorrect: false },
      { text: "8 glasses", isCorrect: true },
      { text: "20 glasses", isCorrect: false },
    ],
  },
  {
    q: "Which activity is good for your heart?",
    a: [
      { text: "Watching TV", isCorrect: false },
      { text: "Running and playing", isCorrect: true },
      { text: "Eating chips", isCorrect: false },
      { text: "Sleeping", isCorrect: false },
    ],
  },
  {
    q: "What food group should you eat the most of for a balanced diet?",
    a: [
      { text: "Candy", isCorrect: false },
      { text: "Fruits and vegetables", isCorrect: true },
      { text: "Pizza", isCorrect: false },
      { text: "Cookies", isCorrect: false },
    ],
  },
  {
    q: "How many hours of sleep should kids get each night for good health?",
    a: [
      { text: "4 hours", isCorrect: false },
      { text: "8-10 hours", isCorrect: true },
      { text: "20 minutes", isCorrect: false },
      { text: "No sleep needed", isCorrect: false },
    ],
  },
];

let currQuestion = 0;
let score = 0;

function loadQues() {
  const question = document.getElementById("ques");
  const opt = document.getElementById("opt");

  question.textContent = Questions[currQuestion].q;
  opt.innerHTML = "";

  for (let i = 0; i < Questions[currQuestion].a.length; i++) {
    const choicesdiv = document.createElement("div");
    const choice = document.createElement("input");
    const choiceLabel = document.createElement("label");

    choice.type = "radio";
    choice.name = "answer";
    choice.value = i;

    choiceLabel.textContent = Questions[currQuestion].a[i].text;

    choicesdiv.appendChild(choice);
    choicesdiv.appendChild(choiceLabel);
    opt.appendChild(choicesdiv);
  }
}

loadQues();

function loadScore() {
  const totalScore = document.getElementById("score");
  totalScore.textContent = `Score: ${score} out of ${Questions.length}`;
}

function nextQuestion() {
  if (currQuestion < Questions.length - 1) {
    currQuestion++;
    loadQues();
  } else {
    document.getElementById("opt").remove();
    document.getElementById("ques").remove();
    document.getElementById("btn").remove();
    loadScore();
  }
}

function checkAns() {
  const selectedAns = parseInt(document.querySelector('input[name="answer"]:checked').value);

  if (Questions[currQuestion].a[selectedAns].isCorrect) {
    score++;
  }
  
  nextQuestion();
}
