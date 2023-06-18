from flask import Flask, request, render_template, redirect, session, flash
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"

# a list consisting of a user's responses using session
CURRENT_SURVEY_KEY = 'current_survey'
user_responses = "response"

# print(all_questions)
all_questions = [item.question for item in satisfaction_survey.questions]


#shoing home page
@app.route('/')
def show_home_page():
    return render_template("home.html")


#clears list of user responses from session to begin a new survey
@app.route("/begin", methods=["POST"])
def handle_start():
    session[user_responses] = []
    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_answers():
    #gets user input
    user_input = request.form["answer"]

    #adds user input to the list of answers
    response = session[user_responses]
    response.append(user_input)

    session[user_responses] = response

    if (len(response) >= len(satisfaction_survey.questions)):
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(response)}")


@app.route(f'/questions/0')
def question_0():
    return render_template("question_0.html",
                           satisfaction_survey=satisfaction_survey,
                           all_questions=all_questions)


@app.route('/questions/1')
def question_1():

    response = session[user_responses]
    if len(response) < 1:
        flash('The question you are trying to access is invalid')
        return redirect(f"/questions/{len(response)}")

    elif len(response) > 3:
        return redirect('/complete')

    return render_template("question_1.html",
                           satisfaction_survey=satisfaction_survey,
                           all_questions=all_questions)


@app.route('/questions/2')
def question_2():
    response = session[user_responses]
    if len(response) < 2:
        flash('The question you are trying to access is invalid')
        return redirect(f"/questions/{len(response)}")

    elif len(response) > 3:
        return redirect('/complete')

    return render_template("question_2.html",
                           satisfaction_survey=satisfaction_survey,
                           all_questions=all_questions)


@app.route('/questions/3')
def question_3():
    response = session[user_responses]
    if len(response) < 3:
        flash('The question you are trying to access is invalid')
        return redirect(f"/questions/{len(response)}")

    elif len(response) > 3:
        return redirect('/complete')

    return render_template("question_3.html",
                           satisfaction_survey=satisfaction_survey,
                           all_questions=all_questions)


@app.route("/complete")
def show_complete():
    return render_template("complete.html")
