import pygame
import math
import time
import itertools

#pygame is initialisation
pygame.init()

#height and the width of the window is set
width = 1022
height = 766

#all the colours that I may need in the code
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
yellow = (255, 241, 13)
gray = (190,190,190)

gameDisplay = pygame.display.set_mode((width, height)) #make the display
pygame.display.set_caption("logic gates") #title of the window
clock = pygame.time.Clock()  #frames per second defined here

#variables
exitgame = False
gates = []
outputGateNumber = 0
truthTableInputs = []
truthTableTypes = []
tableHeaders = False
createPreSetDone = False
currentBoxPosition = -200
currentGateMoving = " "

#these two functions are used to write text onto the screen
def messageDisplay(text,x,y,size):
    large_text = pygame.font.Font("freesansbold.ttf", size)
    TextSurf , TextRect = textObjects(text, large_text)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def textObjects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

#this the function that lets the user move the gatess around the screen it is used inside each of the gate objects
def mouseMoving (x, y, mouseDown):  
    clickStatus = (pygame.mouse.get_pressed())[0]
    (xPos, yPos) = pygame.mouse.get_pos()               #this gets the mouse properites at the time the function is being run
    if mouseDown == False:
        if (x - 25) < xPos < (x + 25) and (y - 25) < yPos < (y + 25): #this checks to see if the mouse is in the correct position
            if clickStatus == 1:
                mouseDown = True
                return xPos, yPos ,mouseDown  #these lines of code then return the correct position to the gate for where it need to move to be inline with the mouse 
            else:
                return x, y ,mouseDown
        else:
            return x, y ,mouseDown
    elif mouseDown == True:
        if clickStatus == 1:
            return xPos, yPos,mouseDown
        else:
            mouseDown = False
            return x, y, mouseDown

#this is to allow the user to click on pre-set gate boxes, this is used so lots of x and y values can be checked
def buttonClick(x,y):
    #these variables work out the current staus of the mouse its postion and if it is clicked down
    clickStatus = (pygame.mouse.get_pressed())[0]
    (xPos, yPos) = pygame.mouse.get_pos()
    if (x) < xPos < (x + 150) and (y) < yPos < (y + 30):
        if clickStatus == 1:
    #it will return true if the mouse is clicked down in the corrent position
            return True

def gateClick(xStart, yStart,nmX):   #this allows the user to chnage the gates inputs
    (xPos, yPos) = pygame.mouse.get_pos()   #gets the mouse position
    if (xStart-20) < xPos < (xStart+20) and (yStart - 20) < yPos < (yStart + 20):  #this checks the the mouse is on the correct position
        if ((pygame.mouse.get_pressed())[0]) == 1: #this checks to see if the mouse is clicked down
            if nmX == 1:    #if and elif change the 1 to a 0 or a 0 to a 1 if both the if statements are true
                nmX = 0
            elif nmX == 0:
                nmX = 1
            time.sleep(0.075) # this is added so that when the user clicks the gates once the number only changes once
    return(nmX)  # this then returns the specific input number back to the function
            
#classes for each of the gates

class Not(object):   #this is the Not gate's (class)
    """not gate"""
    
    def __init__(self): # this iniatalises on startup so all the variables are initalised
        self.nm1 = 1
        self.nm2 = 1  # these are the input and output numbers
        self.nm1Connected = False
        self.nm2Connected = False #these are what parts of the gate are connected and if the whole gate is connected
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 80   #this is the x and y poition of the Not gate
        self.Not = pygame.image.load("not.png") # this is the variable that stores the picture of the gate
        self.mouseDown = False   #this is the variable that stores if the gate is currenly being moved
        
        #position of the input and ouput nodes at start
        self.xStart = self.x
        self.yStart = self.y+60
        
        self.xEnd = self.x+200
        self.yEnd = self.y+60
        
    #this places the gate on the screen and lets the user move the gate around the screen
    def position(self, currentGateMoving):     #currentGateMoving is used to save what gate the user is currently moving so the user cant move more than one gate at a time
        if currentGateMoving == "not" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(self.x, self.y, self.mouseDown) #lets the gate be moved if no other gates are being moved or it is already being moved
        if self.mouseDown == True:
            currentGateMoving = "not"
        elif (self.mouseDown == False) and (currentGateMoving == "not"):   #this validates what the current gate being moved is and if its not being moved or not
            currentGateMoving = " "
        gameDisplay.blit(self.Not ,(self.x,self.y))
        return currentGateMoving

    #this function sorts out the inputs and outputs and the position of the numbers
    def numbersatpoints(self):
        if self.nm1 == 1:
            self.nm2 = 0
        elif self.nm1 == 0:
            self.nm2 = 1

        #position of nodes thought out the code
        self.xStart = self.x
        self.yStart = self.y+60
        self.xEnd = self.x+200
        self.yEnd = self.y+60
        
        #this places the numbers at each of the points
        messageDisplay(str(self.nm1),self.xStart, self.yStart ,30)
        messageDisplay(str(self.nm2),self.xEnd, self.yEnd,30)

    # this function lets the user click on the input number to change it
    def click(self):
        self.nm1 = gateClick(self.xStart, self.yStart, self.nm1)
        
