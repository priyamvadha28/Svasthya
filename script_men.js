// Health Quiz Questions
const Questions = [
    // Mental Health Questions
    {
      q: "What should you do if you're feeling sad?",
      a: [
        { text: "Talk to a friend or family member", isCorrect: true },
        { text: "Keep your feelings to yourself", isCorrect: false },
        { text: "Eat lots of chocolate", isCorrect: false },
        { text: "Watch a sad movie", isCorrect: false },
      ],
    },
    {
      q: "What can you practice to help you relax and feel calm?",
      a: [
        { text: "Deep breathing", isCorrect: true },
        { text: "Eating fast food", isCorrect: false },
        { text: "Jumping on the bed", isCorrect: false },
        { text: "Playing video games", isCorrect: false },
      ],
    },
    {
      q: "What should you do if you're stressed about a test?",
      a: [
        { text: "Study for hours without breaks", isCorrect: false },
        { text: "Ask for help from a teacher or parent", isCorrect: true },
        { text: "Panic and give up", isCorrect: false },
        { text: "Play video games", isCorrect: false },
      ],
    },
    {
      q: "What is a simple way to make yourself feel happy?",
      a: [
        { text: "Watch a comedy show", isCorrect: true },
        { text: "Frown all day", isCorrect: false },
        { text: "Stay in a dark room", isCorrect: false },
        { text: "Eat only vegetables", isCorrect: false },
      ],
    },
    {
      q: "What's a healthy way to express your feelings?",
      a: [
        { text: "Yell at everyone", isCorrect: false },
        { text: "Write in a diary or talk to someone you trust", isCorrect: true },
        { text: "Keep your feelings inside", isCorrect: false },
        { text: "Sing loudly in public", isCorrect: false },
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
  