@when(u'I go to the tip calculator')
def step_impl(context):
	context.browser.get('http://localhost:5000')

@then(u'I should see the calculator form')
def step_impl(context):
	assert "Tip calculator" in context.browser.title

@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("30")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("20")
	tip_percentage.submit()

@then('I should see the results page')
def step_impl(context):
	br = context.browser
	assert br.find_element_by_id('results')

@then('see the valid total and tip percentage on the results page')
def step_impl(context):
	br = context.browser
	results = br.find_element_by_id('results')
	for i in ["meal-cost", "tip-percentage", "tip-result"]:
		assert br.find_element_by_id(i)
		

@then('see the valid tip on the results page')
def step_impl(context):
	br = context.browser.find_element_by_id('tip-result')
	p = br.text
	assert "$6.00" in p

@when('I submit the form with a negative total/tip percentage')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("-30")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("-20")
	br.find_element_by_id("submit").click()

@then('I should see range errors displayed')
def step_impl(context):
	br = context.browser
	
	errs = br.find_elements_by_class_name("field-error")

	for i in errs:
		assert "Number must be " in i.text
	


@when('I submit the form with a tip percentage over 100%')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("30")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("101")
	br.find_element_by_id("submit").click()