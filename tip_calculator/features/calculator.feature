Feature: Confirming that the tip calculator form works

	Scenario: check that the form displays
		When I go to the tip calculator
		Then I should see the calculator form

	Scenario: check that the form submits successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page

	Scenario: Check that results page displays amounts and the tip entered on the form successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page
		And see the valid total and tip percentage on the results page
		And see the valid tip on the results page 

	Scenario: Check that negative percentages are not calculated
		When I go to the tip calculator
		And I submit the form with an invalid total/tip percentage
		Then I should see the calculator form
		And I should be prompted to re-enter the tip percentage