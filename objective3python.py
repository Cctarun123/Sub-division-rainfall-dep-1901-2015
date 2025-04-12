#3. Compare Rainfall Across Seasons
seasonal_columns = ['JF', 'MAM', 'JJAS', 'OND']
seasonal_means = df[seasonal_columns].mean()

plt.figure(figsize=(8, 6))
plt.bar(seasonal_means.index, seasonal_means.values, color='skyblue')
plt.title("Average Rainfall Across Seasons")
plt.xlabel("Season")
plt.ylabel("Average Rainfall (mm)")
plt.tight_layout()
plt.show()
