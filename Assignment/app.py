import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')


def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        print(e)
        return "Sorry, there was an error with the API. Please try again later."


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = f"User: {request.form['question']}\nChatGPT: "
        message = generate_response(prompt)
        return render_template("results.html", question=request.form['question'], message=message)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
