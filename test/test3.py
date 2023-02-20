# 1
a = ["5","14:10:1", "11:12:8","12:30:9"]
print(sorted(a, key=lambda x: int(x.split(":")[0]),reverse=True))

# 2
a = ["5","14:10:1", "11:12:8","12:30:9"]
print(sorted(a, key=lambda x: int(x.split(":")[0]),reverse=False))














