
from bokeh.plotting import figure, show
import math

file = open("data.txt","r", encoding = "utf8")
data = {}

for line in file: 
    (num_hours, question_1, question_2) = line.split(",")
    num_hours = int(num_hours)
    if num_hours in data:
         data[num_hours] += 1
    else:
        data[num_hours] = 1

sorted_hrs = sorted(data.items(), key = lambda x:x[1], reverse = True)

file.close()

hours = [entry[0] for entry in sorted_hrs]
count = [entry[1] for entry in sorted_hrs]

x_values = list(range(len(hours)))

d = figure(title = "Hours spent on an electronic device", x_range = [str(hour) for hour in hours])

d.vbar(x = x_values, top = count, width = .90)

show(d)