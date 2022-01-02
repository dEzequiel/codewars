def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    distance_travel = mpg * fuel_left;

    if distance_to_pump <= distance_travel:
        return True;
    else:
        return False;