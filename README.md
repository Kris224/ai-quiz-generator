## 🧠 AI Quiz Generator from Text using Gemini

A Flask web application that automatically generates quiz questions from any input text using Google's Gemini 2.0 Flash model. Users can select the number of questions, difficulty level, and question type (MCQ, True/False, Fill-in-the-Blank). After attempting the quiz, the user receives a score instantly.

---

### 📸 Preview

![Screenshot 2025-06-12 170126](https://github.com/user-attachments/assets/9a5b33b5-0251-42d2-96e8-2ed158ce5243)
![Screenshot 2025-06-12 170140](https://github.com/user-attachments/assets/5d4c6b39-f12e-47bb-8195-dd4b3f80cebb)
![Screenshot 2025-06-12 170256](https://github.com/user-attachments/assets/65d7d3f1-6a8f-4c73-bb69-43fa31b2f799)

## 🚀 Features

* ✅ Paste any text and generate a quiz
* ✅ Choose question type, difficulty, and count
* ✅ Gemini 2.0 Flash used for fast question generation
* ✅ Quiz supports MCQ, True/False, Fill-in-the-Blanks
* ✅ Score calculated after submission
* ✅ Clean, simple interface with Flask + HTML

---

## 🧰 Tech Stack

| Tech                 | Purpose                 |
| -------------------- | ----------------------- |
| Python               | Backend logic           |
| Flask                | Web framework           |
| Gemini 2.0 Flash API | AI question generation  |
| HTML (Jinja2)        | Frontend templates      |
| Dotenv               | Secure API key handling |

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kris224/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2. Create `.env` File

```bash
touch .env
```

Inside `.env`, add your API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

> 💡 Don't share your `.env` file — it's in `.gitignore`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## 📦 Project Structure

```
ai-quiz-generator/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── templates/
    ├── index.html
    ├── quiz.html
    └── result.html
```

---

## 📌 Example Prompt

Input Text:

```
Photosynthesis is the process by which plants convert sunlight into energy. They use carbon dioxide and water, releasing oxygen as a byproduct.
```

Settings:

* 3 Questions
* Medium
* MCQ

Gemini Output (Example):

```json
[
  {
    "question": "What gas is released during photosynthesis?",
    "type": "MCQ",
    "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
    "answer": "Oxygen"
  },
  ...
]
```

---

## 🧠 Future Improvements

* Export quiz to PDF or text
* Upload PDF/Text files for input
* User login + quiz history
* Deploy to Render/Railway

---
