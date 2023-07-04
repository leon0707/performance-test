from locust import HttpUser, between, task

class WebUIUser(HttpUser):
    wait_time = between(2, 5)
    
    @task
    def generate_image(self):
        self.client.post("/sdapi/v1/txt2img", json={
            "seed": -1,
            "cfgScale": 7,
            "width": 512,
            "height": 512,
            "sampler_name": "Euler a",
            "sampler_index": "Euler a",
            "prompt": "Oil painting of a bustling harbor town, with fishing boats, seagulls, and a lighthouse in the background, high contrast, dramatic lighting, heavily textured brushstrokes",
            "negative_prompt": "",
            "steps": 20,
            "batch_size": 1,
            "save_images": False
        })