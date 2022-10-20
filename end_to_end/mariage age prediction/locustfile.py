import numpy as np
from locust import task
from locust import between
from locust import HttpUser

sample = {
  "gender": "female",
  "height": 159.5,
  "religion": "Hindu",
  "caste": "Thakur",
  "mother_tongue": "Hindi"
}
class AgeOfMarriageTestUser(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H http://localhost:3000
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)