class And(object):  #this is the And gate's (class)
    """and gate"""
    def __init__(self):     # this iniatalises on startup so all the variables are initalised
        self.nm1 = 0    # these are the input and output numbers
        self.nm2 = 1
        self.nm3 = 0
        self.nm1Connected = False
        self.nm2Connected = False #these are what parts of the gate are connected and if the whole gate is connected
        self.nm3Connected = False
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 210    #this is the x and y poition of the And gate
        self.And = pygame.image.load("and.png") # this is the variable that stores the picture of the And gate
        self.mouseDown = False   #this is the variable that stores if the gate is currenly being moved
        
        #position of the input and ouput nodes at start
        self.x1Start = self.x
        self.y1Start = self.y + 30   #there are two Starts as the And gate has two inputs 

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y +60

    #this places the gate on the screen and lets the user move the gate around the screen
    def position(self, currentGateMoving): #currentGateMoving is used to save what gate the user is currently moving so the user cant move more than one gate at a time
        if currentGateMoving == "and" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(self.x, self.y, self.mouseDown)#lets the gate be moved if no other gates are being moved or it is already being moved
        if self.mouseDown == True:
            currentGateMoving = "and"
        elif (self.mouseDown == False) and (currentGateMoving == "and"):#this validates what the current gate being moved is And if its not being moved or not
            currentGateMoving = " "   #currentGateMoving is set to " " if the gate is no longer being moved around
        gameDisplay.blit(self.And ,(self.x,self.y))
        return currentGateMoving

    #this function sorts out the inputs and outputs and the position of the numbers
    def numbersatpoints(self):
        if self.nm1 == 1 and self.nm2 == 1:
            self.nm3 = 1
        else:
            self.nm3 = 0

        #position of the nodes through out the code
        self.x1Start = self.x
        self.y1Start = self.y + 30 
        self.x2Start = self.x
        self.y2Start = self.y + 190 
        self.xEnd = self.x + 200
        self.yEnd = self.y +60

        #this places the numbers at each of the points
        messageDisplay(str(self.nm1),self.x1Start, self.y1Start ,30)
        messageDisplay(str(self.nm2),self.x2Start, self.y2Start,30)
        messageDisplay(str(self.nm3),self.xEnd, self.yEnd ,30)

    # this function lets the user click on the input number to change it
    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)

class Or(object):  #this is the Or gate's (class)
    """or gate"""
    
    def __init__(self): # this iniatalises on startup so all the variables are initalised
        self.nm1 = 0
        self.nm2 = 1    # these are the input and output numbers for the nodes
        self.nm3 = 1
        self.nm1Connected = False
        self.nm2Connected = False  #these are what parts of the gate are connected and if the whole gate is connected
        self.nm3Connected = False  #they turn true to show when they are connected
        self.connected = False
        self.output = False
        self.x = 30  #this is the x and y poition of the Or gate
        self.y = 410
        self.Or = pygame.image.load("or.png")  # this is the variable that stores the picture of the And gate
        self.mouseDown = False   #this is the variable that stores if the gate is currenly being moved
        
        #position of the input and ouput nodes at initalisation
        self.x1Start = self.x
        self.y1Start = self.y + 30

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y +60

    #this places the gate on the screen and lets the user move the gate around the screen
    def position(self, currentGateMoving):  #currentGateMoving is used to save what gate the user is currently moving so the user cant move more than one gate at a time
        if currentGateMoving == "or" or currentGateMoving == " ":  #lets the gate be moved if no other gates are being moved or it is already being moved
            self.x, self.y, self.mouseDown = mouseMoving(self.x, self.y, self.mouseDown)
        if self.mouseDown == True:
            currentGateMoving = "or"
        elif (self.mouseDown == False) and (currentGateMoving == "or"): #this validates what the current gate being moved is Or if its not being moved or not
            currentGateMoving = " "   #currentGateMoving is set to " " if the gate is no longer being moved around
        gameDisplay.blit(self.Or ,(self.x,self.y))
        return currentGateMoving

    #this function sorts out the inputs and outputs and the position of the numbers
    def numbersatpoints(self):
        if self.nm1 == 1 or self.nm2 == 1:
            self.nm3 = 1
        else:
            self.nm3 = 0

        #position of the nodes through out the code
        self.x1Start = self.x 
        self.y1Start = self.y + 30
        self.x2Start = self.x
        self.y2Start = self.y + 155 
        self.xEnd = self.x + 200
        self.yEnd = self.y +60

        #this places the numbers at each of the points
        messageDisplay(str(self.nm1),self.x1Start, self.y1Start ,30)
        messageDisplay(str(self.nm2),self.x2Start, self.y2Start,30)
        messageDisplay(str(self.nm3),self.xEnd, self.yEnd ,30)

    # this function lets the user click on the input number to change it
    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)

