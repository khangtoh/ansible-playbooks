from locust import HttpLocust, TaskSet, task, between

class UserBehaviour(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8089"
    task_set = UserBehaviour
    wait_time = between(5, 9)