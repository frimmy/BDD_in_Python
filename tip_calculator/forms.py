from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import InputRequired, NumberRange, Required

class CalculatorForm(Form):

	meal_cost = DecimalField('meal_cost', validators=[Required()]) #NumberRange(min=0, max=None, message="Must be positive amount") ,InputRequired('This field must be filled with a decimal number.'), 
	tip_percentage = DecimalField('tip_percentage',validators=[Required()]) #NumberRange(min=0, max=100, message="Must be a valid percentage"), InputRequired('This field must be filled with a decimal number.'), 

	#