class Xor(object):  #this is the Xor gate's (class)
    """xor gate"""
    def __init__(self):  # this iniatalises on startup so all the variables are initalised
        self.nm1 = 0
        self.nm2 = 1   # these are the input and output numbers for the nodes
        self.nm3 = 1
        self.nm1Connected = False
        self.nm2Connected = False   #these are what parts of the gate are connected and if the whole gate is connected
        self.nm3Connected = False   #they turn true to show when they are connected
        self.connected = False
        self.output = False
        self.x = 30   #this is the x and y poition of the Xor gate
        self.y = 580
        self.Xor = pygame.image.load("xor.png")  # this is the variable that stores the picture of the And gate
        self.mouseDown = False  #this is the variable that stores if the gate is currenly being moved
        
        #position of the input and output nodes at intalisation
        self.x1Start = self.x
        self.y1Start = self.y + 30

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y +60

    #this places the gate on the screen and lets the user move the gate around the screen
    def position(self, currentGateMoving):  #currentGateMoving is used to save what gate the user is currently moving so the user cant move more than one gate at a time
        if currentGateMoving == "xor" or currentGateMoving == " ": #lets the gate be moved if no other gates are being moved or it is already being moved
            self.x, self.y, self.mouseDown = mouseMoving(self.x, self.y, self.mouseDown)
        if self.mouseDown == True:
            currentGateMoving = "xor"
        elif (self.mouseDown == False) and (currentGateMoving == "xor"):  #this validates what the current gate being moved is Or if its not being moved or not
            currentGateMoving = " "  #currentGateMoving is set to " " if the gate is no longer being moved around
        gameDisplay.blit(self.Xor ,(self.x,self.y))
        return currentGateMoving

    #this function sorts out the inputs and outputs and the position of the numbers
    def numbersatpoints(self):
        if self.nm1 == 1 or self.nm2 == 1:
            self.nm3 = 1
            if self.nm1 == 1 and self.nm2 == 1:
                self.nm3 = 0
        else:
            self.nm3 = 0

        #position of the nodes throughout the code
        self.x1Start = self.x 
        self.y1Start = self.y + 30
        self.x2Start = self.x
        self.y2Start = self.y + 130 #changed from + 30!!!
        self.xEnd = self.x + 200
        self.yEnd = self.y +60

        #this places the numbers at each of the points
        messageDisplay(str(self.nm1),self.x1Start, self.y1Start ,30)
        messageDisplay(str(self.nm2),self.x2Start, self.y2Start,30)
        messageDisplay(str(self.nm3),self.xEnd, self.yEnd ,30)

    # this function lets the user click on the input number to change it
    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)

