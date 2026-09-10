import csv 
readings = []
distance = 0
with open('Robot_Sensor_Readings_1000.csv', 'r') as reading:
    reader = csv.reader(reading)
    for row in reader:
        print(row)

        