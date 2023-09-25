#pyintsaller main.py --onefile
import math 
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def solver(event,x,y):
    global rows
    global columns
    global difficulty
    global revealed
    global tiles
    global buttons
    global finished
    global unsolvable
    global finishedGame
    
    if(finishedGame):
        return
    
    print("solve " + str(x) + ',' + str(y))
    
    index = x*rows+y
    
    valid_neighbours = validNeighbours(x,y)
    maxNeighbours = len(valid_neighbours)
    
    
    #if [x,y] in unsolvable:
        #AS IS
        #do nothing. the function ends here. the unsolvable cells need to be addressed later.
        #print("cell in unsolvable")
        #pass
        
        #TO BE
        #test if the cell is still unsolvable 
        #if yes do nothing
        #else, remove from unsolvable array and solve cell

        
    if not([x,y] in finished) and not([x,y] in flags):
        #reveal the cell
        buttons[index].config(bg="white")
        if not([x,y] in revealed) and not([x,y] in unsolvable):
            reveal(event,x,y,index)
        
        cellValue = int(tiles[x][y])
    
        revealed_neighbours = []
        flagged_neighbours = []
        unknown_neighbours = []
        
        
        for i in range(maxNeighbours):
            n = valid_neighbours[i].split(',')
            a = int(n[0])
            b = int(n[1])
        
            if([a,b] in revealed):
                revealed_neighbours.append([a,b])
            elif([a,b] in flags):
                flagged_neighbours.append([a,b])
            else:
                unknown_neighbours.append([a,b])
        
        r_neighbours = len(revealed_neighbours)
        f_neighbours = len(flagged_neighbours)
        u_neighbours = len(unknown_neighbours)
        
        if(f_neighbours==cellValue):
            #all bombs have been flagged so its safe to reveal all other neighboring cells
            finished.append([x,y])
            if [x,y] in unsolvable:
                unsolvable.remove([x,y])
            
            revealNeighbours(event,x,y)
            solveNeighbours(event,x,y)
            
        
        elif((f_neighbours+u_neighbours)==cellValue):
            #the remaining bombs are in the unknows cells. flag those cells

            finished.append([x,y])
            
            if [x,y] in unsolvable:
                unsolvable.remove([x,y])
            
            for i in range(u_neighbours):
                a = int(unknown_neighbours[i][0])
                b = int(unknown_neighbours[i][1])
                index = a*rows+b
                flagged_neighbours.append([a,b])
                flagClick(event,a,b,index)

            solveNeighbours(event,x,y)
            
            
            
        else:
            print("Can't solve this cell! Adding to unsolvable!")
            if not([x,y] in unsolvable):
                unsolvable.append([x,y])
            chooseNewCell(event)

    else:
        #the cell is solved
        print("Solved cell!")
        chooseNewCell(event)
        

def chooseNewCell(event):
    global revealed
    global unsolvable
    global flags
    global finished

    newCell = False

    #chose a cell that is revealed but not unsolvable
    for i in range(len(revealed)):
        a = int(revealed[i][0])
        b = int(revealed[i][1])

        if not([a,b] in unsolvable) and not([a,b] in flags) and not([a,b] in finished):
            newCell = True
            solver(event,a,b)
            break


    #if no cell exists, chose a random new cell
    if(not newCell):
        print('choosing random cell')
        while(not newCell):
            r1 = random.randint(0,rows-1)
            r2 = random.randint(0,columns-1)

            if not([r1,r2] in revealed):
                newCell = True
                solver(event,r1,r2)

'''
def deadEnd():
    deadEnd = True
    
    for i in range(len(revealed)):
        if not((revealed[i] in finished) or (revelead[i] in unsolvable)):
            deadEnd = False
            
    return deadEnd    
'''

def revealNeighbours(event,i,j):
    global rows
    global revealed
    global flags
     
    valid_neighbours = validNeighbours(i,j)
    newNeighbors = False
    
    for k in range(len(valid_neighbours)):
        n = valid_neighbours[k].split(',')
        a = int(n[0])
        b = int(n[1])
        index = a*rows+b
        
        if not([a,b] in revealed) and not([a,b] in flags):
            reveal(event,a,b,index)
            newNeighbors = True

    #since new neighbors have been revealed, the cell "solvability" needs to be reevaluated
    if newNeighbors and [i,j] in unsolvable:
        unsolvable.remove([i,j])


