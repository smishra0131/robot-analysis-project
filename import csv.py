'''
import csv 
readings = []
distance = 0
unusual_count = 0
with open('Robot_Sensor_Readings_1000.csv', 'r') as reading:
    reader = csv.reader(reading)

    readings = [10, 20, 30, 40, 50]

    next(reader)

    for row in reader:
        readings.append(float(row[2]))


    for reading in readings:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(readings) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", + len(readings))
print("The first reading is", + readings[0])
print("The last reading is", + readings[-1])
print("Minimum:", min(readings))
print("Maximum:", max(readings)) 
print("Average", sum(readings) / len(readings))
def calculate_average(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)  
'''




'''
readings = []
distance = 0
unusual_count = 0
test_a_list = [10, 20, 30, 40, 50]

def finding_unusual_count(test_a_list):
    unusual_count = 0
    for reading in test_a_list:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
    return unusual_count

unusual_count = finding_unusual_count(test_a_list)
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(test_a_list) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", len(test_a_list))
print("The first reading is", test_a_list[0])
print("The last reading is", test_a_list[-1])
print("Minimum:", min(test_a_list))
print("Maximum:", max(test_a_list)) 
print("Average", sum(test_a_list) / len(test_a_list))
def calculate_average(readings):
    if len(test_a_list) == 0:
        return 0
    return sum(test_a_list) / len(test_a_list)  
'''



'''
readings = []
distance = 0
unusual_count = 0
test_b_list = [40, 41, 39, 42, 40, 38, 41, 43, 39, 40,
       	42, 41, 37, 40, 39, 42, 41, 38, 40, 43]


def finding_unusual_count(test_b_list):
    unusual_count = 0
    for reading in test_b_list:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
    return unusual_count

unusual_count = finding_unusual_count(test_b_list)
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(test_b_list) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", len(test_b_list))
print("The first reading is", test_b_list[0])
print("The last reading is", test_b_list[-1])
print("Minimum:", min(test_b_list))
print("Maximum:", max(test_b_list)) 
print("Average", sum(test_b_list) / len(test_b_list))
def calculate_average(readings):
    if len(test_b_list) == 0:
        return 0
    return sum(test_b_list) / len(test_b_list)  
'''


'''
readings = []
distance = 0
unusual_count = 0
test_c_list =  [40, 42, 39, 100, 41, 38, 43, 40, 42, 39,
       	41, 38, 40, 42, 39, 41, 100, 40, 38, 42,
       	41, 39, 40, 43, 38]


def finding_unusual_count(test_c_list):
    unusual_count = 0
    for reading in test_c_list:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
    return unusual_count

unusual_count = finding_unusual_count(test_c_list)
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(test_c_list) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", len(test_c_list))
print("The first reading is", test_c_list[0])
print("The last reading is", test_c_list[-1])
print("Minimum:", min(test_c_list))
print("Maximum:", max(test_c_list)) 
print("Average", sum(test_c_list) / len(test_c_list))
def calculate_average(readings):
    if len(test_c_list) == 0:
        return 0
    return sum(test_c_list) / len(test_c_list)  
'''



'''
readings = []
distance = 0
unusual_count = 0
test_d_list =  [1000, 9999, 7439, 
        7782137231, 88885, 
        666777, 44443, 
        8886634, 777222, 
        66622552,2997745,
        994848, 9938484, 
        2525525, 73736636, 743847]


def finding_unusual_count(test_d_list):
    unusual_count = 0
    for reading in test_d_list:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
    return unusual_count

unusual_count = finding_unusual_count(test_d_list)
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(test_d_list) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", len(test_d_list))
print("The first reading is", test_d_list[0])
print("The last reading is", test_d_list[-1])
print("Minimum:", min(test_d_list))
print("Maximum:", max(test_d_list)) 
print("Average", sum(test_d_list) / len(test_d_list))
def calculate_average(readings):
    if len(test_d_list) == 0:
        return 0
    return sum(test_d_list) / len(test_d_list)  
'''

readings = []
distance = 0
unusual_count = 0
boundary_test =  [19, 20, 21, 59, 60, 61]

def finding_unusual_count(boundary_test):
    unusual_count = 0
    for reading in boundary_test:
 	    if reading < 20 or reading > 60:
               unusual_count += 1
    return unusual_count

unusual_count = finding_unusual_count(boundary_test)
print("Unusual readings:", unusual_count)
percentage = unusual_count / len(boundary_test) * 100
print("Unusual percentage:", percentage)

print("Number of Readings:", len(boundary_test))
print("The first reading is", boundary_test[0])
print("The last reading is", boundary_test[-1])
print("Minimum:", min(boundary_test))
print("Maximum:", max(boundary_test)) 
print("Average", sum(boundary_test) / len(boundary_test))
def calculate_average(readings):
    if len(boundary_test) == 0:
        return 0
    return sum(boundary_test) / len(boundary_test)  
