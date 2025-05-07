const textSamples = [
  "The quick brown fox jumps over the lazy dog.",
  "Python is a powerful and versatile programming language.",
  "Typing fast and accurately takes practice and focus.",
  "JavaScript adds interactivity to your websites.",
  "Frontend development is fun with HTML, CSS, and JS."
];

let originalText = "";
let startTime;
let interval;
let testFinished = false;

function startTest() {
  originalText = textSamples[Math.floor(Math.random() * textSamples.length)];
  document.getElementById("text-to-type").textContent = originalText;

  const inputBox = document.getElementById("input");
  inputBox.value = "";
  inputBox.disabled = false;
  inputBox.focus();

  testFinished = false;
  startTime = new Date().getTime();
  interval = setInterval(updateStats, 100);

  inputBox.addEventListener('input', checkCompletion);  // 👈 live check
}
function checkCompletion() {
  const typed = document.getElementById("input").value;

  if (typed.trim() === originalText.trim()) {
    finishTest();
  }
}
function updateStats() {
  if (testFinished) return;

  const currentTime = new Date().getTime();
  const elapsed = (currentTime - startTime) / 1000;

  const typed = document.getElementById("input").value;
  const wordCount = typed.trim().split(/\s+/).length;

  const wpm = Math.round((wordCount / elapsed) * 60);
  const accuracy = calculateAccuracy(typed, originalText);

  document.getElementById("speed").textContent = isNaN(wpm) ? 0 : wpm;
  document.getElementById("accuracy").textContent = accuracy;
  document.getElementById("time").textContent = Math.floor(elapsed);
}