def solveNeighbours(event,i,j):
    global rows
    global revealed
    global flags
     
    valid_neighbours = validNeighbours(i,j)
    
    for k in range(len(valid_neighbours)):
        n = valid_neighbours[k].split(',')
        a = int(n[0])
        b = int(n[1])
        
        if [a,b] in revealed and not([a,b] in unsolvable) and not([a,b] in finished) and not([a,b] in flags):
            print("Solve neighbour:" + n[0] + ',' + n[1])
            solver(event,a,b)





rows = 0
columns = 0
bombs = 0
difficulty = 0

flags = []

tiles = []

buttons = []
revealed = []
finished = []

unsolvable = []

finishedGame = False


def isFinished(x,y):
    global revealed
    global flags
    
    valid_neighbours = validNeighbours(x,y)
    maxNeighbours = len(valid_neighbours)
    
    count = 0
        
    for i in range(maxNeighbours):
        n = valid_neighbours[i].split(',')
        a = int(n[0])
        b = int(n[1])
        
        if ([a,b] in revealed) or ([a,b] in flags):
            count += 1
                
    return count == maxNeighbours


def validNeighbours(i,j):
    global rows
    global columns

    neighbours = []

    if(i>=0 and j>=0):
        neighbours.append(str(i-1)+','+str(j-1))
        neighbours.append(str(i-1)+','+str(j))
        neighbours.append(str(i-1)+','+str(j+1))
        neighbours.append(str(i)+','+str(j-1))
        neighbours.append(str(i)+','+str(j))
        neighbours.append(str(i)+','+str(j+1))
        neighbours.append(str(i+1)+','+str(j-1))
        neighbours.append(str(i+1)+','+str(j))
        neighbours.append(str(i+1)+','+str(j+1))

        neighbours[4] = ''

        if(i==0):
            neighbours[0] = ''
            neighbours[1] = ''
            neighbours[2] = ''

        if(j==0):
            neighbours[0] = ''
            neighbours[3] = ''
            neighbours[6] = ''

        if(i==rows-1):
            neighbours[6] = ''
            neighbours[7] = ''
            neighbours[8] = ''

        if(j==columns-1):
            neighbours[2] = ''
            neighbours[5] = ''
            neighbours[8] = ''
            
    valid_neighbours = [x for x in neighbours if x != '']
    
    
    return valid_neighbours



def flagClick(event,x,y,index):
    global revealed 
    global flags
    global buttons
    
    
    #every cell with a flag is a suspect to have a bomb therefore it is never revealed. 
    #the following if statement toggles the flag icon and prevents a revealed cell with a number to be overwritten
    #also, when a flag gets added, the unsolvable cells get removed from the unsolvable array

    if not([x,y] in revealed) and not([x,y] in flags):
        flags.append([x,y])
        buttons[index].config(fg="red")
        buttons[index].config(text="🚩")
        youWin()

        #since a new flag has been placed, the neighboring cells "solvability" needs to be reevaluated
        valid_neighbours = validNeighbours(x,y)
    
        for k in range(len(valid_neighbours)):
            n = valid_neighbours[k].split(',')
            a = int(n[0])
            b = int(n[1])
        
            if [a,b] in unsolvable:
                unsolvable.remove([a,b])


    elif not([x,y] in revealed) and [x,y] in flags:
        flags.remove([x,y]) 
        buttons[index].config(text='')
        buttons[index].config(fg="#e9e9e9")
    else:
        pass



def reveal(event,x,y,index):
    global tiles
    global buttons
    global revealed
    global finished
    global finishedGame
    
    print("reveal " + str(x) + ',' + str(y))
    cellValue = tiles[x][y] 

    #prevents the callbacks from the previous game to call in the new game
    if(finishedGame):
        return

    if [x,y] in unsolvable:
        unsolvable.remove([x,y])
    
    if cellValue == 'X':
        buttons[index].config(bg="red")
        buttons[index].config(fg="black")
        buttons[index].config(text="💣")
        showAllBombs(event)
        youLost()
    else:
        revealed.append([x,y])
        buttons[index].config(text=cellValue)
        buttons[index].config(relief="raised")
        
        if cellValue == '0':
            finished.append([x,y])
            buttons[index].config(relief="ridge")
            buttons[index].config(text='')
            buttons[index].config(fg="#e9e9e9")
            revealNeighbours(event,x,y)
            youWin()
        elif cellValue == '1':
            buttons[index].config(fg="blue")
        elif cellValue == '2':
            buttons[index].config(fg="green")
        elif cellValue == '3':
            buttons[index].config(fg="red")
        elif cellValue == '4':
            buttons[index].config(fg="#9900ff")
        elif cellValue == '5':
            buttons[index].config(fg="#660000")
        elif cellValue == '6':
            buttons[index].config(fg="#4a86e8")
        elif cellValue == '7':
            buttons[index].config(fg="black")
        elif cellValue == '8':
            buttons[index].config(fg="#d9d9d9")
        else:
            pass
        
        if not(cellValue == '0') and isFinished(x,y): 
            finished.append([x,y])
        
        youWin()
        



