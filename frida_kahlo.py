'''
Congratulations! You've been hired to work on a retrospective of Frida Kahlo's work at a major museum in Mexico.

Your job is to put together the audio tour, but in order to do that, you need to create a list of each painting 
featured in the exhibit, the date it was painted, and its spot on the tour.

Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID.
'''

# List of paintings in the museum
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# List of dates associated with the paintings above
dates = [1939, 1933, 1946, 1940]

# It doesn't do much good to have the paintings without their dates, and vice versa
# Pair the paintings with their dates and save to the original paintings list
paintings = list(zip(paintings, dates))
# Print the results
print(paintings)
# [('The Two Fridas', 1939), ('My Dress Hangs Here', 1933), ('Tree of Hope', 1946), ('Self Portrait With Monkeys', 1940)]

# There were some last minute additions to the show that we need to add to our list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
# Print the updated list
print(paintings)
# [('The Two Fridas', 1939), ('My Dress Hangs Here', 1933), ('Tree of Hope', 1946), ('Self Portrait With Monkeys', 1940),
# ('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)]

# Since each of these paintings is going to be in the audio tour, they each need a unique identification number. But before 
# we assign them a number, we first need to check how many paintings there are in total
print(len(paintings))
# 7

# Generate a list of identification numbers that starts at 1 and is equal in length to our list of items. Save it to the 
# audio tour number list
audio_tour_number = list(range(1,len(paintings)+1))
# Print the audio tour number list
print(audio_tour_number)
# [1, 2, 3, 4, 5, 6, 7]

# We're finally ready to create our master list. Zip the audio tour number list to the paintings list and save as a master list
master_list = list(zip(audio_tour_number, paintings))
# Print the master list
print(master_list)
# [(1, ('The Two Fridas', 1939)), (2, ('My Dress Hangs Here', 1933)), (3, ('Tree of Hope', 1946)),
#  (4, ('Self Portrait With Monkeys', 1940)), (5, ('The Broken Column', 1944)), (6, ('The Wounded Deer', 1946)), 
# (7, ('Me and My Doll', 1937))]