# Initialize the strings
title = "CMT 400 Research Project"
nature = "Nature of the unit"
schedules = "Schedules in Projects"

# Extract and display the unit code from title
unit_code = title[:7]
print("Unit Code:", unit_code)

# Extract and display the subtitle "Nature of the Unit" from nature
subtitle = nature[14:]
print("Subtitle:", subtitle)

# Convert the string "schedules" to uppercase
schedules_upper = schedules.upper()
print("Uppercase Schedules:", schedules_upper)

# Convert the title to a list and use a for loop to display items in the new list
title_list = list(title)
print("Title List:")
for item in title_list:
    print(item)

# Determine the number of times the word "project" appears in the schedule string
word_to_count = "project"
count = schedules.lower().count(word_to_count)
print("Number of times 'project' appears in schedules:", count)