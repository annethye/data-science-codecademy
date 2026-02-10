'''
Python Strings: Medical Insurance Project

You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.

In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that it is easier to read and analyse.
'''

# The string stores the medical records for 10 individuals
# Each record is separated by a ; and contains the name, age, BMI  (body mass index), and insurance cost for an individual, in that order.
medical_data = \
'''Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0'''

# We want the insurance costs to be represented in US dollars.
# Replace all instances of # in medical_data with $. 
updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)
# Marina Allison   ,27   ,   31.1 , 
# $7010.0   ;Markus Valdez   ,   30, 
# 22.4,   $4050.0 ;Connie Ballard ,43 
# ,   25.3 , $12060.0 ;Darnell Weber   
# ,   35   , 20.6   , $7500.0;
# Sylvie Charles   ,22, 22.1 
# ,$3022.0   ;   Vinay Padilla,24,   
# 26.9 ,$4620.0 ;Meredith Santiago, 51   , 
# 29.3 ,$16330.0;   Andre Mccarty, 
# 19,22.7 , $2900.0 ; 
# Lorena Hodson ,65, 33.1 , $19370.0; 
# Isaac Vu ,34, 24.8,   $7045.0

# We want to calculate the number of medical records in our data.
num_records = 0
for character in updated_medical_data:
  # We're checking for $ because this is a unique character that shows up exactly once for each individual in the data.
  if character == '$':
    num_records += 1
print(f'There are {num_records} medical records in the data.')
# There are 10 medical records in the data.

# Let's clean up the data so it's easy to work with
# Split the string into a list of each medical record. Remember that each medical record is separated by a ; in the string.
medical_data_split = updated_medical_data.split(';')
print(medical_data_split)
# ['Marina Allison   ,27   ,   31.1 , \n$7010.0   ', 'Markus Valdez   ,   30, \n22.4,   $4050.0 ', 'Connie Ballard ,43 \n,   25.3 , $12060.0 ', 
# 'Darnell Weber   \n,   35   , 20.6   , $7500.0', '\nSylvie Charles   ,22, 22.1 \n,$3022.0   ', '   Vinay Padilla,24,   \n26.9 ,$4620.0 ', 
# 'Meredith Santiago, 51   , \n29.3 ,$16330.0', '   Andre Mccarty, \n19,22.7 , $2900.0 ', ' \nLorena Hodson ,65, 33.1 , $19370.0', 
# ' \nIsaac Vu ,34, 24.8,   $7045.0']

# Our data is now stored in a list, but it is still hard to read. Let's split each medical record into its own list.
medical_records = []
for data in medical_data_split:
  medical_records.append(data.split(','))
print(medical_records)
# [['Marina Allison   ', '27   ', '   31.1 ', ' \n$7010.0   '], ['Markus Valdez   ', '   30', ' \n22.4', '   $4050.0 '], 
# ['Connie Ballard ', '43 \n', '   25.3 ', ' $12060.0 '], ['Darnell Weber   \n', '   35   ', ' 20.6   ', ' $7500.0'], 
# ['\nSylvie Charles   ', '22', ' 22.1 \n', '$3022.0   '], ['   Vinay Padilla', '24', '   \n26.9 ', '$4620.0 '], 
# ['Meredith Santiago', ' 51   ', ' \n29.3 ', '$16330.0'], ['   Andre Mccarty', ' \n19', '22.7 ', ' $2900.0 '], 
# [' \nLorena Hodson ', '65', ' 33.1 ', ' $19370.0'], [' \nIsaac Vu ', '34', ' 24.8', '   $7045.0']]

# Our data is now slightly more readable. However, it is not properly formatted – it contains unnecessary whitespace.
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    # Clean whitespace and append to cleaned record
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)
# [['Marina Allison', '27', '31.1', '$7010.0'], ['Markus Valdez', '30', '22.4', '$4050.0'], ['Connie Ballard', '43', '25.3', '$12060.0'], 
# ['Darnell Weber', '35', '20.6', '$7500.0'], ['Sylvie Charles', '22', '22.1', '$3022.0'], ['Vinay Padilla', '24', '26.9', '$4620.0'], 
# ['Meredith Santiago', '51', '29.3', '$16330.0'], ['Andre Mccarty', '19', '22.7', '$2900.0'], ['Lorena Hodson', '65', '33.1', '$19370.0'], 
# ['Isaac Vu', '34', '24.8', '$7045.0']]

