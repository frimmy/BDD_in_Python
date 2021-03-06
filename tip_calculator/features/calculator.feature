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

	Scenario: Check that negative amounts are not calculated
		When I go to the tip calculator
		And I submit the form with a negative total/tip percentage
		Then I should see the calculator form 
		And I should see range errors displayed

	Scenario: Check that percentage over 100% are not calculated
		When I go to the tip calculator
		And I submit the form with a tip percentage over 100%
		Then I should see the calculator form
		And I should see range errors displayed
