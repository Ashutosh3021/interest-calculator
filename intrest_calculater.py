import math as mt
amount=float(input("enter your initial capital: "))
while amount<=0:
    print ("initial capital can't be -ve or 0")
    amount=float(input("enter your amount again: "))

roi=float(input("enter the rate of interest: "))
while roi<=0:
    print ("rate of intrest can't be -ve or 0")
    roi=float(input("enter your rate of intrest again: "))
time=int(input("Length of time, in years, that you plan to save: "))
while time<=0:
    print ("time can't be -ve or 0")
    time=int(input("enter time again: "))
contri=float(input("Amount that you plan to add to the principal every month, or a negative number for the amount that you plan to withdraw every month(+ve for deposal and -ve for withdrawl): "))
no_of_time_intrest_is_compounded=float(input("enter the time of interest compounded in terms of year: "))
while no_of_time_intrest_is_compounded<=0:
    print ("no_of_time_intrest_is_compounded can't be -ve or 0")
    no_of_time_intrest_is_compounded=float(input("enter your no_of_time_intrest_is_compounded again: "))

future_value = amount*(1+(roi/100)/no_of_time_intrest_is_compounded)**(no_of_time_intrest_is_compounded*time) + contri * (((1+(roi/100)/no_of_time_intrest_is_compounded)**(no_of_time_intrest_is_compounded*time)-1)/((roi/100)/no_of_time_intrest_is_compounded))
future_value=mt.ceil(future_value)
print(f"your future value is {future_value}")