# Our data is now clean and ready for analysis.
# Print out the names of each of the ten individuals:
for record in medical_records_clean:
  # You want all of the names in the medical records to be in uppercase characters.
  record[0] = record[0].upper()
  print(record[0])
# MARINA ALLISON
# MARKUS VALDEZ
# CONNIE BALLARD
# DARNELL WEBER
# SYLVIE CHARLES
# VINAY PADILLA
# MEREDITH SANTIAGO
# ANDRE MCCARTY
# LORENA HODSON
# ISAAC VU

# Let's store each name, age, BMI, and insurance cost in separate lists.
names = []
ages = []
bmis = []
insurance_costs = []

# Iterate through medical_records_clean and append name, age, bmi and insurance cost to the corresponding list
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print(f'Names: {names}')
print(f'Ages: {ages}')
print(f'BMI: {bmis}')
print(f'Insurance Costs: {insurance_costs}')
# Names: ['MARINA ALLISON', 'MARKUS VALDEZ', 'CONNIE BALLARD', 'DARNELL WEBER', 'SYLVIE CHARLES', 'VINAY PADILLA', 'MEREDITH SANTIAGO', 
# 'ANDRE MCCARTY', 'LORENA HODSON', 'ISAAC VU']
# Ages: ['27', '30', '43', '35', '22', '24', '51', '19', '65', '34']
# BMI: ['31.1', '22.4', '25.3', '20.6', '22.1', '26.9', '29.3', '22.7', '33.1', '24.8']
# Insurance Costs: ['$7010.0', '$4050.0', '$12060.0', '$7500.0', '$3022.0', '$4620.0', '$16330.0', '$2900.0', '$19370.0', '$7045.0']

# Now that all of our data is in separate lists, we can easily perform analysis on that data. 
# Let's calculate the average BMI in our dataset.
total_bmi = 0
for bmi in bmis:
  # Add bmi to total, remember to convert to float
  total_bmi += float(bmi)
average_bmi = total_bmi / len(bmis)
print(f'Average BMI: {average_bmi}')
# Average BMI: 25.830000000000002

# Calculate the average insurance cost in insurance_costs. 
total_insurance_cost = 0
for cost in insurance_costs:
  # Add cost to total, remember to convert to float and remove $
  total_insurance_cost += float(cost.strip('$'))
average_insurance_cost = total_insurance_cost / len(insurance_costs)
print(f'Average Insurance Cost: {average_insurance_cost}')
# Average Insurance Cost: 8390.7

# Output a string for each individual:
for name, age, bmi, insurance_cost in zip(names, ages, bmis, insurance_costs):
  # Only add first name in title case
  name = name.split()[0].title()
  print(f'{name} is {age} old with a BMI of {bmi} and an insurance cost of {insurance_cost}.')
# Marina is 27 old with a BMI of 31.1 and an insurance cost of $7010.0.
# Markus is 30 old with a BMI of 22.4 and an insurance cost of $4050.0.
# Connie is 43 old with a BMI of 25.3 and an insurance cost of $12060.0.
# Darnell is 35 old with a BMI of 20.6 and an insurance cost of $7500.0.
# Sylvie is 22 old with a BMI of 22.1 and an insurance cost of $3022.0.
# Vinay is 24 old with a BMI of 26.9 and an insurance cost of $4620.0.
# Meredith is 51 old with a BMI of 29.3 and an insurance cost of $16330.0.
# Andre is 19 old with a BMI of 22.7 and an insurance cost of $2900.0.
# Lorena is 65 old with a BMI of 33.1 and an insurance cost of $19370.0.
# Isaac is 34 old with a BMI of 24.8 and an insurance cost of $7045.0.