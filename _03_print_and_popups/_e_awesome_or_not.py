from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

if __name__ == '__main__':
  while True:
        num = random.randint(0, 3)
        user = input("enter something you think is awesome! \n_____________________\n")
        if num == 0:
            print(user + " is awesome!")
        elif num == 1:
            print(user + " is okay")
        elif num == 2:
            print(user + " is boring")
        elif num == 3:
            print(user + " is questionable at best")

        # Make a new window variable, window = Tk()

    # Hide the window using the window's .withdraw() method

    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)

    # 2. Print your variable to the console

    # 3. Get the user to enter something that they think is awesome

    # 4. If your variable is  0
    # -- tell the user whatever they entered is awesome!

    # 5. If your variable is  1
    # -- tell the user whatever they entered is ok.

    # 6. If your variable is  2
    # -- tell the user whatever they entered is boring.

    # 7. If your variable is  3
    # -- invent your own message to give to the user (be nice).

    # Run the window's .mainloop() method
