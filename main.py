from questions import *





def fun_begin():
    for q in quest:
        print(q[0])
        answer = input("? ")
        if answer == q[1]:
            print("ok")
        else:
            print("no")


def main():
    start = input("Начать?(д/н): ")
    if start == "д" or start == "y" or start == "да" or start == "yes":
        fun_begin()
    else:
        print("До свидания")


if __name__ == '__main__':
    main()
