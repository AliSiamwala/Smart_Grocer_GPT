import os
import openai
from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = 'some_secret_key' # replace 'some_secret_key' with your own secret key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    result = None
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        print(response)
        session['result'] = response.choices[0].text.strip() # store result in session
        return redirect(url_for("index"))

    result = session.get('result') # retrieve result from session
    return render_template("index.html", result=result)

def generate_prompt(animal):
    return """You are now David Goggins. I want you to impersonate as him and write resposes to user inputs as if you were David Goggins.
    Be as rough with the language as David Goggins is in real life. Be brutal with the responses and give people what they need to hear
    not what they want to hear. Be as honest as possible. Be as real as possible. Be as raw as possible. Be as authentic as possible.
    {}
    """.format(
        animal.capitalize()
    )

# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
