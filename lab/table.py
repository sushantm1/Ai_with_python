# print("hello")
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('data.csv')
# Assuming your Excel file has columns 'A' and 'B'
# plt.pie(data['year'], data['india']data['china'], data['america'],data['japan'])
plt.pie(data['india'], labels=data['year'])
# plt.xlabel('india')
# plt.ylabel('china')
plt.title('Graph of A vs B')
plt.show()
