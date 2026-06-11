let csvData = [];
let currentQuestion = 0;
let shuffledChoices = [];
let correctAnswerIndex = -1;
let answerClicked = false;
let timerInterval = null;
let timeLeft = 30;

const uploadScreen = document.getElementById('upload-screen');
const gameScreen = document.getElementById('game-screen');
const csvUpload = document.getElementById('csv-upload');
const scenarioEl = document.getElementById('scenario');
const questionEl = document.getElementById('question');
const timerEl = document.getElementById('timer');
const topHalf = document.getElementById('top-half');
const nextBtn = document.getElementById('next-btn');
const answerBoxes = document.querySelectorAll('.answer-box');

// Handle CSV file upload
csvUpload.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            parseCSV(event.target.result);
        };
        reader.readAsText(file);
    }
});

// Parse CSV data with proper quote handling
function parseCSV(text) {
    const lines = text.trim().split('\n');
    csvData = [];

    for (let i = 1; i < lines.length; i++) {
        const values = parseCSVLine(lines[i]);
        if (values.length >= 6) {
            csvData.push({
                scenario: values[0].trim(),
                question: values[1].trim(),
                choices: [
                    values[2].trim(),
                    values[3].trim(),
                    values[4].trim(),
                    values[5].trim()
                ],
                correctAnswer: values[2].trim()
            });
        }
    }

    if (csvData.length > 0) {
        csvData = shuffleArray(csvData);
        uploadScreen.style.display = 'none';
        gameScreen.style.display = 'flex';
        loadQuestion();
    }
}

// Parse a single CSV line handling quoted fields
function parseCSVLine(line) {
    const values = [];
    let current = '';
    let inQuotes = false;

    for (let i = 0; i < line.length; i++) {
        const char = line[i];
        const nextChar = line[i + 1];

        if (char === '"') {
            if (inQuotes && nextChar === '"') {
                current += '"';
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (char === ',' && !inQuotes) {
            values.push(current);
            current = '';
        } else {
            current += char;
        }
    }

    values.push(current);
    return values;
}

// Shuffle array
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

// Start timer
function startTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
    }

    timeLeft = 30;
    timerEl.textContent = timeLeft;

    timerInterval = setInterval(() => {
        timeLeft--;
        timerEl.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            if (!answerClicked) {
                answerClicked = true;
                topHalf.classList.add('incorrect');
                answerBoxes[correctAnswerIndex].classList.add('correct');
                nextBtn.style.display = 'block';
            }
        }
    }, 1000);
}

// Load question
function loadQuestion() {
    if (currentQuestion >= csvData.length) {
        currentQuestion = 0;
    }

    const current = csvData[currentQuestion];
    scenarioEl.textContent = current.scenario;
    questionEl.textContent = current.question;

    const choicesWithCorrect = current.choices.map((choice, index) => ({
        text: choice,
        isCorrect: index === 0
    }));

    shuffledChoices = shuffleArray(choicesWithCorrect);
    correctAnswerIndex = shuffledChoices.findIndex(choice => choice.isCorrect);

    answerBoxes.forEach((box, index) => {
        const answerText = box.querySelector('.answer-text');
        answerText.textContent = shuffledChoices[index].text;
        box.classList.remove('correct', 'incorrect');
    });

    topHalf.classList.remove('correct', 'incorrect');
    nextBtn.style.display = 'none';
    answerClicked = false;
    startTimer();
}

// Handle answer click
answerBoxes.forEach((box, index) => {
    box.addEventListener('click', () => {
        if (answerClicked) return;
        answerClicked = true;

        if (timerInterval) {
            clearInterval(timerInterval);
        }

        if (index === correctAnswerIndex) {
            box.classList.add('correct');
            topHalf.classList.add('correct');
        } else {
            box.classList.add('incorrect');
            answerBoxes[correctAnswerIndex].classList.add('correct');
            topHalf.classList.add('incorrect');
        }

        nextBtn.style.display = 'block';
    });
});

// Handle next button click
nextBtn.addEventListener('click', () => {
    currentQuestion++;
    loadQuestion();
});