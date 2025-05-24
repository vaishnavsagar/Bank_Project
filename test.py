data = [
    {"acc_no": 100, "name": "A", "age": 26},
    {"acc_no": 101, "name": "B", "age": 30},
    {"acc_no": 102, "name": "C", "age": 21},
]

index = next((i for i, item in enumerate(data) if item["acc_no"] == 101), -1)
print(index)

print(next(i for i, item in enumerate(data) if item["acc_no"] in [101, 102, 103]))