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

    def submit(self, data):
        url = f"{self.host}/exp/submit/{self.exp_id}"
        r = requests.post(url, data=json.dumps(data), headers=self.headers)
        print(r.text)


if __name__ == "__main__":
    noob = ExpToolkit()
    noob.set_host("http://localhost:5050/")
    noob.set_project("5f5b1f5d5094d2148a4a3c65")

    noob.register_experiment()
    noob.submit({"key": "231313", "value": "q23434324"})
