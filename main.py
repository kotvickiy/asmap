from questions import *
from random import shuffle



def begin():
    error = []
    shuffle(quest)
    print()
    for q in quest:
        print("-------------------------------------------------------------------------------------")
        print(q[0])
        answer = input("? ")
        if answer != q[1]:
            error.append(q[0])
    if error:
        print("\nОшибки:\n")
        for i in error:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(i)

def main():
    begin()


if __name__ == '__main__':
    main()
