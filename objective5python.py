# 5: Identify the Rainiest Year for Each Sub-division
max_rainfall = df.loc[df.groupby("SUBDIVISION")["ANNUAL"].idxmax()]
top5_rainy = max_rainfall.sort_values("ANNUAL", ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(top5_rainy["SUBDIVISION"], top5_rainy["ANNUAL"], color='blue')
plt.title("Top 5 Rainiest Years by Sub-division")
plt.xlabel("Sub-division")
plt.ylabel("Annual Rainfall (mm)")
#plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
