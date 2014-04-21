from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class CalculatorForm(Form):
	meal_cost = TextField('meal_cost', validators = [Required()])
	tip_percentage = TextField('tip_percentage', validators = [Required()])

	
