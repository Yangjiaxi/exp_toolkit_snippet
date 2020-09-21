"""
Not finished yet.
Or say not started yet :(
"""

import requests
import json

import random
import numpy as np


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


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def gen_data(gpu, epoch, end=None):
    if end is None:
        end = epoch

    x = np.linspace(0, 5, epoch) + np.abs(np.random.randn((epoch))) * 0.3
    data = sigmoid(x)
    for idx, d in zip(range(1, end + 1), data):
        data = {
            "status": f"gpu{gpu}" if idx < epoch else "FIN",
            "progress": f"{idx}/{epoch}",
            "acc": "{:.4f}".format(d),
            "loss": "{:.4f}".format((1 - d) * 10),
        }
        yield data


if __name__ == "__main__":
    noob = ExpToolkit()
    noob.set_host("https://api-exp.jojo.fit")
    noob.set_project("5f683f2236c3222183c809ba")

    noob.register_experiment()
    # noob.resume_experiment("5f644a4bc677b91d32d25943")
    print(noob.exp_id)

    for d in gen_data(gpu=2, epoch=50):
        # print(d)
        noob.submit(d)

