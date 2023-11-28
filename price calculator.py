MV = eval(input("ENTER MILEAGE OF YOUR VEHICLE :"))
FC = eval(input("ENTER FUEL CAPACITY OF YOUR VEHICLE :"))
AS = eval(input("ENTER AVERAGE SPEED :"))
DI = MV * FC
LI = 103.67
print("Distance for per full fueling for your vehicle :",DI)
MF = FC * LI
print("Price for your vehicle per full fueling :",MF)
TI = DI/AS
print("Time Taken For Distance :",TI)

