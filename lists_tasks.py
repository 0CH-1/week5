def directions():
    steps = ["Move forward", "Move backward", "Turn Left", "Turn Right"]
    return steps


def movements():
    path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path



def run_task1():
    print(directions())

def run_task2():
    print("Moving...")
    path = movements()
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")

def menu():
    print("Please select a direction: ")
    steps=directions()
    for index in range(len(steps)):
        print(f"{index} : {steps[index]}")

def run_task3():
    menu()

def menu_and_input():
    print("Please select a direction: ")
    steps=directions()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")
    choice = int(input())
    print()

    return steps[choice]

def run_task4():
    route=[]
    print("Working out escape route...")
    print()
    for _ in range(5):
        direction = menu_and_input()
        route.append(direction)
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run_task1()
    run_task2()
    run_task3()
    run_task4()


# new code
#def movements():
#    steps = ["Move forward", "Move Backward", "Turn Left", "Turn Right"]
#    return steps



# if __name__ == "__main__":
#     run()
#
#
# # new code
# def directions():
#     steps = ["Move forward", "Move Backward", "Turn Left", "Turn Right"]
#     return steps
#

#
#     if __name__ == "__main__":
#         run()

