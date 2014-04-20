from wtforms import Form, DecimalField
from wtforms.validators import Required

class CalculatorForm(Form):
	meal_cost = DecimalField('meal_cost', validators = [Required()])
	tip_percentage = DecimalField('tip_percentage', validators = [Required()])
