TWO_SEATER_PLANE_ONE_COST = 100
TWO_SEATER_PLANE_TWO_COST = 150
FOUR_SEATER_PLANE_ONE_COST = 120
FOUR_SEATER_PLANE_TWO_COST = 200
HISTORIC_PLANE_ONE_COST = 300
HISTORIC_PLANE_TWO_COST = 500
THIRTY_MINUTE_FLIGHTS = 0.5
COOLDOWN = 0.5
ONE_HOUR_FLIGHTS = 1
WORKING_HOURS = 10

while True: 
    print("Type of plane?", '"2 Seater Plane" or "4 Seater Plane" or "Historical Plane?"')
    plane = input()
    if plane == "2 Seater Plane" or plane == "4 Seater Plane" or plane == "Historical Plane":
        print("Length of plane?", '"1 Hour" or "30 Minutes?"')
        length = input()
    else: 
        print("Not an option")
        continue
    if length == "30 Minutes":
        total_flights = WORKING_HOURS / (THIRTY_MINUTE_FLIGHTS + COOLDOWN)
        two_seater_plane = TWO_SEATER_PLANE_ONE_COST
        four_seater_plane = FOUR_SEATER_PLANE_ONE_COST 
        historical_plane =  HISTORIC_PLANE_ONE_COST
        print("The maximum amount of flights for 30 minute flights in one day is" , total_flights)
        break
    elif length == "1 Hour":
        total_flights = WORKING_HOURS / (ONE_HOUR_FLIGHTS + COOLDOWN)
        two_seater_plane = TWO_SEATER_PLANE_TWO_COST
        four_seater_plane = FOUR_SEATER_PLANE_TWO_COST
        historical_plane = HISTORIC_PLANE_TWO_COST
        print("The maximum amount of flights for 1 hour flights in one day is" , total_flights)
        break
    else: 
        print("Not an option")
        continue
    
if plane == "2 Seater Plane":
    print("total cost is",  total_flights * two_seater_plane)
elif plane == "4 Seater Plane":
    print("total cost is", total_flights * four_seater_plane)
else: 
    print("total cost is", total_flights * historical_plane)







   