#gate1 effects changes gate2
#two gates are passed through the function using two for loops
def connectionCheck(gate1, gate2):
    #when there are two not gates that have been connected
    if gate1.__class__.__name__ == "Not" and gate2.__class__.__name__ == "Not":
        if gate2.xStart-10 < gate1.xEnd < gate2.xStart +10 and gate2.yStart-10 < gate1.yEnd < gate2.yStart+10:
            gate2.nm1 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm1Connected = True
            #this works out the difference in x value and y values works with the first and only node on the Not gate
            xDifference = gate1.xEnd - gate2.xStart
            yDifference = gate1.yEnd - gate2.yStart
            #the differnce is added to the second gate so that it moves the stay connected to the first gate
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
            #to disconnect the gates the user drags it faster than 20 pixels in 1/60 of a second so the gates are no longer in range of each other
    #the not gate is changing the other gates
    elif gate1.__class__.__name__ == "Not":
        #not changing others
        if gate2.x1Start-10 < gate1.xEnd < gate2.x1Start +10 and gate2.y1Start-10 < gate1.yEnd < gate2.y1Start+10:
            gate2.nm1 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm1Connected = True
            #this is the same connection code as above but with the first node on the second gate
            xDifference = gate1.xEnd - gate2.x1Start
            yDifference = gate1.yEnd - gate2.y1Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
        if gate2.x2Start-10 < gate1.xEnd < gate2.x2Start +10 and gate2.y2Start-10 < gate1.yEnd < gate2.y2Start+10:
            gate2.nm2 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm2Connected = True
            #this is the same connection code as above but with the 2nd node as it is x2Start and y2Start
            xDifference = gate1.xEnd - gate2.x2Start
            yDifference = gate1.yEnd - gate2.y2Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    #this is where the not gate is being changed by other gates
    elif gate2.__class__.__name__ == "Not":
        if gate2.xStart-10 < gate1.xEnd < gate2.xStart +10 and gate2.yStart-10 < gate1.yEnd < gate2.yStart+10:
            gate2.nm1 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm1Connected = True
            #this is the same code as above but with the first node
            xDifference = gate1.xEnd - gate2.xStart
            yDifference = gate1.yEnd - gate2.yStart
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    #this is where there are no not gates involved
    else:
        if gate2.x1Start-10 < gate1.xEnd < gate2.x1Start +10 and gate2.y1Start-10 < gate1.yEnd < gate2.y1Start+10:
            gate2.nm1 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm1Connected = True
            #this is the same code as above but with the first node
            xDifference = gate1.xEnd - gate2.x1Start
            yDifference = gate1.yEnd - gate2.y1Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
        if gate2.x2Start-10 < gate1.xEnd < gate2.x2Start +10 and gate2.y2Start-10 < gate1.yEnd < gate2.y2Start+10:
            gate2.nm2 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm2Connected = True
            #this the same code as above but with the second node 
            xDifference = gate1.xEnd - gate2.x2Start
            yDifference = gate1.yEnd - gate2.y2Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    #this then returns the gate back to the code so any chnages are saved
    return(gate1, gate2)

#this is the function that works out the output number it does this by using x values of the gates that are connected
def outputNumberRight(gates, outputGateNumber):
    #currentBiggestX is the current value of x that is the biggest
    currentBiggestX = 0
    #the for loop goes through all the gates and the compares there x values of the output of the gate
    for gate in gates:
        if gate.connected == True:
            if gate.xEnd > currentBiggestX:
                currentBiggestX = gate.xEnd
                if gate.__class__.__name__ == "Not":
                    outputGateNumber = gate.nm2
                    #the gate will then have its output attribute set to true when it is the output number
                    gate.output = True
                else:
                    outputGateNumber = gate.nm3
                    gate.output = True
    return gates, outputGateNumber

#this is how the truth table is created
def tableCreation(gates, truthTableInputs, truthTableTypes):
    #this sets the truthtableinputs and truthtabletypes to empty
    truthTableInputs = []
    truthTableTypes = []
    #this list stores all the letters of the alphabet so they can be used on the headers of the truth table
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabetCount = 0   #this stores the current position in the array that the program is in
    tempGates = [] #this is where the connected gate are temporary stored while the truth table is being created
    #this loop creates an array of all the connected gates and stores they in array then orders them
    for i in gates:
        if i.connected == True:
            tempGates.append(i)
    tempGates = gateOrdering(tempGates) #changed
    #this main for loop then goes through the array of connected gates and creates a truth table
    for i in tempGates:
        #these if statements then check if each node is connected and if it not then it is added to the truth table
        if i.nm1Connected == False:
            truthTableInputs.append(i.nm1)
            truthTableTypes.append(alphabet[alphabetCount])
            alphabetCount = alphabetCount + 1
        #when an item is added to the truth table the next letter is added and the value of the node either a 1 or a 0
        if i.nm2Connected == False:
            if not(i.output == True and i.__class__.__name__ == "Not"):
                truthTableInputs.append(i.nm2)
                truthTableTypes.append(alphabet[alphabetCount])
                alphabetCount = alphabetCount + 1
        if not(i.__class__.__name__ == "Not"):
            if i.nm3Connected == False:
                if not(i.output == True):
                    truthTableInputs.append(i.nm3)
                    truthTableTypes.append(alphabet[alphabetCount])
                    alphabetCount = alphabetCount + 1
    #the truthTableInputs and truthTableTypes are then returned so that they can be printed on the screen or added to a file (shown below)
    return truthTableInputs, truthTableTypes

