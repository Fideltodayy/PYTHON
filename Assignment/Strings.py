# Step 1: Initialize three strings called title, nature, and schedules
title = "CMT 400 Research Project"
nature = "Finance,The Research Project is meant to offer financial literacy"
schedules = "To be delivered in 1 semester"
print(title,nature,schedules)
# Step 2: Using slicing syntax
# i. Extract and display the unit code from title
unit_code = title[:7]
print("Unit Code:", unit_code)

# ii. Extract and display the subtitle "Nature of the Unit" from nature
# start_index = nature.index("Finance")
# end_index = nature.index("The Research Project is meant to offer financial literacy")  # Assuming this is where it ends
# subtitle = nature[start_index:end_index]
# print("Subtitle:", subtitle)
subtitle = nature.split(",")
print(subtitle[0])

# iii. Convert the string called schedules to upper case
schedules_upper = schedules.upper()
print("Schedules (Upper Case):", schedules_upper)

# iv. Convert the title to a list and use a for loop to display items in the new list.
title_list = list(title)
print("Title as a list:", title_list)
print("Displaying items in the list:")
for item in title_list:
    print(item)

# Step 3: Determine the number of times the word “project” appears in the schedule string.
project_count = schedules.lower().count("project")
print("Number of times 'project' appears in schedules:", project_count)

#this can still be optimised.I will revisit