def revealNeighbours(event,i,j):
    global rows
    global revealed
    global flags
     
    valid_neighbours = validNeighbours(i,j)
    
    for k in range(len(valid_neighbours)):
        n = valid_neighbours[k].split(',')
        a = int(n[0])
        b = int(n[1])
        index = a*rows+b
        
        if not([a,b] in revealed) and not([a,b] in flags):
            reveal(event,a,b,index)


def countNeighboursBombs(i,j):
    global tiles
    
    count = 0
    neighbours = validNeighbours(i,j)
            
    for k in range(len(neighbours)):
        n = neighbours[k].split(',')
        a = int(n[0])
        b = int(n[1])
        
        if(tiles[a][b] == 'X'):
            count += 1
                    
    return str(count)




def setTiles():
    global rows
    global columns
    global bombs
    global tiles
    global difficulty
    
    print("New Game")
    tiles.clear()
    tiles = [['0' for x in range(rows)] for y in range(columns)] 
    
    setBombs()
    bombs_tiles = []
    
    

    while(bombs>0):
        r1 = random.randint(0, rows-1)
        r2 = random.randint(0, columns-1)
    
        if(not([r1,r2] in bombs_tiles)):
            bombs_tiles.append([r1,r2])
            bombs -= 1
            tiles[r1][r2] = 'X'
        else:
            pass
    
    setBombs()

    for i in range(rows):
        for j in range(columns):
            if(tiles[i][j] == '0'):
                tiles[i][j] = countNeighboursBombs(i,j)
    
    for i in range(columns):
        print(tiles[i])

def updateCounter(event):
    global bombCounterLabel
    global flags
    global bombs

    bombCounter = bombs - len(flags)
    bombCounterLabel.config(text = "Bombs: " + str(bombCounter),fg="red")



def resetGame():
    global flags
    global buttons
    global revealed
    global rows
    global columns
    global root
    global restartButton
    global restartIcon
    global finished
    global window_width
    global bombs
    global bombCounterLabel
    global finishedGame

    finishedGame = False

    flags.clear()
    buttons.clear()
    revealed.clear()
    finished.clear()

    restartButton.grid(row=0,column=0,columnspan = columns) 
    restartButton.bind('<Button-1>', beginGame)

    bombCounter = bombs - len(flags)
    bombCounterLabel.config(text = "Bombs: " + str(bombCounter),fg="red")
    bombCounterLabel.grid(row=0,column=columns-2,columnspan = columns,sticky="W") 

    for i in range(1,rows+1):
        for j in range(columns):
            Grid.rowconfigure(root,i,weight=1)
            Grid.columnconfigure(root,j,weight=1)
    
    cellNumber = 0

    for i in range(1,rows+1):
        for j in range(columns):
            # Create a Button
            buttons.append(Button(root, width=2, height=1))
            buttons[cellNumber].grid(row=i,column=j,sticky="NSEW")
            buttons[cellNumber].bind('<Double-Button-1>', lambda event, x=i-1,y=j,index=cellNumber:reveal(event,x,y,index))
            #buttons[cellNumber].bind('<Double-Button-1>', lambda event, x=i-1,y=j:solver(event,x,y), add='+')
            buttons[cellNumber].bind('<Button-2>', lambda event, x=i-1,y=j:solver(event,x,y))
            buttons[cellNumber].bind('<Button-3>', lambda event, x=i-1,y=j,index=cellNumber:flagClick(event,x,y,index))
            buttons[cellNumber].bind('<Button-3>', updateCounter, add='+')
            cellNumber += 1



    

def youWin():
    global rows
    global columns
    global revealed
    global flags
    global root
    global finishedGame
    
    cells = rows*columns
    revealedNumber = len(revealed)
    flagsNumber = len(flags)
    
    if((revealedNumber + flagsNumber) == cells):
        finishedGame = True
        result = messagebox.askquestion("", "You Win! Retry?")
        if result == 'yes':
            setTiles()
            resetGame()
        else:
            root.destroy()
    else:
        pass


