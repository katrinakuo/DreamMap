#Hack@Smith
#w group

######################################################################################################
#
#                             LIBRARIES
#
######################################################################################################

from graphics import*
from time import sleep
import pdb

######################################################################################################
#
#                             VARIABLES
#
######################################################################################################

WIDTH = 1000
HEIGHT = 730

win = GraphWin( "Dream Map", WIDTH, HEIGHT)

MapCSV = "smithMapHack.csv"
SmithMap = "SmithMap.gif"

######################################################################################################
#
#                             CLASSES
#
######################################################################################################

class Button:
     """Implements a button, which contains a label (text),
     is rectangular (frame), and can be clicked (True) or not clicked."""

     def __init__(self, x1, y1, w, h, text ):
          """constructor: pass (x,y) of top left corner,
          and width and height.  Pass the text displayed in
          button."""
          p1 = Point( x1, y1 )
          p2 = Point( x1+w, y1+h )
          self.frame = Rectangle( p1, p2 )
          self.frame.setFill( "white" )
          self.label = Text(Point( x1+w//2, y1+h//2 ), text )
          self.clicked = False
        
     def draw( self, win ):
          """display button on window."""
          self.frame.draw( win )
          self.label.draw( win )

     def isClicked( self, p ):
          """Checks if p is inside the frame of the button.  Returns True
          if p inside frame, False otherwise.  If p inside, button
          changes state and color."""
          x1, y1 = self.frame.getP1().getX(), self.frame.getP1().getY()
          x2, y2 = self.frame.getP2().getX(), self.frame.getP2().getY()

          if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
               self.clicked = not self.clicked
               self.frame.setFill( "light blue" )
               sleep(0.3)
               self.frame.setFill( "white" )

               return True
          else:
               return False

######################################################################################################
#
#                             FUNCTIONS
#
######################################################################################################

def boxes(mapLines):
     polygons = []
     for line in mapLines:
          item = (str(line)).split(",")#get rid of lines that are too short

          #used for specific lines that create more pleasing polygons

          #designating each variable
          category = ((item[0])).lower()#insignificant
          nameList2 = item[1].lower().split(' ')
          name = "".join(nameList2)
          colorList2 = item[2].lower().split(' ')
          color = "".join(colorList2)
          coordinate = item[5:-2]
          category = str(item[0])
          categoryList = str(category[0:len(category)]).lower().split(" ")
          category = "".join(categoryList)

          if color == "red":
               if name == "quad":
                    color = "lavender"
               elif name == "greenstreet":
                    color = "honeydew"
               elif name == "centercampus":
                    color = "azure"
               elif name == "upperelmstreet":
                    color = "Misty Rose"
               else:
                    color = "Light Yellow"                    
               
          polygon = []

          for x, y in zip(range(0, len(coordinate), 2), range(1, len(coordinate), 2)): #alternate the numbers so every even is x and every odd is y
               X = coordinate[x].strip() #removing any excess un-needed info
               Y = coordinate[y].strip() #removing any excess un-needed info
               points = Point(X, Y) #creating point
               polygon.append(points)#add point to polygon
          polygons.append([name, color, polygon])
          
     return polygons
     #pdb.set_trace()
     #createMap(polygons)

def createMap(polygons):
     for name, color, polygon in polygons:
          #to create the map of each item/polygon and color coding

          poly = Polygon(polygon) #objectifying the polygon
          poly.draw(win) #draw on window
          poly.setFill(color)#fill in color based on that house

def makeButtons():
     quadButton = Button(530, 75, 138, 40, "Quad")
     quadButton.draw(win)
     
     greenStButton = Button(205, 430, 200, 40, "Green St")
     greenStButton.draw(win)

     centerCampusButton = Button(500, 385, 195, 40, "Center Campus")
     centerCampusButton.draw(win)

     upperElmStButton = Button(518, 575, 145, 40, "Upper Elm St")
     upperElmStButton.draw(win)

     lowerElmStButton = Button(390, 680, 100, 40, "Lower Elm St")
     lowerElmStButton.draw(win)
     
     while True:
          clickedPoint = win.getMouse()
          
          if quadButton.isClicked(clickedPoint): # if exit click, stop loop
               continue
          if greenStButton.isClicked(clickedPoint):
               continue
          if centerCampusButton.isClicked(clickedPoint):
               continue
          if upperElmStButton.isClicked(clickedPoint):
               continue
          if lowerElmStButton.isClicked(clickedPoint):
               continue



def main():
     global win
     
     # put a logo of Smith in the middle of the window
     img = Image( Point(875/2.4, HEIGHT//2), "SmithMap.gif" ) #name of smith map gif on my comp
     img.draw( win )

     #to open the smith map csv that is has been collaborated by every csc111 student
     file = open(MapCSV, "r")
     lines = file.readlines()
     file.close()
     polygons = boxes(lines)
     createMap(polygons)
     makeButtons()


if __name__ == '__main__':
     main()


"""
          while True:
               clickedPoint =  win.getMouse()

               if quadButton.isClicked(clickedPoint): # if exit click, stop loop
                    continue
               
               if greenStButton.isClicked(clickedPoint):
                    continue

               if centerCampusButton.isClicked(clickedPoint):
                    continue
                    
               if upperElmStreetButton.isClicked(clickedPoint):
                    continue

               if upperElmStreetButton.isClicked(clickedPoint):
                    continue

                    """
