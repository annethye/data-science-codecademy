'''
Python Lists: Medical Insurance Estimation Project

In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on five variables:

age: age of the individual in years
sex: 0 for female, 1 for male
bmi: individual's body mass index
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual's insurance cost (in USD):

insurance_cost = 250 ∗ age − 128 ∗ sex + 370 ∗ bmi + 425 ∗ num_of_children + 24000 ∗ smoker − 12500
'''

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print(f'{name}\'s estimated insurance cost: {estimated_cost} dollars.')
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = 'Maria', age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)
# Maria's estimated insurance cost: 4222.0 dollars.

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
'Rohan', age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)
# Rohan's estimated insurance cost: 5442.0 dollars.

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = 'Valentina', age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)
# Valentina's estimated insurance cost: 36368.0 dollars.

# We want to compare the estimated insurance costs (as calculated by our function) to the actual amounts that Maria, Rohan, and Valentina paid.
# List of individuals
names = ['Maria', 'Rohan', 'Valentina']
# Corresponding actual insurance amounts
insurance_costs = [4150.0, 5320.0, 35210.0]

# Currently the names and insurance_costs lists are separate, but we want each name to be paired with an insurance cost.
print(zip(names, insurance_costs))
# <zip object at 0x000001D695A18808>

# This output does not mean much to us. To change it to a format we can actually understand, we must convert the zip object to a list 
insurance_data = list(zip(names, insurance_costs))
print(f'Here is the actual insurance cost data: {insurance_data}')
# Here is the actual insurance cost data: [('Maria', 4150.0), ('Rohan', 5320.0), ('Valentina', 35210.0)]

# Create list to store the estimated insurance costs
estimated_insurance_data = []
# Add our estimated insurance data for Maria, Rohan, and Valentina
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))
print(f'Here is the estimated insurance cost data: {estimated_insurance_data}')
# Here is the estimated insurance cost data: [('Maria', 4222.0), ('Rohan', 5442.0), ('Valentina', 36368.0)]

# You may notice that there are differences between the actual insurance costs and estimated insurance costs. 
# This means that our estimate_insurance_cost() function does not calculate insurance costs with 100% accuracy
insurance_cost_difference = [(names[i], estimated_insurance_data[i][1] - insurance_data[i][1]) for i in range(len(names))]
print(f'Here is the difference between real and estimated insurance cost data: {insurance_cost_difference}')
# Here is the difference between real and estimated insurance cost data: [('Maria', 72.0), ('Rohan', 122.0), ('Valentina', 1158.0)]