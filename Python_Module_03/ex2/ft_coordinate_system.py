import math


def get_player_pos() -> tuple:
    while True:
        cordonates = input("Enter new coordinates as floats in format " +
                           "'x,y,z': ")
        mylist = []
        try:
            if "," in cordonates:
                mylist = cordonates.split(",")
            try:
                for x in mylist:
                    float(x)
                return (float(mylist[0]), float(mylist[1]), float(mylist[2]))
            except ValueError as e:
                print(f"Error on parameter '{x}': {e}")
        except Exception as e:
            print(f"Invalid syntax : {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    mytuple = get_player_pos()
    print(f"Got a first tuple: {mytuple}")
    x1, y1, z1 = mytuple
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: "
          f"{round(math.sqrt((x1)**2 + (y1)**2 + (z1)**2), 4)}")
    print("\nGet a second set of coordinates")
    mytup = get_player_pos()
    x2, y2, z2 = mytup
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2), 4)}")
