from graph import create_graph
from navigation import find_path, get_steps
from voice import speak

def main():
    G = create_graph()

    start = input("Enter your current location: ")
    end = input("Where do you want to go? ")

    try:
        path = find_path(G, start, end)
        print("Path:", path)

        steps = get_steps(path)

        for step in steps:
            print(step)
            speak(step)

    except:
        print("Invalid location entered!")

if __name__ == "__main__":
    main()