import redis
r = redis.Redis(host="127.0.0.1", port=6379,password='ls-root123')
# r.setbit("foo", 0, 1)   # 1
# r.setbit("foo", 1, 1)   # 1
# r.setbit("foo", 2, 1)   # 1
# r.setbit("foo", 3, 1)   # 1
# r.setbit("foo", 4, 1)   # 1
# r.setbit("foo", 5, 1)   # 1
# r.setbit("foo", 6, 1)   # 1
# r.setbit("foo", 7, 1)   # 1
r.setbit("foo", 1089, 1)

print(r.get("foo"))