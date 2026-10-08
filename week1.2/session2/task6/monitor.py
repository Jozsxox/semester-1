# Week 1.2, Session 2: Task 6

#Temperature
temperature = int(input("what's the machine's temperature? :"))
if temperature > 80 :
    print(f"shut down the machine")
elif 50 < temperature < 80:
    print(f"the machine is within safe limits")
elif temperature < 50:
    print(f"the machine is low and no action is needed")

#Pressure
pressure = int(input("what's the machine's pressure?:"))
if pressure > 100:
    print(f"the recommend maintenance")
elif 70 < pressure < 100:
    print(f"pressure is stable")
elif pressure < 70:
    print(f"Pressure of the system is operating normally")

#Determine Status
if temperature > 80 or pressure > 100:
         print(f"conditions and recommend shutting it down")
elif temperature < 50:
    print(f"machine stopped and no immediate actuon is needed")
else:
    print(f"the machine is running normally")