# importing the required module
import matplotlib.pyplot as plt

file_location = "C:\\Python\\x_values.txt"
fh = open(file_location, "r")
x = fh.read()
x = x.split("\n")
x_values = []
count = 0

for i in x:
    count = count + 1
    int_i = int(i)
    x_values.append(int_i)

print(type(x_values))
print(x_values)


file_location = "C:\\Python\\y_values.txt"
fh = open(file_location, "r")
y = fh.read()
y = y.split("\n")
y_values = []
count = 0
print(y)

for i in y:
    count = count + 1
    int_i = int(i)
    y_values.append(int_i)
print(y_values)

# x axis values
x = x_values
# corresponding y axis values
y = y_values

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
