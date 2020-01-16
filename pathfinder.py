import os

os.mkdir("./build")

with open("./build/index.html", "w") as f:
    f.write("<h1>Hello</h1>")