#this function is used to delete all the data out of a file this is used in the truth table creation algorithm
def deleteFile(file):
    file.seek(0)
    file.truncate()

#this function resets all the gates so that they are all in the correct positions 
def gatesReset(gates):
    #this function will be activated when a button is pressed so will be run as part of the main loop
    gates[0].x = 30
    gates[0].y = 210
    gates[1].x = 30
    gates[1].y = 410
    gates[2].x = 30
    gates[2].y = 80
    gates[3].x = 30
    gates[3].y = 580
    for i in range(len(gates))[4::]:   #places the extra gates off the screen
        gates[i].x = -300
        gates[i].y = 1000

#this is the preSetGates algorithm
def preSetGates(gates):
    #the preset gate file is read and then the number of lines is worked out and the number of boxes for that file is put on the screen
    num_lines = sum(1 for line in open("Pre-set.txt"))
    preMadeGates = open("Pre-set.txt", "r+")
    boxPosition = 20
    currentLineNumber = 0
    allLines = preMadeGates.readlines()
    lineNumber = 0
    andCount = 0
    orCount = 0
    notCount = 0 
    xorCount = 0
    global currentBoxPosition
    #this fills in the box that is currently being use in gray
    pygame.draw.rect(gameDisplay, gray, (320,currentBoxPosition,150,30), 0) #rect is used with (display to add it to, colour, (x,y,x size, y size) , width=0 means filled)
    #this for loop goes through each line in the text file
    for i in range(num_lines):
        #this draws the box at the correct position on the screen 
        pygame.draw.rect(gameDisplay, black, (320,boxPosition,150,30), 4)
        #this spits up all the text on one line and puts it into an array for fasteer/easier access
        currentLineSplitted = allLines[lineNumber].split()
        #this then diplays the name of the gate in the box that is on the screen
        messageDisplay(str(currentLineSplitted[0]),390,boxPosition+15 ,19)
        
        #this checks if the box has been clicked 
        if buttonClick(320,boxPosition) == True:
            currentBoxPosition = boxPosition
            positionInLine = 1
            #this makes sure there are enough gates to create any pre-set gate
            gates.append(And())
            gates.append(Or())
            gates.append(Not())
            gates.append(Xor())
            #this reset make sure that all the gates are off the screen when this pre-set is created
            gatesReset(gates)

            #this loops goes through the line that has been splitted from the file 
            for gate in currentLineSplitted[1::3]:
                #this if statement checks for both capitalised and non capitalised so that both the user pre-set works and the already sets circuits work
                if gate == "and" or gate == "And":
                    #this then places the gates at the correct part of the screen that has been specified in the file
                    gates[andCount].x = int(currentLineSplitted[positionInLine+1])
                    gates[andCount].y = int(currentLineSplitted[positionInLine+2])
                    #this then counts up to tell how many of the and gates have been already places on the screen so gates already places dont get moved again
                    andCount = andCount + 4
                if gate == "or" or gate == "Or":
                    gates[orCount + 1].x = int(currentLineSplitted[positionInLine+1])
                    gates[orCount + 1].y = int(currentLineSplitted[positionInLine+2])
                    orCount = orCount + 4
                if gate == "not" or gate == "Not":
                    gates[notCount + 2].x = int(currentLineSplitted[positionInLine+1])
                    gates[notCount + 2].y = int(currentLineSplitted[positionInLine+2])
                    notCount = notCount + 4
                if gate == "xor" or gate == "Xor":
                    gates[xorCount + 3].x = int(currentLineSplitted[positionInLine+1])
                    gates[xorCount + 3].y = int(currentLineSplitted[positionInLine+2])
                    xorCount = xorCount + 4
                #this counts up the current position in the line
                positionInLine = positionInLine + 3

        #this lets the user right click on the gate to delete it
        #this checks to see if the right mouse button is clicked down 
        if (pygame.mouse.get_pressed())[2] == 1:
            (xPos, yPos) = pygame.mouse.get_pos()
            #this checks to see if the user is in the correct position
            if (320) < xPos < (470) and (boxPosition) < yPos < (boxPosition + 30):
                #this reads the file then adds the lines in the file to an array
                file = open("Pre-set.txt", "r+")
                lines = file.readlines()
                print(lines)
                print(lineNumber)
                #this then removes the correct line from the array 
                lines.pop(lineNumber)
                #the file is then cleared
                deleteFile(file)
                #then the items are added back into the file
                for item in lines:
                    file.write(item)
                #when the deleting is does the fucntion is stopped using return to stop any errors from happening
                return
        #this then incements the box number and its y postion on the screen as each box is 30 px high
        boxPosition = boxPosition + 30
        lineNumber = lineNumber + 1
    #this cuts of the end of the gates to prevent there being too many gates being added to the file
    if len(gates) > 7:
        gates = gates[0:8]

