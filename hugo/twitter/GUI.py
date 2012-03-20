'''
Created on Mar 20, 2012

@author: root
'''
import Tkinter
from Tkinter import Frame, Tk, LabelFrame, Text, Label, IntVar, OptionMenu, Button
import tkMessageBox   
import Search 
from hugo.twitter import SendMessage

class TwitterSearcher(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")
        self.keyA = 1
        self.keyB = 1
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        "Text to enter the clear text"
        self.clearLabelFrame = LabelFrame(self.parent, text = "Search Text")
        self.clearLabelFrame.place(x = 65, y = 20)
        self.clearText = Text(self.clearLabelFrame, width = 65, height = 5)
        self.clearText.pack()
        
        "Button to encode"
        self.encodeButton = Button(self.parent, text = "Search", command = self.search)
        self.encodeButton.place(x = 460, y = 130)
        
        "Text to display encoded text"
        self.encodedLabelFrame = LabelFrame(self.parent, text = "Tweets")
        self.encodedLabelFrame.place(x = 65, y = 160)
        self.encodedText = Text(self.encodedLabelFrame, width = 65, height = 15)
        self.encodedText.pack()
        
        "Send tweet"
        self.clearLabelFrame = LabelFrame(self.parent, text = "Tweet")
        self.clearLabelFrame.place(x = 65, y = 400)
        self.sendTweet = Text(self.clearLabelFrame, width = 65, height = 5)
        self.sendTweet.pack()
        
        "Button to encode"
        self.encodeButton = Button(self.parent, text = "Send", command = self.send)
        self.encodeButton.place(x = 470, y = 500)
        
        
    def search(self):
        clear = self.clearText.get(1.0, Tkinter.END)
        rst = Search.search(clear)
        self.encodedText.delete(1.0, Tkinter.END)
        content = Search.jsonParser(rst)
        display = ""
        
        if (len(content) == 0):
            display = "Nothing" 
        else:
            for tweet in content:
                key = tweet.keys()[0]
                display +=  key + " said: \n" + "\t" + tweet.get(key) + "\n\n"
                
            checkReport = False
            for tweet in content:
                if(Search.insertMySQL(tweet)):
                    checkReport = True
            if(checkReport):
                tkMessageBox.showinfo("Insert to database", "Insert successfully" )
        
        self.encodedText.insert(1.0, display)
        
    def send(self):
        message = self.sendTweet.get(1.0, Tkinter.END)
        #print len(message)
        if(142> len(message)>1):
            SendMessage.send(message)
            tkMessageBox.showinfo("Send", "Send successfully")
        else:
            tkMessageBox.showinfo("Send", "No tweet to send, please enter your tweet")

def main():
    root = Tk()
    root.geometry("600x610+300+30")
    root.title("Twitter Search")
    app = TwitterSearcher(root)
    root.mainloop()

if __name__ == '__main__':
    main()