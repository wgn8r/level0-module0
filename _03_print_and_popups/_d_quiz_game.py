from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    x=simpledialog.askstring(title=None,prompt="what is the quadratic formula?")
    #      // 3.  Use an if statement to check if their answer is correct
    if x=="(-b±√b^2-4ac)/2a":
        score+=1
    x = simpledialog.askstring(title=None, prompt="who won the masters in 2020")
    if x.upper()=="DUSTIN JOHNSON":
        score+=1
    x = simpledialog.askstring(title=None, prompt="who won the british open last year")
    if x.upper() == "CAMERON SMITH":
        score += 1
    messagebox.showinfo(title=None,message=score)
    window.mainloop()
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