#this function lets the user add there own pre-sets to the pre-sets file
def createPreSet(gates):
    #this opens the file with the abilty to write into without damage to the file
    truthtable = open("Pre-set.txt","a")
    count = 0
    #this stops the user adding more than two types of the same gate as a pre-set
    if len(gates) > 8:
        gates = gates[0:8]
        gameDisplay.fill(white)
        #this is where the error is displayed that tells the user that cannot have more than two of the same type of gate in the same circuit
        messageDisplay("you can't have more than 2 gates of the same type being added into the pre-sets", 500, 300, 25)
        pygame.display.update()
        time.sleep(1.5)
        #if the user does this the function is ended as to not carry on with the rest of the code
        return gates
    #this works out the number of connected gates 
    for gate in gates:
        if gate.connected == True:
            count = count + 1
    #this makes sure that there is more than one connected gate
    if count < 2:
        messageDisplay("you have to have 2 or more gates connected", 600, 300, 25)
        pygame.display.update()
        time.sleep(1.5)
        #if there is not enough connected gates then the function will exit and report an on screen error to the user
        return gates
    #this adds the name of the pre-set to the file
    truthtable.write("user_Pre-set")
    #this then adds the position and the name of the gates in there current positions to the file then adds a line in for the next pre-set and exits
    for gate in gates:
        if gate.connected == True:
            truthtable.write(" " + gate.__class__.__name__ + " " + str(gate.x) + " " + str(gate.y))
    truthtable.write("\n")
    return gates

#this is how the gates are ordered in the program this uses a merge sort to sort them this is the most simple sorting function
def gateOrdering(gates):
    for i in range(len(gates)):
        for j in range(len(gates)-1-i):
            if gates[j].x > gates[j+1].x:
                gates[j], gates[j+1] = gates[j+1], gates[j]
    return gates

#this is the function that creates the help screen
def helpScreen():
    #these are all the statements that create the polygon of the arrow
    #gates arrow
    pygame.draw.polygon(gameDisplay, gray, ((330, 600), (400, 500), (400, 570), (530, 570), (530, 630), (400, 630), (400, 700)))
    #truth table
    pygame.draw.polygon(gameDisplay, gray, ((770, 100), (830, 170), (790, 170), (790, 300), (750, 300), (750, 170), (710, 170)))
    #pre-set gates
    pygame.draw.polygon(gameDisplay, gray, ((400, 130), (460, 200), (420, 200), (420, 385), (380, 385), (380, 200), (340, 200)))
    #gates arrow text
    messageDisplay("This is where the gates are stored",755,580,15)
    messageDisplay("click and hold on the top corner to move them",755,600,15)
    messageDisplay("click on the input number to change that number",755,620,15)
    messageDisplay("press R to reset and M to create more gates",755,640,15)
    messageDisplay("M will only work if you have moved all the gates out of the starting area",755,660,15)
    #truth table text
    messageDisplay("This is where the truth table will be displayed",755,315,15)
    messageDisplay("when at least two gates are connected",755,335,15)
    messageDisplay("press c to create a complete truth table in a file called truthTable",755,355,15)
    messageDisplay("to create it you have to exit the program for it to save to the file",755,375,15)
    #pre-set arrow text
    messageDisplay("This is where the pre-set gates are",460,400,15)
    messageDisplay("you can left click on the gates to select them",460,420,15)
    messageDisplay("right click to remove them and press x to create your own",460,440,15)

#class initalisation
gates.append(And())
gates.append(Or())
gates.append(Not())
gates.append(Xor())

