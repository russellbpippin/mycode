#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])


#print(switch["lynx"])


print("first test - .get()")
print(switch.get("lynx"))
print("second test - .get()")
print(switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!"))
print("third test - .get()")
print(switch.get("version"))
print("fourth test - .keys()")
print(switch.keys())
print("fifth test - .values()")
print(switch.values())
print("sixth test - pop()")
switch.pop("version")
print(switch.keys())
print(switch.values())
print("seventh test - Add ne value")
switch["adminlogin"]="kar108"
print(switch.keys())
print(switch.values())
print("eigth test - add new value")
switch["password"]="qwerty"
print(switch.keys())
print(switch.values())

