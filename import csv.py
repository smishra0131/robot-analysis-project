import csv 
readings = []
distance = 0
unusual_count = 0
unusual_readings_id = []
below_20 = 0
above_60 = 0

with open('Robot_Sensor_Readings_1000.csv', 'r') as reading:
    reader = csv.reader(reading)

    next(reader)

    for row in reader:
        readings.append(float(row[2]))
        if float(row[-1]) < 20:
            below_20 += 1
        if float(row[-1]) > 60:
            above_60 += 1
        if float(row[-1]) < 20 or float(row[-1]) > 60:
            unusual_count += 1
            unusual_readings_id.append(row[0])

def unusual_percent(readings):
    if len(readings) == 0:
        return 0
    return (unusual_count / len(readings) * 100)




def calculate_average(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)  
print("IMPORT REPORT")
print("----------------")
print("Number of readings:", len(readings))
print("First reading:", readings[0])
print("Last reading:", readings[-1])
print("Minimum:", min(readings))
print("Maximum:", max(readings)) 
print("Average", calculate_average(readings))
print("Readings below 20:", below_20)
print("Readings above 60:", above_60)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(readings))
print("Unusual Reading IDs:", unusual_readings_id)
print(type(row[2]))
print(type(float(row[2])))
for start in range(0, len(readings), 100):
 	group = readings[start:start + 100]
 	print("Group:", start + 1, "to", start + len(group))
 	print("Average:", sum(group) / len(group))



#test a
'''
readings = []
distance = 0
unusual_count = 0
test_a_list = [10, 20, 30, 40, 50]
below_20 = 0
above_60 = 0


unusual_count = 0
for reading in test_a_list:
    if reading < 20:
            below_20 += 1
    if reading > 60:
            above_60 += 1
    if reading < 20 or reading > 60:
            unusual_count += 1

def unusual_percent(test_a_list):
    if len(test_a_list) == 0:
        return 0
    return (unusual_count / len(test_a_list) * 100)




def calculate_average(test_a_list):
    if len(test_a_list) == 0:
        return 0
    return sum(test_a_list) / len(test_a_list)  
print("IMPORT REPORT")
print("----------------")
print("Number of Readings:", len(test_a_list))
print("The first reading is", test_a_list[0])
print("The last reading is", test_a_list[-1])
print("Minimum:", min(test_a_list))
print("Maximum:", max(test_a_list)) 
print("Average", calculate_average(test_a_list))
print("Readings below 20:", below_20)
print("Readings above 60:", above_60)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(test_a_list))
'''


#test b
'''
readings = []
distance = 0
unusual_count = 0
test_b_list = [40, 41, 39, 42, 40, 38, 41, 43, 39, 40,
       	42, 41, 37, 40, 39, 42, 41, 38, 40, 43]

below_20 = 0
above_60 = 0


unusual_count = 0
for reading in test_b_list:
    if reading < 20:
            below_20 += 1
    if reading > 60:
            above_60 += 1
    if reading < 20 or reading > 60:
            unusual_count += 1

def unusual_percent(test_b_list):
    if len(test_b_list) == 0:
        return 0
    return (unusual_count / len(test_b_list) * 100)




def calculate_average(test_b_list):
    if len(test_b_list) == 0:
        return 0
    return sum(test_b_list) / len(test_b_list)  
print("IMPORT REPORT")
print("----------------")
print("Number of Readings:", len(test_b_list))
print("The first reading is", test_b_list[0])
print("The last reading is", test_b_list[-1])
print("Minimum:", min(test_b_list))
print("Maximum:", max(test_b_list)) 
print("Average", calculate_average(test_b_list))
print("Readings below 20:", below_20)
print("Readings above 60:", above_60)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(test_b_list))

'''

#test c
'''
readings = []
distance = 0
unusual_count = 0
test_c_list =  [40, 42, 39, 100, 41, 38, 43, 40, 42, 39,
       	41, 38, 40, 42, 39, 41, 100, 40, 38, 42,
       	41, 39, 40, 43, 38]

below_20 = 0
above_60 = 0


unusual_count = 0
for reading in test_c_list:
    if reading < 20:
            below_20 += 1
    if reading > 60:
            above_60 += 1
    if reading < 20 or reading > 60:
            unusual_count += 1

def unusual_percent(test_c_list):
    if len(test_c_list) == 0:
        return 0
    return (unusual_count / len(test_c_list) * 100)




def calculate_average(test_c_list):
    if len(test_c_list) == 0:
        return 0
    return sum(test_c_list) / len(test_c_list)  
print("IMPORT REPORT")
print("----------------")
print("Number of Readings:", len(test_c_list))
print("The first reading is", test_c_list[0])
print("The last reading is", test_c_list[-1])
print("Minimum:", min(test_c_list))
print("Maximum:", max(test_c_list)) 
print("Average", calculate_average(test_c_list))
print("Readings below 20:", below_20)
print("Readings above 60:", above_60)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(test_c_list))

'''


#test d
'''
readings = []
distance = 0
unusual_count = 0
test_d_list =  [10, 20, 30, 40, 
                60, 70, 80, 90, 100]

below_50 = 0
above_50 = 0

unusual_count = 0
for reading in test_d_list:
    if reading < 50:
            below_50 += 1
    if reading > 50:
            above_50 += 1
    if reading < 50 or reading > 50:
            unusual_count += 1

def unusual_percent(test_d_list):
    if len(test_d_list) == 0:
        return 0
    return (unusual_count / len(test_d_list) * 100)




def calculate_average(test_d_list):
    if len(test_d_list) == 0:
        return 0
    return sum(test_d_list) / len(test_d_list)  
print("IMPORT REPORT")
print("----------------")
print("Number of Readings:", len(test_d_list))
print("The first reading is", test_d_list[0])
print("The last reading is", test_d_list[-1])
print("Minimum:", min(test_d_list))
print("Maximum:", max(test_d_list)) 
print("Average", calculate_average(test_d_list))
print("Readings below 50:", below_50)
print("Readings above 50:", above_50)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(test_d_list))
'''



#Boundary test
'''
readings = []
distance = 0
unusual_count = 0
boundary_test =  [19, 20, 21, 59, 60, 61]
below_20 = 0
above_60 = 0


unusual_count = 0
for reading in boundary_test:
    if reading < 20:
            below_20 += 1
    if reading > 60:
            above_60 += 1
    if reading < 20 or reading > 60:
            unusual_count += 1

def unusual_percent(boundary_test):
    if len(boundary_test) == 0:
        return 0
    return (unusual_count / len(boundary_test) * 100)




def calculate_average(boundary_test):
    if len(boundary_test) == 0:
        return 0
    return sum(boundary_test) / len(boundary_test)  
print("IMPORT REPORT")
print("----------------")
print("Number of Readings:", len(boundary_test))
print("The first reading is", boundary_test[0])
print("The last reading is", boundary_test[-1])
print("Minimum:", min(boundary_test))
print("Maximum:", max(boundary_test)) 
print("Average", calculate_average(boundary_test))
print("Readings below 20:", below_20)
print("Readings above 60:", above_60)
print("Unusual readings:", unusual_count)
print("Unusual percentage:", unusual_percent(boundary_test))
'''