from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import Required

class CalculatorForm(Form):
	
	meal_cost = DecimalField('meal_cost', validators = [Required('This field must be filled with a decimal number.')])
	tip_percentage = DecimalField('tip_percentage', validators = [Required('This field must be filled with a decimal number.')])

	
