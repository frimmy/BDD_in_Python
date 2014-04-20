from flask import Flask, render_template, redirect, url_for,request
from forms import CalculatorForm

app = Flask(__name__)

@app.route('/')
def home():
	form = CalculatorForm()
	if request.method == 'POST' and form.validate():
		return redirect(url_for('results'))
	return render_template('home.html', form = form)

@app.route('/results', methods=['POST'])
def results():
	return render_template('results.html')

if __name__ == '__main__':
	app.run(debug=True)