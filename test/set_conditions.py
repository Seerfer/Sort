import json
import os

FILE = "conditions.json"

condictions = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/' + FILE, "r"))
algorithms = []
for key, value in condictions["algorithms"].items():
    if value is True:
        algorithms.append(key)
partsort = condictions["other"]["part"]
number_of_arrays = condictions["number_of_arrays"]
array_length = condictions["array_length"]
reverse = condictions["other"]["reverse"]

