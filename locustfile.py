from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "http://localhost"
    def on_start(self):
        self.client.post("/login", {
            "username": "admin",
            "password": "12345678"
        })
    
    @task
    def index(self):
        self.client.get("/")