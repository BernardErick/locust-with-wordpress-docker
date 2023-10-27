from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "http://localhost"
    def on_start(self):
        self.client.post("/wp-login.php", {
            "username": "admin",
            "password": "12345678"
        })
    
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/2023/10/27/blog-post-com-uma-imagem-de-aproximadamente-1mb/")
        self.client.get("/2023/10/27/blog-post-com-um-texto-de-aproximadamente-400kb/")
        self.client.get("/2023/10/27/blog-post-com-uma-imagem-de-300kb/")
        