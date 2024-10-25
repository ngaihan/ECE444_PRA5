import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("latencies.csv")

# Create a figure for the boxplots
plt.figure(figsize=(12, 8))

# Create a boxplot for each test case
for test_case in range(1, 5):
    # Extract the latency data for the current test case
    latencies = df[df["Test Case"] == test_case]["Latency (seconds)"]
    
    # Create a subplot for the current test case
    plt.subplot(2, 2, test_case)
    plt.boxplot(latencies, vert=False)
    plt.title(f"Latency Boxplot for Test Case {test_case}")
    plt.xlabel("Latency (seconds)")
    plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the boxplots as an image file
plt.savefig("latency_boxplots.png")

# Show the boxplots
plt.show()
