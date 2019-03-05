from msgpackrpc import Client,Address
client = Client(Address('localhost',6789))
result = client.call('double',8)
print(result)