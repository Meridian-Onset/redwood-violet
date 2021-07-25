import os
import json


cwd = os.path.dirname(os.path.realpath(__file__))

butt = os.path.join(cwd, 'cfg.json')

with open(butt) as f:
    conf = json.load(f)

if __name__ == "__main__":
    for key in conf.keys():
        print(conf[key])
