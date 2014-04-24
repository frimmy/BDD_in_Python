from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import validators #InputRequired, NumberRange, Required
from wtforms.fields import DecimalField
class CalculatorForm(Form):

	meal_cost = DecimalField('meal_cost', validators=[validators.InputRequired("This field is required"), validators.NumberRange(min=0)], places=2) 
	tip_percentage = DecimalField('tip_percentage', validators=[validators.InputRequired("This field is required"), validators.NumberRange(min=0, max=100)], places=2)

	
