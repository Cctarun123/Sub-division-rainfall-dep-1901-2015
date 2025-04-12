#2. Identify Top and Bottom Rainfall Sub-divisions
mean_rainfall_by_region = df.groupby("SUBDIVISION")["ANNUAL"].mean().sort_values()
top_5 = mean_rainfall_by_region.tail(5)
bottom_5 = mean_rainfall_by_region.head(5)

plt.figure(figsize=(12, 6))
plt.barh(bottom_5.index, bottom_5.values, color='tomato', label='Lowest')
plt.barh(top_5.index, top_5.values, color='seagreen', label='Highest')
plt.xlabel("Average Annual Rainfall (mm)")
plt.title("Top and Bottom 5 Sub-divisions by Average Annual Rainfall")
plt.legend()
plt.tight_layout()
plt.show()
