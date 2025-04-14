#1. Analyze Yearly Rainfall Trends
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\cctar\\Downloads\\cleaned_rainfall_data.csv")
yearly_rainfall = df.groupby("YEAR")["ANNUAL"].mean()
plt.figure(figsize=(12, 6))
plt.plot(yearly_rainfall.index, yearly_rainfall.values, color='blue', linewidth=2)
plt.title("Average Annual Rainfall Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Annual Rainfall (mm)")
plt.grid(True)
plt.tight_layout()
plt.show()
