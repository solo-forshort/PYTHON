from prettytable import PrettyTable
from matplotlib import pyplot as plt
import numpy as np

table = PrettyTable(["Name", "Age", "Occupation"])
table.add_row(["Asare", 24, "Developer"])
table.add_row(["Ama", 30, "Designer"])
table.add_row(["Kofi", 28, "Manager"])
table.add_row(["Ben", 39, "Pharmacist"])
table.add_row(["Efo", 54, "Traditionalist"])
print(table)

Point_1 = np.array([1, 2, 3, 4, 5])
Point_2 = np.array([2, 3, 5, 7, 11])
Point_3 = np.array([1, 4, 9, 16, 25])
Point_4 = np.array([1, 8, 27, 64, 125])

plt.plot(Point_1, Point_2)
plt.plot(Point_1, Point_3)
plt.plot(Point_3, Point_4)
plt.plot(Point_1, Point_4)

plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()