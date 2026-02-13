'''
Python Syntax: Medical Insurance Project

Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs.
Using a formula that estimates a person's yearly insurance costs, you will investigate how different factors 
such as age, sex, BMI, etc. affect the prediction.
We are using this medical insurance dataset as a guide: https://www.kaggle.com/datasets/mirichoi0218/insurance

In this code, we estimate the medical insurance costs for individuals based on five variables:
age: age of the individual in years
sex: 0 for female, 1 for male
bmi: individual's body mass index
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual's insurance cost (in USD):
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
'''

# Create the variables for each factor we will consider when estimating medical insurance costs.
# The following is for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2
age = 28 
sex = 0 
bmi = 26.2 
num_of_children = 3 
smoker = 0 

# Insurance estimate formula:
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Use string concatenation to print the value in an informative way
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# This person's insurance cost is 5469.0 dollars.

# We have seen how our formula can estimate costs for one individual. 
# Now let's play with some individual factors to see what role each one plays in our estimation!

#---------------------AGE FACTOR---------------------
# Add 4 years to our age variable
age += 4
# Recalculate insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Find the difference between our new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Use string concatenation to print the value in an informative way
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")
# The change in cost of insurance after increasing the age by 4 years is 1000.0 dollars.

# Reset age to evaluate each factor seperately
age = 28


#---------------------BMI FACTOR---------------------
# Add 3.1 to our bmi variable
bmi += 3.1
# Recalculate insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Find the difference between our new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Use string concatenation to print the value in an informative way
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")
# The change in estimated insurance cost after increasing BMI by 3.1 is 1147.0 dollars.

# Reset bmi to evaluate each factor seperately
bmi = 26.2


#---------------------SEX FACTOR---------------------
# Reassign the value of sex to 1, representing a male
sex = 1
# Recalculate insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Find the difference between our new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Use string concatenation to print the value in an informative way
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")
# The change in estimated cost for being male instead of female is -128.0 dollars.

# Reset sex to evaluate each factor seperately
sex = 0


#---------------------SMOKING FACTOR---------------------
# Reassign the value of smoker to 1, representing a smoker
smoker = 1
# Recalculate insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Find the difference between our new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Use string concatenation to print the value in an informative way
print("The change in estimated cost for being a smoker is " + str(change_in_insurance_cost) + " dollars.")
# The change in estimated cost for being a smoker is 24000.0 dollars.

# Reset smoker to evaluate each factor seperately
smoker = 0


#---------------------CHILDREN FACTOR---------------------
# Reassign the value of num_of_children to 1, representing one child
num_of_children = 1
# Recalculate insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Find the difference between our new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Use string concatenation to print the value in an informative way
print("The change in estimated cost for having one child instead of 3 is " + str(change_in_insurance_cost) + " dollars.")
# The change in estimated cost for having one child instead of 3 is -850.0 dollars.

# Reset children to evaluate each factor seperately
num_of_children = 0


#---------------------CONCLUSION---------------------
# The estimated insurance cost on average increases as you age, and as your bmi increases, and it balloons if you smoke.
# On the contrary your insurance costs on average decrease if you're a male and if you have fewer children.