def solver(event,x,y):
    global rows
    global columns
    global difficulty
    global revealed
    global tiles
    global buttons
    global finished
    global unsolvable
    
    
    print("solve " + str(x) + ',' + str(y))
    
    index = x*rows+y
    
    valid_neighbours = validNeighbours(x,y)
    maxNeighbours = len(valid_neighbours)
    
    
    if [x,y] in unsolvable:
        pass
    elif not([x,y] in finished) and not([x,y] in flags):
        buttons[index].config(bg="white")
        if not([x,y] in revealed):
            reveal(event,x,y,index)
        
        cellValue = int(tiles[x][y])
        print("chosen cell: " + str(x) + ',' + str(y))
    
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
            finished.append([x,y])
            if [x,y] in unsolvable:
                unsolvable.remove([x,y])
            
            revealNeighbours(event,x,y)
            solveNeighbours(event,x,y)
            
        
        elif((f_neighbours+u_neighbours)==cellValue):
            finished.append([x,y])
            
            if [x,y] in unsolvable:
                unsolvable.remove([x,y])
            
            for i in range(u_neighbours):
                a = int(unknown_neighbours[i][0])
                b = int(unknown_neighbours[i][1])
                index = a*rows+b
                flagged_neighbours.append([a,b])
                flagClick(event,a,b,index)
            
            
            
        else:
            print("Dont know!")
            unsolvable.append([x,y])
            
            solveNeighbours(event,x,y)
                
            
            print('i give up!')
            """
            chosen = False
            
            revealedAndUnsolvable = [value for value in unsolvable if value in revealed]
            
            if revealedAndUnsolvable ==  revealed:
                print("choosing random cell")
                r1 = random.randint(0, rows-1)
                r2 = random.randint(0, columns-1)
                solver(event,r1,r2)
            else:
                while (chosen == False):
                    newCell = random.choice(revealed)
                    
                    if not(newCell in finished) and not(newCell in unsolvable):
                        chosen = True
                        solver(event,newCell[0],newCell[1])
            """
    else:
        print("Solved cell!")
        """  
        chosen = False
            
        revealedAndUnsolvable = [value in unsolvable for value in revealed]
            
        if not(False in revealedAndUnsolvable):
            print("choosing random cell")
            r1 = random.randint(0, rows-1)
            r2 = random.randint(0, columns-1)
            solver(event,r1,r2)
        else:
            while (chosen == False):
                newCell = random.choice(revealed)
                    
                if not(newCell in finished) and not(newCell in unsolvable) and not(newCell in flags):
                    chosen = True
                    solver(event,newCell[0],newCell[1])

        """

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


import math 
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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

def iselem(r1,r2,array):
    for i in range(len(array)):
        if (r1 == array[i][0] and r2 == array[i][1]):
            return True
    return False


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
        
        if [a,b] in revealed or [a,b] in flags:
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
    
    if not([x,y] in revealed) and not([x,y] in flags):
        flags.append([x,y])
        buttons[index].config(fg="red")
        buttons[index].config(text="🚩")
        youWin()
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
    
    print("reveal " + str(x) + ',' + str(y))
    cellValue = tiles[x][y] 
    
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
        
        print('finished')
        print(finished)
        print('revealed')
        print(revealed)
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
    
        if(not(iselem(r1,r2,bombs_tiles))):
            bombs_tiles.append([r1,r2])
            bombs -= 1
            tiles[r1][r2] = 'X'
        else:
            pass

    for i in range(rows):
        for j in range(columns):
            if(tiles[i][j] == '0'):
                tiles[i][j] = countNeighboursBombs(i,j)
    
    for i in range(columns):
        print(tiles[i])


def resetGame():
    global flags
    global buttons
    global revealed
    global rows
    global columns
    global root
    global restartButton
    global finished

    flags.clear()
    buttons.clear()
    revealed.clear()
    finished.clear()
    
    

    #label=ttk.Label(root,text="Deez Nuts!")
    #label.grid(row=0,column=0,columnspan=1) 
    

    #restartButton.grid(row=0,column=1,columnspan=10) 
    #restartButton.bind('<Button-1>', beginGame)
    
    
    for i in range(rows+1):
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
            #buttons[cellNumber].bind('<Button-3>', flagCounter, add='+')
            cellNumber += 1


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
    

def youWin():
    
    global rows
    global columns
    global revealed
    global flags
    global root
    
    cells = rows*columns
    revealedNumber = len(revealed)
    flagsNumber = len(flags)
    
    if((revealedNumber + flagsNumber) == cells):
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
       
    result = messagebox.askquestion("", "You Lost! Retry?")
    if result == 'yes':
        setTiles()
        resetGame()
    else:
        root.destroy()


def beginGame(event):    
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




def destroyButton(event):
    global menuButtons
    global menuLabel
    
    menuLabel.grid_forget()
    menuLabel.destroy()
    
    for i in range(len(menuButtons)):
        menuButtons[i].grid_forget()
        menuButtons[i].destroy()
    
    menuButtons.clear()



def chooseDifficulty():
    global menuButtons
    global menuLabel
    
    menuLabel.config(text='Choose the difficulty')

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
root.geometry('450x100')
window_width = 450
window_height = 100
#root.geometry('800x800')

menuLabel = Label(root, text='')
menuLabel.pack(ipadx=10, ipady=10)
menuLabel.grid(row=0,column=0,columnspan=10) 

menuButtons = []


#restartIcon = PhotoImage(file='smile.png')
#restartButton = Button(root, image=restartIcon)
#restartButton.pack(side = LEFT)
#restartButton.bind('<Button-1>', beginGame)
#restartButton.grid(row=0,column=1,columnspan=10) 

#counter_button = Button(admin, text='number up one', command=numup)
#counter_button.pack(side=RIGHT)
#admin.mainloop()


chooseDifficulty()

root.mainloop()




a = [[2, 6], [1, 6], [0, 6], [0, 7], [0, 8], [1, 7], [1, 8], [2, 7], [2, 8], [3, 7], [3, 6], [3, 5], [4, 5], [4, 6], [4, 7], [3, 8], [4, 8]]
b = [[i,j] for i in range(rows) for j in range(columns)]

c = [value in b for value in a]

#print(a)
#print(b)
print(c)

condition = True
for i in range(len(c)):
      condition = condition and c[i]
    
print(condition)    




def deadEnd():
    deadEnd = True
    
    for i in range(len(revealed)):
        if not((revealed[i] in finished) or (revelead[i] in unsolvable)):
            deadEnd = False
            
    return deadEnd    