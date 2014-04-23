from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import InputRequired, NumberRange, Required

class CalculatorForm(Form):

	meal_cost = DecimalField('meal_cost', [Required()]) #, InputRequired('This field must be filled out.')
	tip_percentage = DecimalField('tip_percentage', [Required()]) # , InputRequired('This field must be filled out.')

	
