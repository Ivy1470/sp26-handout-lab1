"""
This question has two parts:

Part 1: Please implement these stub functions to match the documentation.
It will be useful to use a dict to store the "threshold" for each tax bracket, 
and use an appropriate control structure to go over it and find the right tax bracket.

Part 2: The California, New York, and Federal tax functions should have code in common.
Factor it out into a helper function, so that the code is not repeated, but the functionality
remains the same.

As always, make sure to implement tests in the tests directory.
"""

# Relevant information:
# Federal income tax rates:  https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
# California income tax rates: https://www.hrblock.com/tax-center/filing/states/california-tax-rates
# Massachusetts income tax rate: 5% for everyone
# New York state income tax rates: https://www.nerdwallet.com/article/taxes/new-york-state-tax
def calculate_progressive_tax(income: int, brackets: list) -> float:   # type: ignore
    """Helper function to calculate tax based on progressive tax brackets
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    brackets : list
        List of tuples (threshold, rate) representing tax brackets
        
    Returns
    -------
    float
        The total tax amount
    """
    tax = 0.0
    previous_threshold = 0
    
    for threshold, rate in brackets:
        if income > threshold:
            taxable_amount = threshold - previous_threshold
            tax += taxable_amount * rate
            previous_threshold = threshold
        else:
            taxable_amount = income - previous_threshold
            tax += taxable_amount * rate
            return tax
    
    taxable_amount = income - previous_threshold
    tax += taxable_amount * brackets[-1][1]
    
    return tax


def income_tax_fed(income: int) -> float:
    """Calculates the amount of federal income tax paid by somebody in the United States
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    
    Returns
    -------
    float
        The amount of federal income tax they pay
    """
    fed_brackets = [
        (11000, 0.10),
        (44725, 0.12),
        (95375, 0.22),
        (182100, 0.24),
        (231250, 0.32),
        (578125, 0.35),
        (float('inf'), 0.37)
    ]
    
    return calculate_progressive_tax(income, fed_brackets)

def income_tax_ca(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in California
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of CA state tax they pay if they live in California
    """
    ca_brackets = [
        (10412, 0.01),
        (24684, 0.02),
        (38959, 0.04),
        (54081, 0.06),
        (68350, 0.08),
        (349137, 0.093),
        (418961, 0.103),
        (698271, 0.113),
        (float('inf'), 0.123)]
    
    return calculate_progressive_tax(income, ca_brackets)

def income_tax_ma(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in Massachusetts
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in Masachusetts
    """
    return income * 0.05

def income_tax_ny(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in New York state
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in New York state
    """
    ny_brackets = [
        (8500, 0.04),
        (11700, 0.045),
        (13900, 0.0525),
        (80650, 0.055),
        (215400, 0.06),
        (1077550, 0.0685),
        (5000000, 0.0965),
        (25000000, 0.103),
        (float('inf'), 0.109)]
    
    return calculate_progressive_tax(income, ny_brackets)

def calculate_income_tax() -> None:
    """
    1. Ask the user to input their state (CA for California, MA for Massachusetts, NY for New York)
    2. Ask the user to input an annual income
    3. Print a sentence formatted like this: "Your income is XX before tax and XX after tax. You pay XX income tax."
    4. Handle invalid unit inputs gracefully with the error message "Invalid state. Please enter CA, MA, or NY."
    """
    state = input("Enter your state (CA, MA, or NY): ").strip().upper()
    
    if state not in ['CA', 'MA', 'NY']:
        print("Invalid state. Please enter CA, MA, or NY.")
        return
    
    income = int(input("Enter your annual income: "))
    
    if state == 'CA':
        state_tax = income_tax_ca(income)
    elif state == 'MA':
        state_tax = income_tax_ma(income)
    else:
        state_tax = income_tax_ny(income)
    
    fed_tax = income_tax_fed(income)
    
    total_tax = state_tax + fed_tax
    after_tax_income = income - total_tax
    
    print(f"Your income is {income} before tax and {after_tax_income:.2f} after tax. You pay {total_tax:.2f} income tax.")


if __name__ == "__main__":
    calculate_income_tax()