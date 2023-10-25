from questions import *
from random import shuffle



def fun_begin():
    shuffle(quest)
    print()
    for q in quest:
        print("-------------------------------------------------------------------------------------")
        print(q[0])
        answer = input("? ")
        if answer == q[1]:
            print("ok\n")
        else:
            print("no\n")


def main():
    start = input("Начать?(д/н): ")
    if start == "д" or start == "y" or start == "да" or start == "yes":
        fun_begin()
    else:
        print("До свидания")


if __name__ == '__main__':
    main()