#main loop
while not (exitgame):
    #this adds the fill into the baclground for the first time
    gameDisplay.fill(white)
    #this adds the line to devide the gates from the main screen
    pygame.draw.line(gameDisplay, black, (250,0),(250,800), 8)
    #this is where the pre-set gates are run
    preSetGates(gates)
    #this is where all the gates methods are run so that they are able to function properly
    for gate in gates:
        currentGateMoving = gate.position(currentGateMoving)
        gate.numbersatpoints()
        gate.click()

    #this is where the connection between each of the gates is checked this will run for every single gate that is on the screen
    for firstGate in gates:
        for secondGate in gates:
            firstGate, secondGate = connectionCheck(firstGate, secondGate)

    #this function call is used to work out the current output value 
    gates, outputGateNumber = outputNumberRight(gates, outputGateNumber)

    #this will work out is an entire gate is connected or not
    for gate in gates:
        #goes through all the gates to check
        if gate.__class__.__name__ == "Not":
            if gate.nm1Connected == True or gate.nm2Connected == True:
                gate.connected = True
            else:
                gate.connected = False
        else:
            if gate.nm1Connected == True or gate.nm2Connected == True or gate.nm3Connected == True:
                gate.connected = True
            else:
                gate.connected = False

    #number of outputs is reset from what it may have been from the previous loop
    numberOfOutputs = 0
    #this goes through all the gates and if the gates output if not connected to anything then numberofoutputs is incremented
    #this bit of code is run to check how many circuits there are this is done by working out the number of outputs there are
    for gate in gates:
        if gate.connected == True:
            if gate.__class__.__name__ == "Not":
                #this statement checks to see if the gates output is connected
                if gate.nm2Connected == False:
                    numberOfOutputs = numberOfOutputs + 1
            else:
                if gate.nm3Connected == False:
                    numberOfOutputs = numberOfOutputs + 1

    #this takes the events that are happening in pygame and applies them to the if statements that are below
    for event in pygame.event.get():
        #this if statement checks to see if the quit button is clicked and if it is pygame is quit then python is quit
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #this statment checks to see if there has been a keypress
        if event.type == pygame.KEYDOWN:
            #when the letter r is pressed then gatesReset function is run
            if event.key == pygame.K_r:
                gatesReset(gates)
        if event.type == pygame.KEYDOWN:
            #when the m button is pressed then the positon of the current gates aere checked this will make sure gates are not places on the top of each other
            if event.key == pygame.K_m:
                #this stores if there are any gates that are on the top of each other
                gateSamePlace = 0
                #this for loop the goes through all the gates as they are in order at this time the for loop goes through 4 at a time
                for i in range(len(gates))[::4]:
                    #these if statements check to see if the gates have been moved from the original position
                    if not(gates[i].x == 30 and gates[i].y == 210):
                        if not(gates[i+1].x == 30 and gates[i+1].y == 410):
                            if not(gates[i+2].x == 30 and gates[i+2].y == 80):
                                if not(gates[i+3].x == 30 and gates[i+3].y == 580):
                                    #this is incremented by one if all the gates are out of the starting positions
                                    gateSamePlace = gateSamePlace + 1
                #this will only run when all the gates are out of there starting positions even if the user has created more gates
                if gateSamePlace >= (len(gates))/4:
                    gates.append(And())
                    gates.append(Or())
                    gates.append(Not())
                    gates.append(Xor())
        if event.type == pygame.KEYDOWN:
                    #when the x button is pressed then the user-preset gate is added to the file that contains all the preset gates
                    if event.key == pygame.K_x:
                        #the if statement checks that the user can only add one preset gate pre time of running the program
                        if (not(createPreSetDone) == True) and (numberOfOutputs == 1):
                            gates = createPreSet(gates)
                            createPreSetDone = True
        if event.type == pygame.KEYDOWN:
                            #when the c button is pressed 
                            if event.key == pygame.K_c:
                                #this makes sure that there is only one logic circuit on the screen at this time
                                if numberOfOutputs == 1:
                                    #this is where most of the variables are set such as the file that the truth table is going to be saved to
                                    truthtable = open("truthTable.txt","w")
                                    totalinputs = 0
                                    inputsArray = []
                                    inputstypeArray = []
                                    #this is where the contents of the truth table file is deleted
                                    deleteFile(truthtable)
                                    #this for loop goes through and then creates and array of all the conencted gates and the inputs on the logic circuit
                                    for i in gates:
                                        if i.connected == True:
                                            if i.__class__.__name__ == "Not":
                                                i.nm1 = 0
                                                i.nm2 = 0
                                                if i.nm1Connected == False:
                                                    inputsArray.append(i)
                                                    inputstypeArray.append(1)
                                            else:
                                                i.nm1 = 0
                                                i.nm2 = 0
                                                i.nm3 = 0
                                                if i.nm1Connected == False:
                                                    inputsArray.append(i)
                                                    inputstypeArray.append(1)
                                                if i.nm2Connected == False:
                                                    inputsArray.append(i)
                                                    inputstypeArray.append(2)
                                    #this creates all the possable options for a truth table using itertools libary 
                                    pretruthtable = list(itertools.product([0, 1], repeat=(len(inputsArray))))
                                    #this for loop assigns the values from the pretruthtable to the inputs on the truth table
                                    for i in range(len(pretruthtable)):
                                        for leninputarray in range(len(inputsArray)):
                                            if inputstypeArray[leninputarray] == 1:
                                                inputsArray[leninputarray].nm1 = pretruthtable[i][leninputarray]
                                            if inputstypeArray[leninputarray] == 2:
                                                inputsArray[leninputarray].nm2 = pretruthtable[i][leninputarray]

                                        #this is where the inputs are taken and the gates are able to work out the output values
                                        gameDisplay.fill(white)
                                        for gate in gates:
                                            currentGateMoving = gate.position(currentGateMoving)
                                            gate.numbersatpoints()
                                            gate.click()
                                            pygame.display.update()

                                        #here the connections between all the gates are checked so that the connections will be true
                                        for firstGate in gates:
                                            for secondGate in gates:
                                                firstGate, secondGate = connectionCheck(firstGate, secondGate)

                                        #this then works out the outputs of the gates as some of them may have been changed from the connectionCheck
                                        gameDisplay.fill(white)
                                        for gate in gates:
                                            currentGateMoving = gate.position(currentGateMoving)
                                            gate.numbersatpoints()
                                            gate.click()
                                            pygame.display.update()
                                        #this adds a pause between each change of the input values this lets the user see what is happening 
                                        clock.tick(5) 
                                        pygame.display.update()

                                        #this is where the truth table is created and then it is saved into the file this uses the tablCreation algorythm
                                        truthTableInputs, truthTableTypes = tableCreation(gates, truthTableInputs, truthTableTypes)
                                        gates, outputGateNumber = outputNumberRight(gates, outputGateNumber)
                                        print(truthTableTypes)
                                        print(truthTableInputs , "  //   Q:" , outputGateNumber)
                                        if tableHeaders  == False:
                                            for item in truthTableTypes:
                                                truthtable.write((str(item))+ "    ,    ")
                                            tableHeaders  = True
                                        truthtable.write("\n")
                                        for item in truthTableInputs:
                                            truthtable.write(str(item) + "    ,    ")
                                        truthtable.write("      Q: " + str(outputGateNumber))
                                        truthtable.write("\n")

                                #this is where the errors will be thrown up if the user does not have one logic circuit it will be displayed on the screen for around 3.5 seconds
                                else:
                                    if numberOfOutputs > 1:
                                        gameDisplay.fill(white)
                                        messageDisplay("you can only have one circuit at a time when creating a truth table", 511,300,20)
                                        pygame.display.update()
                                        time.sleep(3.5)
                                    elif numberOfOutputs < 1:
                                        gameDisplay.fill(white)
                                        messageDisplay("you need to have at least one logic circuit to create a truth table", 511,300,20)
                                        pygame.display.update()
                                        time.sleep(3.5)
                                            
    #this is where the truth table is created the values that the function needs are passed into the function
    truthTableInputs, truthTableTypes = tableCreation(gates, truthTableInputs ,truthTableTypes)
    #this is where the validation is done so that the truth table will only be displayed if there is one logic circuit
    if numberOfOutputs == 1:
        #these lines of code just display the table headers then the numbers at the inputs then the output
        messageDisplay((str(truthTableInputs)),770, 60,20)
        messageDisplay((" Q: " + str(outputGateNumber)),770, 80,20)
        messageDisplay(str(truthTableTypes),770, 40,20)
    else:
        #this will be dsiplayed if there are the correct number of logic circuits 
        messageDisplay("too many circuits or too few",770, 60,20)

    pygame.draw.rect(gameDisplay, red, (860,723,150,30), 0)
    messageDisplay("HELP",935,740,30)
    if buttonClick(860,723) == True:
        helpScreen()
    
    #this changes all the parts of gates to not connected so that they can be updated in the next tick of the gate
    for i in gates:
        if i.__class__.__name__ == "Not":
            i.nm1Connected = False
            i.nm2Connected = False
        else:
            i.nm1Connected = False
            i.nm2Connected = False
            i.nm3Connected = False
        i.output = False

    #this then resets any of the values that need to be reset
    outputGateNumber = 0
    truthTableInputs = []
    truthTableTypes = []

    #this is where the fps is defiend and the display is updated
    pygame.display.update()
    clock.tick(60)
