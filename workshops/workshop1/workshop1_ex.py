import numpy as np


def tax(income):
    """
    Return the taxes owed for a given income.

    Paramteres
    ---------
    income
        gross income

    Returns
    ----
    Tax owed

    """

    # for n in range(incomes):

    taxes = None

    if income < 300000:
        taxes = 0
    elif income <= 700000 and income >= 300000:
        taxes = 0.2 * (income - 300000)
    else:
        taxes = 0.2 * (700000 - 300000) + 0.35 * (income - 700000)

    return taxes


# Create 13 candidate income levels
incomes = np.linspace(0, 1200000, 13)
# taxes_loop = np.empty(len(incomes))
taxes_loop = []


for income in incomes:
    # Compute taxes for current income level
    taxes = tax(income)
    taxes_loop.append(taxes)
    net_income = income - taxes
    print(
        f'Gross income: {income:10.0f}; Taxes; {taxes:10.0f}; Net income {net_income:10.0f}'
    )

def tax_numpy():
        taxes = tax(income)
        

