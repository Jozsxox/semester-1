# Week 1.2, Session 2: Task 6
temperature = float(input("what's the machine's temperature? :"))
if temperature > 80 :
    print(f"shut down the machine")
elif 50 < temperature < 80:
    print(f"the machine is within safe limits")
elif temperature < 50:
    print(f"the machine is low and no action is needed")

pressure = float(input("what's the machine's pressure?:"))
