import requests
import time
import csv

# URL of your Flask application running on AWS Elastic Beanstalk
url = [
    "http://servesentiment-env.eba-7m3tpfmd.ca-central-1.elasticbeanstalk.com/1",
    "http://servesentiment-env.eba-7m3tpfmd.ca-central-1.elasticbeanstalk.com/2",
    "http://servesentiment-env.eba-7m3tpfmd.ca-central-1.elasticbeanstalk.com/3",
    "http://servesentiment-env.eba-7m3tpfmd.ca-central-1.elasticbeanstalk.com/4"
]

# Number of times to run the test
num_requests = 100
num_testcases = 4

# List to store latencies
latencies = [[] for _ in range(num_testcases)]

for j in range(num_testcases):
    for i in range(num_requests):
        start_time = time.time()
        response = requests.get(url[j])
        end_time = time.time()

        latency = end_time - start_time
        latencies[j].append(latency)

        print(f"Request {i+1}: {latency:.4f} seconds")

# Write latencies to a CSV file
with open("latencies.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Test Case", "Request Number", "Latency (seconds)"])
    for j in range(num_testcases):
        for i, latency in enumerate(latencies[j], 1):
            csvwriter.writerow([j+1, i, latency])

print("Latencies have been successfully written to latencies.csv")
