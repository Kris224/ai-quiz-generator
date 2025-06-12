from flask import Flask, render_template, request
import google.generativeai as genai
import json, random
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Configure your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace with your actual API key

# Function to generate quiz using Gemini
def generate_quiz(text, num_questions, difficulty, q_type):
    prompt = f"""
Generate {num_questions} {q_type} questions from the following content with {difficulty} difficulty.
Return the output as a valid JSON list of objects with the following fields:
"question", "type", "options" (for MCQs), and "answer".

Example:
[
  {{
    "question": "What is ...?",
    "type": "MCQ",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }},
  ...
]

Content:
{text}
"""

    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

    try:
        response = model.generate_content(prompt)
        output = response.text.strip()

        # Clean markdown formatting
        if output.startswith("```"):
            output = output.split("```")[1]  # remove code block
            output = output.replace("json", "").strip()

        quiz = json.loads(output)
        return quiz
    except Exception as e:
        print("🔴 Error:", e)
        return []

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        num = int(request.form["num"])
        difficulty = request.form["difficulty"]
        qtype = request.form["qtype"]

        quiz = generate_quiz(text, num, difficulty, qtype)
        if not quiz:
            return "Error generating quiz. Try again."

        for q in quiz:
            if q["type"].upper() == "MCQ":
                random.shuffle(q["options"])

        return render_template("quiz.html", quiz=quiz, total=len(quiz))

    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    total = int(request.form["total"])

    for i in range(total):
        user_answer = request.form.get(f"q{i}", "").strip().lower()
        correct_answer = request.form.get(f"a{i}", "").strip().lower()
        if user_answer == correct_answer:
            score += 1

    return render_template("result.html", score=score, total=total)

if __name__ == "__main__":
    app.run(debug=True)
