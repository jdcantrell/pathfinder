import os
from datetime import datetime

if not os.path.isdir("./build"):
    os.mkdir("./build")

this_year = 2020
start = datetime(this_year, 1, 1)
end = datetime(this_year + 1, 1, 1)
now = datetime.now()

total = end - start
current = now - start

percent = round(current / total * 100)
blocks = round(current / total * 80)

run = round(19.7 / 600 * 100)
run_blocks = round(19.7 / 600 * 80)

with open("./build/index.html", "w") as f:
    f.write("<h1>You got this!</h1>")
    f.write("<pre>")
    f.write("Year: {}%\n".format(percent))
    f.write("{}{}\n".format("▓" * blocks, "░" * (80 - blocks)))
    f.write("\n")
    f.write("Running Distance: {}%\n".format(run))
    f.write("{}{}\n".format("▓" * run_blocks, "░" * (80 - run_blocks)))
    f.write("</pre>")
