from flask import Flask, render_template, request
from genai import call_ai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        resume = request.form["resume"]
        job = request.form["job"]
        prompt = request.form["prompt"]

        result = call_ai(resume, job, prompt)

    return render_template("input.html", result=result)

if __name__ == "__main__":
    app.run()
