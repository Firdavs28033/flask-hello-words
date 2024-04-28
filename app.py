from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
	username = 'Firdavs'
	title = 'Portfolio'
	return render_template('index.html', title=title, username=username)

@app.route('/admin')
def admin():
	return redirect(url_for('home'))




if __name__ == "__main__":
	app.run()
