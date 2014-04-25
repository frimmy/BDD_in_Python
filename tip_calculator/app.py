from flask import Flask, render_template, redirect, url_for,request, flash
from forms import CalculatorForm

app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'abc123'

@app.route('/', methods=['GET','POST'])
def home():
	form = CalculatorForm()

	return render_template('home.html', form=form)	


@app.route('/results', methods=['GET','POST'])
def results():

	form = CalculatorForm()
	mealdata = None

	if request.method == 'POST' and form.validate_on_submit():

		mealdata = dict(meal_cost=form.meal_cost.data, tip_percentage=form.tip_percentage.data, tip='')
		
		flash('submitted tip calculator fields Meal Cost= "' + str(mealdata['meal_cost']) + '" Tip Percentage= "' + str(mealdata['tip_percentage']) +'%"')
			
		mealdata['tip'] = calculate_tip(mealdata['meal_cost'],mealdata['tip_percentage'])
		
		return render_template('results.html', form=form, mealdata=mealdata)


	return render_template('home.html', form=form)	

def calculate_tip(base_cost, tip_percentage):

	tip = float(base_cost) * float(tip_percentage)/100
	return '{:.2f}'.format(tip)

if __name__ == '__main__':
	app.run(debug=True)