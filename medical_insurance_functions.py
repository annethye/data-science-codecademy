'''
Python Functions: Medical Insurance Project

You are curious about how certain factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

In this code, we estimate the medical insurance costs for two individuals, Maria and Omar, based on five variables:

age: age of the individual in years
sex: 0 for female, 1 for male
bmi: individual's body mass index
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual's insurance cost (in USD):

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
'''

# Maria variables
age, sex, bmi, num_of_children, smoker = 28, 0, 26.2, 3, 0
# Estimate Maria's insurance cost
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(f'The estimated insurance cost for Maria is {insurance_cost} dollars.')
# The estimated insurance cost for Maria is 5469.0 dollars.

# Omar variables
age, sex, bmi, num_of_children, smoker = 35, 1, 22.2, 0, 1
# Estimate Maria's insurance cost
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(f'The estimated insurance cost for Omar is {insurance_cost} dollars.')
# The estimated insurance cost for Omar is 28336.0 dollars.


# The code used to estimate insurance costs for Maria and Omar looks quite similar – in both cases we 
# calculate the insurance cost using the same formula and then print the output. This code is a great 
# candidate for a function because it involves repeating almost identical commands in multiple places.

# Define the function and take inputs for the name and each of the values needed in the insurance formula.
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  # Use the estimated insurance formula
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  # Print statement
  print(f'The estimated insurance cost for {name} is {estimated_cost} dollars.')
  # Return estimated cost
  return estimated_cost

maria_insurance_cost = calculate_insurance_cost(name = 'Maria', age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
# The estimated insurance cost for Maria is 5469.0 dollars.
print(maria_insurance_cost)
# 5469.0

omar_insurance_cost = calculate_insurance_cost(name = 'Omar', age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
# The estimated insurance cost for Omar is 28336.0 dollars.
print(omar_insurance_cost)
# 28336.0