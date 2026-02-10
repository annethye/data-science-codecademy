'''
Working with Python Lists: Medical Insurance Costs Project

You are a doctor sorting through medical insurance cost data for some patients.

Using your knowledge of Python lists, you will store medical data and see what valuable insights you can gain from that data.
'''

# Names of ten individuals
names = ['Mohamed', 'Sara', 'Xia', 'Paul', 'Valentina', 'Jide', 'Aaron', 'Emily', 'Nikita', 'Paul']
# Associated medical insurance costs
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Append Priscilla and her insurance cost
names.append('Priscilla')
insurance_costs.append(8320.0)

# Combine the individuals and their costs
medical_records = list(zip(insurance_costs, names))
print(medical_records)
# [(13262.0, 'Mohamed'), (4816.0, 'Sara'), (6839.0, 'Xia'), (5054.0, 'Paul'), (14724.0, 'Valentina'), (5360.0, 'Jide'), 
# (7640.0, 'Aaron'), (6072.0, 'Emily'), (2750.0, 'Nikita'), (12064.0, 'Paul'), (8320.0, 'Priscilla')]

# Calculate the number of medical records we're dealing with
num_medical_records = len(medical_records)
print(f'There are {num_medical_records} medical records.')
# There are 11 medical records.

# Select the first medical record
first_medical_record = medical_records[0]
print(f'Here is the first medical record: {first_medical_record}')
# Here is the first medical record: (13262.0, 'Mohamed')

# Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list
medical_records.sort()
print(f'Here are the medical records sorted by insurance cost: {medical_records}')
# Here are the medical records sorted by insurance cost: [(2750.0, 'Nikita'), (4816.0, 'Sara'), (5054.0, 'Paul'), (5360.0, 'Jide'),
# (6072.0, 'Emily'), (6839.0, 'Xia'), (7640.0, 'Aaron'), (8320.0, 'Priscilla'), (12064.0, 'Paul'), (13262.0, 'Mohamed'), (14724.0, 'Valentina')]

# Let's look at the three cheapest insurance costs in our medical records.
cheapest_three = medical_records[:3]
print(f'Here are the three cheapest insurance costs in our medical records: {cheapest_three}')
# Here are the three cheapest insurance costs in our medical records: [(2750.0, 'Nikita'), (4816.0, 'Sara'), (5054.0, 'Paul')]

# Let's look at the three most expensive insurance costs in our medical records.
priciest_three = medical_records[-3:]
print(f'Here are the three most expensive insurance costs in our medical records: {priciest_three}')
# Here are the three most expensive insurance costs in our medical records: [(12064.0, 'Paul'), (13262.0, 'Mohamed'), (14724.0, 'Valentina')]

# Some individuals in our medical records have the same name. Count the number of occurrences of 'Paul' in the names list
occurrences_paul = names.count('Paul') 
print(f'There are {occurrences_paul} individuals with the name Paul in our medical records.')
# There are 2 individuals with the name Paul in our medical records.

# Select the middle 5 records
middle_five_records = medical_records[3:8]
print(f'The middle five records are: {middle_five_records}')
# The middle five records are: [(5360.0, 'Jide'), (6072.0, 'Emily'), (6839.0, 'Xia'), (7640.0, 'Aaron'), (8320.0, 'Priscilla')]

# Sort the medical records alphabetically by name. 
medical_records_alphabetically = sorted(medical_records, key=lambda x: x[1])
print(f'Here are the medical records sorted by name: {medical_records_alphabetically}')
# Here are the medical records sorted by name: [(7640.0, 'Aaron'), (6072.0, 'Emily'), (5360.0, 'Jide'), (13262.0, 'Mohamed'), (2750.0, 'Nikita'),
# (5054.0, 'Paul'), (12064.0, 'Paul'), (8320.0, 'Priscilla'), (4816.0, 'Sara'), (14724.0, 'Valentina'), (6839.0, 'Xia')]