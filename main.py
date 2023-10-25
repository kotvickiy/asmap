from questions import *
from random import shuffle



def begin():
    error = 0
    shuffle(quest)
    print()
    for q in quest:
        print("-------------------------------------------------------------------------------------")
        print(q[0])
        answer = input("? ")
        if answer != q[1]:
            error += 1
    print(f"\nОшибок {error}")

def main():
    begin()


if __name__ == '__main__':
    main()
