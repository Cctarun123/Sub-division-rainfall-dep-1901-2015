#4. Detect Rainfall Anomalies
import numpy as np

mean_annual = df["ANNUAL"].mean()
std_annual = df["ANNUAL"].std()
threshold = 2
anomalies = df[np.abs(df["ANNUAL"] - mean_annual) > threshold * std_annual]

plt.figure(figsize=(12, 6))
plt.scatter(df["YEAR"], df["ANNUAL"], alpha=0.5, label="Normal")
plt.scatter(anomalies["YEAR"], anomalies["ANNUAL"], color='red', label="Anomaly")
plt.title("Rainfall Anomalies Detection")
plt.xlabel("Year")
plt.ylabel("Annual Rainfall (mm)")
plt.legend()
plt.tight_layout()
plt.show()

