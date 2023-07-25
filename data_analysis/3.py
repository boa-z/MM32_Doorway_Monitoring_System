import csv
import matplotlib.pyplot as plt

counts = {1:0, 2:0, 3:0}

with open('guest.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        guest_type = int(row[2])
        counts[guest_type] += 1

labels = 'password', 'Card', 'Face'
sizes = [counts[1], counts[2], counts[3]]
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.title("Guest Type Ratio")
plt.show()