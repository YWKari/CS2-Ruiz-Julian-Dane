# Travel Fare Calculator
# Version 3

def fare(d, r, p):
    return d * r * p

FARE_RATE = 14

while True: 
    language = input(print("Enter your language:"))
    
    if language.strip() == "English" or language.strip() == "english": 
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
                    print("Please input a distance above zero (km)")
    
            km = input(print("Is your distance in km? (yes/no)"))
                
            yes = ["yes", "Yes", "yep", "Yep", "ye", "Ye", "Yea", "yea", "yeah", "Yeah", "y", "Y"]
            if km.strip() in yes:
                break
            else:
                print("Please input a distance above zero (km)")
        
        while True:
            passengers_input = input("Enter number of passengers: ")
            
            if passengers_input.isdigit() and int(passengers_input) > 0:
                passengers = int(passengers_input)
                break
            else:
                print("Please input a valid number of passengers (at least 1)")
                
        total_fare = fare(distance, FARE_RATE, passengers)
        
        print("\nPassenger:", name)
        print("Total Fare: PHP", round(total_fare, 2))
        break
    
    
    elif language.strip() == "Tagalog" or language.strip() == "tagalog" or language.strip() == "filipino" or language.strip() == "Filipino": 
        while True:
            name = input("Ilagay ang pangalan: ")
            
            if name.strip() != "":
                break
            else:
                print("Mangyaring maglagay ng pangalan")
        
        while True: 
            while True:
                distance_input = input("Ilagay ang distansya (km): ")
                
                if distance_input.isdigit() and float(distance_input) > 0:
                    distance = float(distance_input)
                    break
                else:
                    print("Mangyaring maglagay ng distansya na higit sa zero (km)")
                    
            km = input(print("Nasa km ba ang distansya mo? (opo/hindi)"))
                
            yes = ["yes", "Yes", "yep", "Yep", "ye", "Ye", "Yea", "yea", "yeah", "Yeah", "y", "Y", "opo", "Opo", "oo", "Oo", "oo po", "Oo po", "Yes po", "yes po"]
            if km.strip() in yes:
                break
            else:
                print("Mangyaring maglagay ng distansya na higit sa zero (km)")
        
        while True:
            passengers_input = input("Ilagay ang bilang ng mga pasahero: ")
            if passengers_input.isdigit() and int(passengers_input) > 0:
                passengers = int(passengers_input)
                break
            else:
                print("Mangyaring maglagay ng wastong bilang ng mga pasahero (hindi bababa sa 1)")
                  
        total_fare = fare(distance, FARE_RATE, passengers)
        
        print("\nPassenger:", name)
        print("Total Fare: PHP", round(total_fare, 2))
        break
    
    else: 
        print("Enter an available language (English/Tagalog)")
