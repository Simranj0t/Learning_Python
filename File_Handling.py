# # command to open an existing file in the location

# file = open("demo.txt","r")
# data = file.read()
# print(data)
# print(type(data))
# file.close()

# # To read the file line by line 

# file = open("demo.txt","r")
# line1 = file.readline()
# print(line1)

# line2 = file.readline()
# print(line2)
# file.close()

# # Or this command can also work as 

# with open("demo.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()

# print(line1)
# print(line2)
# file.close()

#  to add the line using the w - overrite mode and a - to append the text
# file = open("demo.txt","w")
# file.write("This is a new line to test the Write mode with -w")
# print(file)
# file.close()

# # to add the line using the w - overrite mode and a - to append the text
# file = open("demo.txt","a")
# file.write("This is a new line to test the Write mode with -a")
# print(file)
# file.close()

# Deleting a file 
# import os 
# os.remove("status.txt")

# Practice question

# with open("practice.txt","w") as f:
    # data = f.write("This is a new file\n This is new line ")
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
