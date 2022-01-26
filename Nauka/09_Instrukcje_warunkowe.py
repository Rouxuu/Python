light = input("Jakie jest światło? (red, green, yellow)")

if light == "red":
    print("Stój!")
elif light == "yellow":
    print("Przygotuj się!")
elif light == "green":
    print("Jedź!")
else:
    print("Miałeś kurwa 3 opcje do wyboru...")

print("Jedź!") if light == "green" else print("Stój!")
