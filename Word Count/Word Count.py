from tkinter import *
   
#Creates the function that calculates the amount of words read   
def countWords():
    wordList=[]
    sentence=sentEnt.get(1.0,END)
    wordList.append(sentence)
    wordsSplit=str(wordList).split()
    wordsCounted=(len(wordsSplit))
    wordCount.set(wordsCounted)
    



window=Tk()
window.title('Word Count')


#Label and entry for the sentence to be counted 
sentLbl=Label(window,text='Enter Words To Count:',font=('Verdana',12))
sentLbl.grid(row=0,column=2,columnspan=1,sticky=NW,pady=10)
sentEnt=Text(window)
sentEnt.grid(row=0,rowspan=2,column=1,columnspan=2,sticky=S,pady=35)


#Creates a button that calls to the function to count the words 
countButton=Button(window,text='COUNT',font=('Verdana',16),command=countWords)
countButton.grid(row=4,column=1,columnspan=2,sticky=N,pady=15,padx=25)

#Crreates an entry box & Label to display the number of words
wordCount=StringVar()
wordLabel=Label(window,text='Number of Words:',font=('Verdana',12))
wordLabel.grid(row=5,column=1,columnspan=2,sticky=N,pady=1,padx=25)
numberOfWords=Entry(window,state='readonly',fg='red',textvariable=wordCount,font=('Verdana',10))
numberOfWords.grid(row=5,column=1,columnspan=2,sticky=S,pady=25,padx=25)

window.mainloop()
