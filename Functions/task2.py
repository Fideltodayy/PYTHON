
# Question 1

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data from Table 1
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
rainfall = np.array([515, 521, 653, 659, 617, 574, 739, 534, 603, 628, 502])
maize_output = np.array([32, 37, 46, 46, 42, 39, 52, 40, 40, 44, 28])

# (a) Scatter plot
plt.scatter(rainfall, maize_output)
plt.xlabel('Rainfall (mm)')
plt.ylabel('Maize Output')
plt.title('Annual Precipitation vs. Maize Output')
plt.show()

# (a) Linear regression
slope, intercept, r_value, p_value, std_err = linregress(rainfall, maize_output)
line = slope * rainfall + intercept

# (a) Scatter plot with linear regression line
plt.scatter(rainfall, maize_output)
plt.plot(rainfall, line, color='red')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Maize Output')
plt.title('Annual Precipitation vs. Maize Output with Linear Regression')
plt.show()

# (a) Coefficient of correlation
print("Coefficient of Correlation (r-value):", r_value)

# (b) Explanation
print("We can use the information gathered in Table 1 to predict future results because there is a correlation between annual precipitation and maize output. The positive correlation indicates that as rainfall increases, maize output tends to increase.")

# (c) Prediction using the model
years_to_predict = np.array([2021, 2022])
predicted_output = slope * years_to_predict + intercept
print("Predicted Maize Output for 2021 and 2022:", predicted_output)

# Question 2
# (a) Create and write to king.txt
file_path = 'C:/PyFiles/king.txt'
text_to_write = "A five-day visit to Kenya by Britain’s King Charles III is unearthing memories of atrocities committed during the six-decade colonization of the East African country."
with open(file_path, 'w') as file:
    file.write(text_to_write)

# (c) Read and display the content of king.txt
with open(file_path, 'r') as file:
    content = file.read()
print("Content of king.txt after writing:")
print(content)

# (d) Append text to king.txt
text_to_append = "\nCharles’s presence has elicited mixed reactions among Kenyans. Some see it as a reminder of the dark colonial past, during which thousands of people were tortured and killed as they fought for the country’s independence. Others say the visit should be viewed as a new chapter in the two countries’ relationship."
with open(file_path, 'a') as file:
    file.write(text_to_append)

# (e) Read and display the contents of king.txt after appending
with open(file_path, 'r') as file:
    appended_content = file.read()
print("Content of king.txt after appending:")
print(appended_content)