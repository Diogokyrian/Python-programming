

with open("netrobase.txt", "a") as file:
     file.write("so far so good")

with open("netrobase.txt", "r") as file:
    for line in file.readlines():
        print(line)
        