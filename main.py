from datetime import datetime

# 1. Sample Income Data
# This data simulates individual income entries with their respective dates.
# In a real scenario, this would come from an accounting system or manual entry.
income_data = [
    {'date': '2023-01-15', 'amount': 1500, 'description': 'Project A - Q1'},
    {'date': '2023-02-20', 'amount': 2000, 'description': 'Project B - Q1'},
    {'date': '2023-03-10', 'amount': 1000, 'description': 'Project C - Q1'},
    {'date': '2023-04-05', 'amount': 2500, 'description': 'Project D - Q2'},
    {'date': '2023-05-18', 'amount': 1800, 'description': 'Project E - Q2'},
    {'date': '2023-06-20', 'amount': 3000, 'description': 'Project F - Q2 (late)'},
    {'date': '2023-07-12', 'amount': 1200, 'description': 'Project G - Q3'},
    {'date': '2023-08-25', 'amount': 2200, 'description': 'Project H - Q3'},
    {'date': '2023-09-15', 'amount': 1700, 'description': 'Project I - Q3 (early)'},
    {'date': '2023-10-08', 'amount': 2800, 'description': 'Project J - Q4'},
    {'date': '2023-11-22', 'amount': 1900, 'description': 'Project K - Q4'},
    {'date': '2023-12-01', 'amount': 3500, 'description': 'Project L - Q4'},
]

# Convert date strings to datetime objects for easier comparison
for item in income_data:
    item['date'] = datetime.strptime(item['date'], '%Y-%m-%d')

# 2. Define Irregular Tax Periods
# These periods are defined with custom, non-standard start and end dates,
# simulating the 'irregular tax periods' mentioned in the article.
tax_periods = {
    'Period 1 (Jan-Mar)': {'start': '2023-01-01', 'end': '2023-03-31'},
    'Period 2 (Apr-Jun)': {'start': '2023-04-01', 'end': '2023-06-25'}, # Irregular end date
    'Period 3 (Jul-Sep)': {'start': '2023-07-01', 'end': '2023-09-20'}, # Irregular end date
    'Period 4 (Oct-Dec)': {'start': '2023-10-01', 'end': '2023-12-31'},
}

# Convert period date strings to datetime objects for comparison
for period_name, dates in tax_periods.items():
    dates['start'] = datetime.strptime(dates['start'], '%Y-%m-%d')
    dates['end'] = datetime.strptime(dates['end'], '%Y-%m-%d')

# 3. Calculate Income per Period (SUMIFS equivalent)
# This section demonstrates how to sum income conditionally based on date ranges,
# mimicking the functionality of a spreadsheet's SUMIFS function.
period_totals = {}
print("--- Income per Irregular Tax Period ---")
for period_name, dates in tax_periods.items():
    current_period_income = 0
    for item in income_data:
        # Check if the income item's date falls within the current tax period
        if dates['start'] <= item['date'] <= dates['end']:
            current_period_income += item['amount']
    period_totals[period_name] = current_period_income
    print(f"{period_name}: ${current_period_income:,.2f}")

# 4. Calculate Year-End Total
total_annual_income = sum(period_totals.values())
print("\n--- Year-End Totals ---")
print(f"Total Annual Income (before special rule): ${total_annual_income:,.2f}")

# 5. Apply the 92.35% Rule
# The article mentions a "92.35% rule" as a special calculation that standard
# summation methods might not cover. For demonstration, we apply this rule
# as a final adjustment to the total annual income. This could represent
# a deductible portion, a specific tax base calculation, or a safe harbor threshold.
SPECIAL_RULE_PERCENTAGE = 0.9235
adjusted_taxable_income = total_annual_income * SPECIAL_RULE_PERCENTAGE

print(f"\nApplying the 92.35% Rule (e.g., for adjusted taxable income):")
print(f"Adjusted Taxable Income: ${adjusted_taxable_income:,.2f} (Total * {SPECIAL_RULE_PERCENTAGE:.2%})")
