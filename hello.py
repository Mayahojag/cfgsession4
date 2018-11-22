from flask import Flask, render_template, request
import requests
app = Flask("MyApp")

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0572c993e99241bfa6dd09d852fca104.mailgun.org/messages",
        auth=("api", "fe405937c852cd354b63f957cd8bd6d9-4412457b-b64f1c96"),
        data={"from": "Excited User <mailgun@sandbox0572c993e99241bfa6dd09d852fca104.mailgun.org>",
              "to": ["email"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


@app.route("/")
def hello():
	return "Hello World"

@app.route("/<name>")
def hello_someone(name):
		return render_template("hello.html", name=name.title())

app.run(debug=True)

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	email = form_data ["email"]
	send_simple_message(email)
	return "Email sent to: {}".format(email)