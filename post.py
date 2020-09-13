"""
Not finished yet.
Or say not started yet :(
"""

import requests
import json


class ExpToolkit:
    def __init__(self):
        self.record = []  # list of json(dict)

        self.host = None
        self.proj_id = None
        self.exp_id = None

        self.headers = None

        self._set_up()

    def _set_up(self):
        self.headers = {"Content-Type": "application/json"}

    def set_host(self, host):
        self.host = host if not host.endswith("/") else host[:-1]

    def set_project(self, proj_id):
        self.proj_id = proj_id

    def register_experiment(self):
        url = f"{self.host}/exp/register/{self.proj_id}"
        r = requests.get(url, headers=self.headers)
        ret = json.loads(r.text)
        try:
            self.exp_id = ret["data"]["_id"]
        except:
            raise ValueError("Bad data structure, no `.data._id` field.")

    def resume_experiment(self, exp_id):
        self.exp_id = exp_id

    def submit(self, data):
        url = f"{self.host}/exp/submit/{self.exp_id}"
        r = requests.post(url, data=json.dumps(data), headers=self.headers)
        print(r.text)


if __name__ == "__main__":
    noob = ExpToolkit()
    noob.set_host("http://localhost:5050/")
    noob.set_project("5f5e081786656163f7a6b7fb")

    # noob.register_experiment()
    noob.resume_experiment("5f5e083a86656163f7a6b801")
    print(noob.exp_id)

    data = {
        "status": "gpu0",
        "progress": "FIN",
        "mrr_5": "0.1232",
        "mrr_20": "0.1679",
        "loss": "5.6662",
    }
    noob.submit(data)
