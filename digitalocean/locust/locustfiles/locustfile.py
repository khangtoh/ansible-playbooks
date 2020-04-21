from locust import HttpLocust, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust
from dotenv import load_dotenv
load_dotenv()

import os

import sentry_sdk
from sentry_sdk import capture_exception, capture_message

class UserTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")
    
    @task
    def stats(self):
        self.client.get("/stats/requests")

class SentryTask(TaskSet):
    @task
    def sendEvent(self):
        capture_message('Something went wrong')
    @task
    def sendException(self):
        try:
            missingfunc()
        except Exception as e:
            # Alternatively the argument can be omitted
            capture_exception(e)

class WebsiteUser(FastHttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """
    host = "http://127.0.0.1:8089"
    wait_time = between(2, 5)
    tasks = [SentryTask]
    sentrydsn = os.getenv('SENTRY_DSN')
    sentry_sdk.init(sentrydsn)
