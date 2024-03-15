import os
import random
from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class NextcloudUser(HttpUser):
    auth = None
    user_name = None
    wait_time = between(2, 5)

    # users to test this with.
    def on_start(self):
        user_idx = random.randrange(1, 50)
        self.user_name = f'TestUser_{user_idx}'
        self.auth = HTTPBasicAuth(self.user_name, f'TestPassword_{user_idx}')

    @task(5)
    def propfind(self):
         self.client.request("PROPFIND", f"/remote.php/dav/files/{self.user_name}/", auth=self.auth)

    @task(5)
    def read_file(self):
        self.client.get(f"/remote.php/dav/files/{self.user_name}/Readme.md", auth=self.auth)

    @task(10)
    def upload_file_text(self):
        with open("/data/file.txt", "rb") as file:
            self.client.put(f"/remote.php/dav/files/{self.user_name}/file.txt", data=file, auth=self.auth)
        self.client.delete(f"/remote.php/dav/files/{self.user_name}/file.txt", auth=self.auth)
        
    @task(10)
    def upload_file_1kb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1kb_file_{random.randrange(0, 10)}"
        with open("/data/file_1kb", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
        self.client.delete(remote_path, auth=self.auth)

    @task(5)
    def upload_file_1Mb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1Mb_file_{random.randrange(0, 10)}"
        with open("/data/file_1Mb", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
        self.client.delete(remote_path, auth=self.auth)
        
    @task(1)
    def upload_file_1Gb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1Gb_file_{random.randrange(0, 10)}"
        with open("/data/file_1Gb", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
        self.client.delete(remote_path, auth=self.auth)
