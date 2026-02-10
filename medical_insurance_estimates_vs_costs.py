'''
Python Loops: Medical Insurance Estimates vs. Costs Project

You are interested in analyzing medical insurance cost data efficiently without writing repetitive code.

In this project, you will use your new knowledge of Python loops to iterate through and analyze medical insurance cost data.
'''

# Names of seven individuals
names = ['Judith', 'Abel', 'Tyson', 'Martha', 'Beverley', 'David', 'Anabel']
# Corresponding estimated medical insurance cost
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
# Corresponding actual insurance cost
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Let's calculate the average insurance cost each person paid. 
# Initialise total cost
total_cost = 0
# Loop through actual insurance costs and add the values to the total cost
for value in actual_insurance_costs:
  total_cost += value
# Calculate the average insurance cost each person paid
average_cost = total_cost / len(actual_insurance_costs)
print(f'Average Insurance Cost: {average_cost} dollars.')
# Average Insurance Cost: 4400.0 dollars.

# For each individual, determine whether their insurance cost is above or below average.
# The for loop iterates through the entire list and prints out the insurance cost for each individual.
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print(f'The insurance cost for {name} is {insurance_cost} dollars.')
  # Check whether the insurance cost is above, below or equal to average
  if insurance_cost > average_cost:
    print(f'The insurance cost for {name} is above average.')
  elif insurance_cost < average_cost:
    print(f'The insurance cost for {name} is below average.')
  else:
    print(f'The insurance cost for {name} is equal to the average.')
# The insurance cost for Judith is 1100.0 dollars.
# The insurance cost for Judith is below average.
# The insurance cost for Abel is 2200.0 dollars.
# The insurance cost for Abel is below average.
# The insurance cost for Tyson is 3300.0 dollars.
# The insurance cost for Tyson is below average.
# The insurance cost for Martha is 4400.0 dollars.
# The insurance cost for Martha is equal to the average.
# The insurance cost for Beverley is 5500.0 dollars.
# The insurance cost for Beverley is above average.
# The insurance cost for David is 6600.0 dollars.
# The insurance cost for David is above average.
# The insurance cost for Anabel is 7700.0 dollars.
# The insurance cost for Anabel is above average.

# If you look closely at actual and estimated insurance costs you will notice that each of the actual insurance costs are 10% higher than the estimated insurance costs.
# Using a list comprehension, create a new list with 10% higher estimates.
updated_estimated_costs = [i * 11/10 for i in estimated_insurance_costs]
print(updated_estimated_costs)
# [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]