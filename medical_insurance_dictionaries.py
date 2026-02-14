'''
Python Dictionaries: Medical Insurance Project

You have been asked to create a program that organizes and updates medical records efficiently.

In this project, you will use your new knowledge of Python dictionaries to create a database of medical records for patients.
'''

# Dictionary to keep a record of patients and their insurance costs
medical_costs = {}

# Let's add some key value pairs
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

# Using one line of code, add three patients 
medical_costs.update({'Connie': 8886.0, 'Isaac': 16444, 'Valentina': 6420})
print(medical_costs)
# {'Marina': 6607.0, 'Vinay': 3225.0, 'Connie': 8886.0, 'Isaac': 16444, 'Valentina': 6420}

# Vinay's insurance cost is actually 3325.0, update the dictionary
medical_costs['Vinay'] = 3325.0
print(medical_costs)
# {'Marina': 6607.0, 'Vinay': 3325.0, 'Connie': 8886.0, 'Isaac': 16444, 'Valentina': 6420}

# Let's calculate the average medical cost of each patient
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
average_cost = total_cost / len(medical_costs)
print(f'Average Insurance Cost: {average_cost}')
# Average Insurance Cost: 8336.4

# Create a second dictionary that maps patient names to their ages.
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35 , 52]

zipped_ages = zip(names, ages)
names_to_ages = {name: age for name, age in zipped_ages}
print(names_to_ages)
# {'Marina': 27, 'Vinay': 24, 'Connie': 43, 'Isaac': 35, 'Valentina': 52}

marina_age = names_to_ages.get('Marina', None)
print(f'Marina\'s age is {marina_age}')
# Marina's age is 27

medical_records = {}
# Add patient name as a key and a medical data dictionary as a value
medical_records['Marina'] = {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-smoker', 'Insurance_cost': 6607.0}
medical_records['Vinay'] = {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance_cost': 3225.0}
medical_records['Connie'] = {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}
medical_records['Isaac'] = {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}
medical_records['Valentina'] = {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}
print(medical_records)
# {'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-smoker', 'Insurance_cost': 6607.0}, 
# 'Vinay': {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance_cost': 3225.0}, 
# 'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}, 
# 'Isaac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}, 
# 'Valentina': {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}}

# The medical_records dictionary acts like a database of medical records. Let's access a specific piece of data in medical_records.
# Print out Connie's insurance cost 
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")
# Connie's insurance cost is 8886.0 dollars.

# Vinay has moved to a new country and we no longer want to include him in our medical records.
medical_records.pop('Vinay')

# Let's take a closer look at each patient's medical record.
for name, record in medical_records.items():
  print(
    f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']}"
    f" with {record['Children']} children and insurance cost of {record['Insurance_cost']}"
    )
# Marina is a 27 year old Female Non-smoker with a BMI of 31.1 with 2 children and insurance cost of 6607.0
# Connie is a 43 year old Female Non-smoker with a BMI of 25.3 with 3 children and insurance cost of 8886.0
# Isaac is a 35 year old Male Smoker with a BMI of 20.6 with 4 children and insurance cost of 16444.0
# Valentina is a 52 year old Female Non-smoker with a BMI of 18.7 with 1 children and insurance cost of 6420.0

# Function to update the medical_records dictionary with new patients.
def update_medical_records(name, age, sex, bmi, children, smoker, insurance_cost): 
  medical_records[name] = {'Age': age, 'Sex': sex, 'BMI': bmi, 'Children': children, 'Smoker': smoker, 'Insurance_cost': insurance_cost}

# Let's add a new patient to the dictionary
update_medical_records('Laura', 36, 'Female', 21.2, 0, 'Non-smoker', 3100.0)
print(medical_records)
# {'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-smoker', 'Insurance_cost': 6607.0}, 
# 'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}, 
# 'Isaac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}, 
# 'Valentina': {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}, 
# 'Laura': {'Age': 36, 'Sex': 'Female', 'BMI': 21.2, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance_cost': 3100.0}}