from bs4 import BeautifulSoup
import requests
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

merger = pd.read_csv('ic_gdp2.csv')
merger = merger.dropna()

c = list(merger['Share of internet users'])
y=[]
for i in c:
    y.append(float(i.strip('%')))
x = list(merger['Nominal GDP($ billions)'])
bb = np.array(x)
#print(y)

plt.figure(figsize=(6,4))
plt.scatter(x,y)
plt.xlabel('Nominal GDP($ billions)')
plt.ylabel('Internet access(Percent)')
plt.title('Does internet access increase with GDP')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()

# print(np.median(y))


grad = (443.07-34.81)/(57.59-27.18)
print(grad)

