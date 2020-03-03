#!/user/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)

#this line will add dns
proto.append("dns")
protoa.append("dns")
print(proto)

# a list of common ports
proto2 = [22,80,443,53]

#pass proto2 as an argument to the extend method
proto.extend(proto2)
print(proto)
#pass proto2 an an argument to the append method
protoa.append(proto2)
print(protoa)

proto3 = [22]

protoa.append(proto3)

