import sys
import tkinter as tk
from rectpack import newPacker


class CustomCanvas(tk.Frame):
    # Constructor for customCanvas
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = tk.Tk()
        self.canvas = self.addCanvas()

    # Method to actually add a tkinter canvas to the class
    def addCanvas(self):
        canvas = tk.Canvas(self.root, height=self.height, width=self.width, bg="black")
        canvas.pack()
        return canvas

    # Helper method to draw the rectangles on the canvas
    def addRect(self, rect):
        x1, y1 = rect.x, rect.y
        x2, y2 = x1 + rect.width, y1 + rect.height
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    # Apparently I need this to get my window to actually show up
    def goTime(self):
        self.root.mainloop()


# Rectangle class to make rectangles to be added to canvas
class Rectangle:

    # Constructor for rectangle
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


# Method to pack all given rectangles into the canvas
def pack(allRect, canvasSize):
    # Init for packer package
    packer = newPacker()
    # Add all rectangles
    for r in allRect:
        packer.add_rect(width=r.width, height=r.height)

    # Create a bin to mirror the canvas
    packer.add_bin(height=canvasSize[0], width=canvasSize[1])
    packer.pack()

    # Retrieve the bin with the packed rectangles
    bin = packer[0]

    # Clear the old list of rectangles
    allRect.clear()

    # Add packed rectangles to list
    for rect in bin:
        allRect.append(Rectangle(height=rect.height, width=rect.width, x=rect.x, y=rect.y))

    return allRect


# Main method to be called when stand-alone
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

    # Add rectangles to canvas
    for rect in rectList:
        myCanvas.addRect(rect)

    # Actually start the window
    myCanvas.goTime()

    fileIn.close()


if __name__ == '__main__':
    main(sys.argv[1])
