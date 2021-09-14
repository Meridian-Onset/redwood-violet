import os
import json
# TODO: implement a defaultdict version of this

cwd = os.path.dirname(os.path.realpath(__file__))

json_path = os.path.join(cwd, 'cfg.json')

with open(json_path) as f:
    conf = json.load(f)




if __name__ == "__main__":
    for key in conf.keys():
        print(conf[key])
