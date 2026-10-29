def directions():
 steps = ["Move forward", "Move Backward", "Turn Left", "Turn Right"]
 return steps

def run():
    steps = directions()
    print(steps)

if __name__ == "__main__":
    run()