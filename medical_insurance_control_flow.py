'''
Python Control Flow: Medical Insurance Project

In this project, you will examine how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs.

The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on four variables:

age: age of the individual in years
sex: 0 for female, 1 if male
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual's insurance cost:

insurance_cost = 400 ∗ age − 128 ∗ sex + 425 ∗ num_of_children + 10000 ∗ smoker − 2500
'''

# Function to analyse smoking status. As insurance costs are higher for smokers, it will return advice on how to lower insurance costs.
def analyse_smoker(smoker_status):
  if smoker_status == 1:
    print('To lower your cost, you should consider quitting smoking.')
  else:
    print('Smoking is not an issue for you.')

# Function to analyse BMI. As insurance costs generally increase with BMI, it will return advice on how to lower insurance costs.
def analyse_bmi(bmi_value):
  if bmi_value > 30:
    print('Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.')  
  elif bmi_value < 18.5:
    print('Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.')
  elif bmi_value <= 30 and bmi_value >= 25:
    print('Your BMI is in the overweight range. To lower your cost, you should lower your BMI.')
  else:
    print('Your BMI is in a healthy range.')

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print(f'{name}\'s estimated insurance cost: {estimated_cost} dollars.')
  # Call our analysis functions
  analyse_smoker(smoker)
  analyse_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
# Keanu's estimated insurance cost: 29591.0 dollars.
# To lower your cost, you should consider quitting smoking.
# Your BMI is in the overweight range. To lower your cost, you should lower your BMI.

# Estimate Laura's insurance cost
laura_insurance_cost = estimate_insurance_cost(name = 'Laura', age = 82, sex = 0, bmi = 18, num_of_children = 0, smoker = 0)
# Laura's estimated insurance cost: 14660 dollars.
# Smoking is not an issue for you.
# Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.