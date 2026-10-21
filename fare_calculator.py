# Travel Fare Calculator
# Ver 2.1

def fare(d, r, p):
    return d * r * p

while True:
    name = input("Enter passenger name: ")
    
    if name.strip() != "":
        break
    else:
        print("Please input a name")

while True: 
    while True:
        distance_input = input("Enter distance (km): ")
        
        if distance_input.isdigit() and float(distance_input) > 0:
            distance = float(distance_input)
            break
        else:
            print("Please input a distance above zero in km")
    
    km = input(print("Is your distance in km? (yes/no)"))
    
    yes = ["yes", "Yes", "yep", "Yep", "ye", "Ye", "Yea", "yea", "yeah", "Yeah", "y", "Y"]
    if km.strip() in yes:
        break
    elif km.strip() == "":
        print("Please input a distance above zero in km")
    else:
        print("Please input a distance above zero in km")

while True:
    passengers_input = input("Enter number of passengers: ")
    
    if passengers_input.isdigit() and int(passengers_input) > 0:
        passengers = int(passengers_input)
        break
    else:
        print("Please input a valid number of passengers (at least 1)")

FARE_RATE = 14

total_fare = fare(distance, FARE_RATE, passengers)

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
