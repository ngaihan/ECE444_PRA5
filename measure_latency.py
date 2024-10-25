import requests
import time
import csv

# URL of your Flask application running on AWS Elastic Beanstalk
url = "http://servesentiment-env.eba-7m3tpfmd.ca-central-1.elasticbeanstalk.com/"

# Number of times to run the test
num_requests = 100

# List to store latencies
latencies = []

for i in range(num_requests):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    latency = end_time - start_time
    latencies.append(latency)

    print(f"Request {i+1}: {latency:.4f} seconds")

# Write latencies to a CSV file
with open("latencies.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Request Number", "Latency (seconds)"])
    for i, latency in enumerate(latencies, 1):
        csvwriter.writerow([i, latency])

print("Latencies have been successfully written to latencies.csv")

# Calculate average latency
average_latency = sum(latencies) / num_requests
print(f"\nAverage Latency: {average_latency:.4f} seconds")
