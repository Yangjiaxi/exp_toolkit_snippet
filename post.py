"""
Not finished yet.
Or say not started yet :(
"""

import requests
import json

import random


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


def gen_data(gpu, epoch, end=None):
    if end is None:
        end = epoch
    for idx in range(1, end + 1):
        data = {
            "status": f"gpu{gpu}" if idx < epoch else "FIN",
            "progress": f"{idx}/{epoch}",
            "mrr_5": "{:.4f}".format(0.1234 + idx * 0.001 + (random.random() - 0.5) * 0.1),
            "mrr_20": "{:.4f}".format(0.1681 + idx * 0.001 + (random.random() - 0.5) * 0.1),
            "loss": "{:.4f}".format(6.556 - idx * 0.001 + (random.random() - 0.5) * 0.5),
        }
        yield data


if __name__ == "__main__":
    noob = ExpToolkit()
    noob.set_host("http://localhost:5050")
    noob.set_project("5f5ebf156ee8596d1c084fb9")

    noob.register_experiment()
    # noob.resume_experiment("5f61d67d5571e5d5ee451e4d")
    print(noob.exp_id)

    for d in gen_data(gpu=1, epoch=20):
        noob.submit(d)

    # data = {
    #     "status": "gpu0",
    #     "progress": "FIN",
    #     "mrr_5": "0.1234",
    #     "mrr_20": "0.1681",
    #     "loss": "5.6660",
    # }
    # noob.submit(data)
