import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input rows, or "masses"
with open(os.path.join(dirname, "input.txt")) as masses_list:
    masses = [int(masses) for masses in masses_list]

def calculateFuel(mass): 
    return math.floor(mass/3) - 2

def calculateFuelTotal():
    sum = 0
    for mass in masses:
        fuelMass = calculateFuel(mass)
        fuelFuelMass = calculateFuelsFuel(fuelMass)
        sum += fuelMass + fuelFuelMass

    return sum

def calculateFuelsFuel(mass):
    sum = 0
    fuelMass = calculateFuel(mass)
    while fuelMass > 0:
        sum += fuelMass
        fuelMass = calculateFuel(fuelMass)
        
    return sum

#print total
print(calculateFuelTotal())