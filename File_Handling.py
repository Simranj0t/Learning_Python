# command to open an existing file in the location

file = open("demo.txt","r")
data = file.read()
print(data)
print(type(data))
file.close()

# To read the file line by line 

file = open("demo.txt","r")
line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)
file.close()

# or this command can also work as 

with open("demo.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)