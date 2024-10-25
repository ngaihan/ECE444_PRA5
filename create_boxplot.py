import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("latencies.csv")

# Extract the latency data
latencies = df["Latency (seconds)"]

# Create a boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(latencies, vert=False)
plt.title("Latency Boxplot")
plt.xlabel("Latency (seconds)")
plt.grid(True)

# Save the boxplot as an image file
plt.savefig("latency_boxplot.png")

# Show the boxplot
plt.show()
