from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def greetings():
	return render_template('index.html', name="Mike")

@app.route('/ninjas')
def ninjas():
	return render_template('ninja.html')

@app.route('/dojos/new')
def create():
	return render_template('/dojos.html')

app.run(debug=True)