def youLost():
    global root
    global finishedGame

    finishedGame = True
    result = messagebox.askquestion("", "You Lost! Retry?")
    if result == 'yes':
        setTiles()
        resetGame()
    else:
        root.destroy()


def beginGame(event):  
    global finishedGame

    finishedGame = False
    setTiles()
    resetGame()



def setBombs():
    global difficulty
    global bombs
    
    if difficulty == 1:
        bombs = 10
    elif difficulty == 2:
        bombs = 40
    elif difficulty == 3:
        bombs = 99




def setDifficulty(event,index):
    global rows
    global columns
    global difficulty
    
    if index == 0:
        rows = 9
        columns = 9
        difficulty = 1
    elif index == 1:
        rows = 16
        columns = 16
        difficulty = 2
    elif index == 2:
        rows = 30
        columns = 30
        difficulty = 3
        
    setBombs()
    
    
    print("rows: " + str(rows) + "\ncolumns: " + str(columns) + "\nbombs: " + str(bombs))




def showAllBombs(event):
    global rows
    global columns
    global tiles
    global revealed
    global buttons
    
    for i in range(rows):
        for j in range(columns):
            if (tiles[i][j] == 'X'):
                index = i*rows + j
                buttons[index].config(fg="black")
                buttons[index].config(text="💣")



def resizeWindow(event):
    global difficulty
    global root
    global window_width 
    global window_height
    
    if difficulty == 1:
        root.geometry('300x300')
        window_width = 300
        window_height = 300
    elif difficulty == 2:
        root.geometry('600x600')
        window_width = 600
        window_height = 600
    elif difficulty == 3:
        root.geometry('1200x1200')
        window_width = 1200
        window_height = 1200



def destroyButton(event):
    global menuButtons
    global menuLabel
    
    menuLabel.grid_forget()
    menuLabel.destroy()
    
    createdLabel.grid_forget()
    createdLabel.destroy()

    for i in range(len(menuButtons)):
        menuButtons[i].grid_forget()
        menuButtons[i].destroy()
    
    menuButtons.clear()



def chooseDifficulty():
    global menuButtons

    menuButtons.append(Button(root, text="Begginer",width=20, height=1))
    menuButtons[0].grid(row=1,column=0)
    menuButtons[0].bind('<Button-1>', lambda event, index=0:setDifficulty(event,index))
    menuButtons[0].bind('<Button-1>', resizeWindow, add='+')
    menuButtons[0].bind('<Button-1>', beginGame, add='+')
    menuButtons[0].bind('<Button-1>', destroyButton, add='+')

    menuButtons.append(Button(root, text="Intermediate",width=20, height=1))
    menuButtons[1].grid(row=1,column=1)
    menuButtons[1].bind('<Button-1>', lambda event, index=1:setDifficulty(event,index))
    menuButtons[1].bind('<Button-1>', resizeWindow, add='+')
    menuButtons[1].bind('<Button-1>', beginGame, add='+')
    menuButtons[1].bind('<Button-1>', destroyButton, add='+')

    menuButtons.append(Button(root, text="Expert",width=20, height=1))
    menuButtons[2].grid(row=1,column=2)
    menuButtons[2].bind('<Button-1>', lambda event, index=2:setDifficulty(event,index))
    menuButtons[2].bind('<Button-1>', resizeWindow, add='+')
    menuButtons[2].bind('<Button-1>', beginGame, add='+')
    menuButtons[2].bind('<Button-1>', destroyButton, add='+')






# buttons = []
#tiles = beginPlay(rows,columns,bombs,tiles)
#rows = 10
#columns = 10
rows = 0
columns = 0
bombs = 0
difficulty = 0


# create a tkinter window
root = Tk()
root.title('Minesweeper')
root.resizable(True, True)
root.geometry('450x130')
window_width = 450
window_height = 100
#root.geometry('800x800')

menuLabel = Label(root, text='Welcome!\nTo begin playing, choose the difficulty\n')
menuLabel.pack(ipadx=10, ipady=10)
menuLabel.grid(row=0,column=0,columnspan=10) 

createdLabel = Label(root, text='\n\nProject by: José Pereira')
createdLabel.grid(row=2,column=2,sticky="SE") 

menuButtons = []

bombCounterLabel = Label(root, text = "Bombs: ",fg="red")


restartIcon = PhotoImage(file='smile.png')
restartButton = Button(root, image=restartIcon)



chooseDifficulty()

root.mainloop()




  

