import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv")
print(data)
print(data.head())

plt.plot(data['year'], data['india'], label='India')
plt.plot(data['year'], data['china'], label='China')
plt.plot(data['year'], data['america'], label='America')
plt.plot(data['year'], data['japan'], label='Japan')

plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Data Distribution Over Years')
plt.legend()
plt.show()

# Create a pie chart
# data_2005 = data[data['year'] == 2005].iloc[0, 1:]
# plt.pie(data_2005, labels=data_2005.index, autopct='%1.1f%%', startangle=140)
# plt.title('Pie Chart of countries by year')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
