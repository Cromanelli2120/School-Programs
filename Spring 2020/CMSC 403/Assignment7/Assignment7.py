import sys
import tkinter as tk


class CustomCanvas(tk.Frame):
    def __init__(self, height, width):
        tk.Frame.__init__(self, master=None)
        self.height = height
        self.width = width
        self.grid()
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.grid


class Rectangle:

    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


def pack(allRect, canvasSize):
    for x in range(0, len(allRect)):
        pass

    return allRect


def main(path):
    # Open the file with the given filepath from argv[1]
    fileIn = open(path, 'r')
    line = fileIn.readline().strip()

    # Split the elements into height and width and make a canvas from them
    dims = line.split(',')
    myCanvas = CustomCanvas(int(dims[0]), int(dims[1]))
    rectList = []
    # Continue to parse until no more lines
    while True:
        line = fileIn.readline().strip()
        if not line:
            break
        line = line.split(',')
        # Again, get the dimensions from the line and create a rectangle
        rect = Rectangle(int(line[0]), int(line[1]))
        # add the new triangle to our list of triangles
        rectList.append(rect)
        # end while

    canvasDims = (myCanvas.height, myCanvas.width)
    rectList = pack(rectList, canvasDims)

    for rect in rectList:
        myCanvas.create_rectangle()

    fileIn.close()


if __name__ == '__main__':
    main(sys.argv[1])
