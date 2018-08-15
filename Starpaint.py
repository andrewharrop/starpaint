#Starpaint.py
#a paint project by Austin Teshuba
#Standard features: oval, box, line, brush, pencil, color select, save, load
#advanced: circular color wheel, slider controls, spraypaint, flood fill, regular fill, right click to clear, hold shift to maintain proportions/ratios, filled unfilled toggle
#cursors for every relevant tool, color grab, undo, redo, oval that works on every size length, calligraphy, two color wheels, polygon tool from 3 sides to 20 sides
#resizing of stamps and loaded photos, no dragging for the sizing tools like stamp and load (clicks instead that are much more elegant), storage of loaded photos
#desrription box for tools, 
from pygame import * #all graphics programs will need this
from math import * #math module import
from tkinter import * #for save and load
from random import * # imports random
init()
font.init() # initialize the font module
titleFont=font.SysFont("Art Brewery", 72, False) #create a size 72 Art Brewery font
iconFont=font.SysFont("Arial",10,False)#create the little font for the icons
descriptionFont=font.SysFont("Arial", 14, False)# create the fonts for the descriptions
welcomeFont=font.SysFont("Arial", 14, True)# create the font for the welcome box
headerFont=font.SysFont("Arial", 18, True)# create the fonts to title certain functions
    #r   g b
####Each of these are presaved colors with the rgb coordinates as specified
RED  =(255,0,0) #tuple - a list that can not be changed!
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0,255)
WHITE=(255,255,255,255)
GREY=(122,122,122)
CLICKEDBLUE=(51,152,219)


######Tkinter stuff#####
root=Tk()
root.withdraw()#hides the little Tk window
#########################


size=(1200,720) #screen resolution
screen=display.set_mode(size)#creating a 800x600 window. returns Surface object

display.set_caption("Starpaint")#The caption is starpaint
running=True #boolean variable

######SCREEN SETUP######

background=image.load("background.jpg")
screen.blit(transform.smoothscale(background, (size[0], size[1])), (0,0))#adds background to the screen

canvasSurface=Surface((825,520))#new surface object for canvas
canvasRect=Rect(200,100,825,520)#These are the rect arguments for the canvas
canvasSurface.fill(WHITE)#make the canvase surface white
screen.blit(canvasSurface, (200,100))#add the surface to the screen

title="Starpaint  Create your Own Cup" # create the title at the top of the screen
titleSurface = titleFont.render(title, True, BLACK) # returns surface at the top of the screen for the text
screen.blit(titleSurface, (110,20)) #blit surface to the screen

backSiren=image.load("siren.png")
screen.blit(transform.smoothscale(backSiren, (85,85)), (10,10))

surfaceColor=GREY#all surfaces will be this color


pTool="pencil"#declartion to prevent crashing and give initial green rectangle around pencil
tool="pencil"#default tool is pencil

##############INIT THE TOOL SETS##############

toolSet1Surface=Surface((180,225))#toolset surface creation
toolSet1Rect=Rect(10,100,180,255)
toolSet1Surface.fill(surfaceColor)

def t1Blit():#function to blit the 1st toolset to screen
    screen.blit(toolSet1Surface,(10,100))

t1Blit()

toolSet2Surface=Surface((180,375))#toolset surface creation
toolSet2Rect=Rect(10,335,180,375)
toolSet2Surface.fill(surfaceColor)

def t2Blit():#function to blit the second toolset to screen
    screen.blit(toolSet2Surface, (10,335))
t2Blit()

toolSet3Surface=Surface((750,80))#toolset surface creation
toolSet3Rect=Rect(200,630,750,80)
toolSet3Surface.fill(surfaceColor)
def t3Blit():#function to blit the third toolset to screen
    screen.blit(toolSet3Surface,(200,630))
t3Blit()

########PTOOL CHECK#######
def pToolCheck():#This functions checks the previous tool (the one once selected) and then triggeres the reset function of that icon. This removes the green border from its icon
    global pTool
    if pTool=="pencil":
        pencilReset()
    elif pTool=="eraser":
        eraserReset()
    elif pTool=="line":
        lineReset()
    elif pTool=="oval":
        ovalReset()
    elif pTool=="box":
        boxReset()
    elif pTool=="brush":
        brushReset()
    elif pTool=="polygon":
        polygonReset()
    elif pTool=="load1" or pTool=="load2" or pTool=="load3":
        loadBarReset()
    elif pTool=="calligraphy":
        calligraphyReset()
    elif pTool== "spraypaint":
        spraypaintReset()
    elif pTool=="colorGrab":
        colorGrabIconReset()
    elif pTool=="fill":
        fillIconReset()
    elif pTool=="stamp1":
        pTool=""
        stampIconReset(1)
    elif pTool=="stamp2":
        pTool=""
        stampIconReset(2)
    elif pTool=="stamp3":
        pTool=""
        stampIconReset(3)
    elif pTool=="stamp4":
        pTool=""
        stampIconReset(4)
    elif pTool=="stamp5":
        pTool=""
        stampIconReset(5)
    elif pTool=="stamp6":
        pTool=""
        stampIconReset(6)
    elif pTool=="stamp7":
        pTool=""
        stampIconReset(7)
    elif pTool=="stamp8":
        pTool=""
        stampIconReset(8)
    elif pTool=="stamp9":
        pTool=""
        stampIconReset(9)
    elif pTool=="stamp10":
        pTool=""
        stampIconReset(10)
    elif pTool=="stamp11":
        pTool=""
        stampIconReset(11)
    
##############TOOLSET1#########
def t1SetText(textSurface, rectObj, textObj, font=iconFont):#this function prgramatically places text below each icon specified.
    #block out the area the text used to be
    draw.rect(toolSet1Surface, surfaceColor, (rectObj.x+rectObj.width/2-font.size(textObj)[0]/2, rectObj.y+rectObj.height+5, font.size(textObj)[0], font.size(textObj)[1]))
    #blit it to the surface, centered, belw the icon
    toolSet1Surface.blit(textSurface, (rectObj.x+rectObj.width/2-font.size(textObj)[0]/2, rectObj.y+rectObj.height+5))
    t1Blit()#blit to screen

def iconReset(sTool, icon, iconRect, iconText):#this function programatically resets any icon to its original state (unclicked). This also adds the selected rectangle
    if sTool == tool:
        col=GREEN#if the selected tool is the same as the tool, then give it the green rect
    else:
        col=BLACK#otherwise, give it a standard rect
    draw.rect(toolSet1Surface, surfaceColor, iconRect)#add the icon with border
    toolSet1Surface.blit(icon, (iconRect.x, iconRect.y))
    draw.rect(toolSet1Surface, col, iconRect, 1)

    textSurface=iconFont.render(iconText, True, BLACK)#add the icon text
    t1SetText(textSurface, iconRect, iconText)

def clickedIcon(icon, iconRect, iconText):# This function programmatically adds a clicked effect to all icons as they are pressed. It provides feedback to the user
    #global pTool
    pToolCheck()#get rid of old green rectangles if not needed
    toolSet1Surface.blit(icon, (iconRect.x, iconRect.y))#clear the affected rect area
    draw.rect(toolSet1Surface, CLICKEDBLUE, iconRect, 1)#draw a blue border for the icon
    textSurface=iconFont.render(iconText, True, CLICKEDBLUE)#draw blue font for icon
    t1SetText(textSurface, iconRect, iconText)#put the text on

##########ToolSet 1 image loading, rect creation. This section is self-explanitory - hardcoding numbers for design and assigning variables to image objects
pencilIcon=image.load("pencil.png")#set up the pencil icon
pressedPencilIcon=image.load("pencilClicked.png")#clicked version of the pencil
pencilRect=Rect(15,5,40,40)#rect arguments for pencil
pencilText="Pencil"#This is the text that wil go in the icon text below the icon

###note - this section is commentless because its the same as the previous 4 lines, just repeated for different tools. refer to that for insight
eraserIcon=image.load("eraser.png")#Load the icons, make the icon rectangle
pressedEraserIcon=image.load("eraserClicked.png")
eraserRect=Rect(70,5,40,40)
eraserText="Eraser"

lineIcon=image.load("line.png")
pressedLineIcon=image.load("lineClicked.png")
lineRect=Rect(125,5,40,40)
lineText="Line"

boxIcon=image.load("rectangle.png")
pressedBoxIcon=image.load("rectangleClicked.png")
boxRect=Rect(15,65,40,40)
boxText="Rectangle"

ovalIcon=image.load("oval.png")
pressedOvalIcon=image.load("ovalClicked.png")
ovalRect=Rect(70,65,40,40)
ovalText="Oval"

brushIcon=image.load("brush.png")
pressedBrushIcon=image.load("brushClicked.png")
brushRect=Rect(125,65,40,40)
brushText="Brush"

polygonIcon=image.load("polygon.png")
pressedPolygonIcon=image.load("polygonClicked.png")
polygonRect=Rect(15, 125, 40, 40)
polygonText="Polygon"

calligraphyIcon=image.load("calligraphy.png")
pressedCalligraphyIcon=image.load("calligraphyClicked.png")
calligraphyRect=Rect(70, 125, 40, 40)
calligraphyText="Calligraphy"
quill=image.load("quill.png")#This is a cursor image

spraypaintIcon=image.load("spraypaint.png")
pressedSpraypaintIcon=image.load("spraypaintClicked.png")
spraypaintRect=Rect(125, 125, 40, 40)
spraypaintText="Spraypaint"

##########Icon reset functions#####
#Each of these functions are simply to simplify the typing process when wanting to reset them using the iconReset function. 
def pencilReset():#function to write the icon reset for pencil quickly
    iconReset("pencil", pencilIcon, pencilRect, pencilText)#pass in appropriate arguments for the iconReset function
pencilReset()#call this function initially to add it to the screen
#note - the next functions aren't commented as they are the same code as the previous lines. Look to these comments for insight
def eraserReset():
    iconReset("eraser", eraserIcon, eraserRect, eraserText)
eraserReset()

def ovalReset():
    iconReset("oval", ovalIcon, ovalRect, ovalText)
ovalReset()

def boxReset():
    iconReset("box", boxIcon, boxRect, boxText)
boxReset()

def lineReset():
    iconReset("line",lineIcon, lineRect, lineText)
lineReset()

def brushReset():
    iconReset("brush", brushIcon, brushRect, brushText)
brushReset()

def polygonReset():
    iconReset("polygon", polygonIcon, polygonRect, polygonText)
polygonReset()

def calligraphyReset():
    iconReset("calligraphy", calligraphyIcon, calligraphyRect, calligraphyText)
calligraphyReset()

def spraypaintReset():
    iconReset("spraypaint", spraypaintIcon, spraypaintRect, spraypaintText)
spraypaintReset()

############Polygon slider#########
#This slider controls how manyh sides are going to be on the polygon for the polygon tool
polygonSliderSurface=Surface((160,40))#initialize the slider for thickness
polygonSliderRect=Rect(10,185,160,40)#slider rect arguments
polygonSliderSurface.fill(surfaceColor)#Fill the surface with the surface color so it blends
polygonSliderPos=0#start the slider at 0
draw.line(polygonSliderSurface, BLACK, (10,19),(160,19),2)#draw the slider line
polygonSliderBoxRect = Rect(polygonSliderPos,14,11,11)#create the slider box based on the slider posititon
draw.rect(polygonSliderSurface, BLACK, polygonSliderBoxRect)#draw the rectangle just made
sides=5#starting value for thickness
sidesText=("Sides: %i"%(sides))#programatically create the text for underneath the slider based on slides variable
polygonSliderText=iconFont.render(sidesText, True, BLACK)#make the text object for under the slider
polygonSliderSurface.blit(polygonSliderText, (80-int(iconFont.size(sidesText)[0]/2), 26))#add the text
toolSet1Surface.blit(polygonSliderSurface, (polygonSliderRect.x, polygonSliderRect.y))#Blit to the toolset
t1Blit()#blit the toolset to the screen

polygonPointsArray=[]#Empty array for polygon points


def polygonSlider(x):#Adjust the polygon slider as the x coordinate of the slider box changes
    global polygonSliderBoxRect#declare all affectted variables as global so they change on a global scope
    global sides
    global sidesText
    global polygonSliderText
    global polygonSliderSurface
    polygonSliderSurface.fill(surfaceColor)#clear the surface 
    draw.line(polygonSliderSurface, BLACK, (0,19),(160,19),2)#readd the line
    polygonSliderBoxRect = Rect(x,14,11,11)#remake the select square 
    draw.rect(polygonSliderSurface, BLACK, polygonSliderBoxRect)#add the select square to the surface
    sidesText=("Sides: %i"%(sides))#change the text based on the amount fo sides
    polygonSliderText=iconFont.render(sidesText, True, BLACK)#make the text object, and add it to the screen
    polygonSliderSurface.blit(polygonSliderText, (80-int(iconFont.size(sidesText)[0]/2), 26))
    toolSet1Surface.blit(polygonSliderSurface, (polygonSliderRect.x, polygonSliderRect.y))#blit to surface, blit to screen
    t1Blit()





#############SECOND BOX OF CONTROLS##################

#####Initial functions
def clickedIcon2(icon, iconRect, iconText):#Programmatically gives the clicked effect for icons
    pToolCheck()#get rid of old green rectangle
    draw.rect(toolSet2Surface, surfaceColor, iconRect)#clear cion area
    toolSet2Surface.blit(icon, (iconRect.x, iconRect.y))#give the icon area the desired blue effect
    draw.rect(toolSet2Surface, CLICKEDBLUE, iconRect, 1)
    textSurface=iconFont.render(iconText, True, CLICKEDBLUE)
    t2SetText(textSurface, iconRect, iconText)#blit and add in text

def t2SetText(textSurface, rectObj, textObj, font=iconFont):#adds text to the icons with surface object, rectangle object, text object and font
    #Centers text under icons
    draw.rect(toolSet2Surface, surfaceColor, (rectObj.x+rectObj.width/2-font.size(textObj)[0]/2, rectObj.y+rectObj.height+5, font.size(textObj)[0], font.size(textObj)[1]))
    #blits to screen
    toolSet2Surface.blit(textSurface, (rectObj.x+rectObj.width/2-font.size(textObj)[0]/2, rectObj.y+rectObj.height+5))
    t2Blit()

    
def iconReset2(icon, iconRect, iconText, sTool="uselessWord"):#resets icons in the second tool set to their usual self. Takes icon object, rectangle, text, and its tool name 
    if sTool==tool:#default sTool is so no rectangle will be triggered if tool is irrelevant. If relevant, and the tool inputted is the present tool, draw a green rect
        col=GREEN
    else:
        col=BLACK#otherwise draw a normal blackm one
    draw.rect(toolSet2Surface, surfaceColor, iconRect)#clear area
    toolSet2Surface.blit(icon, (iconRect.x, iconRect.y))#add icon
    draw.rect(toolSet2Surface, col, iconRect, 1)#draw border

    textSurface=iconFont.render(iconText, True, BLACK)#make and add text
    t2SetText(textSurface, iconRect, iconText)

#################THICKNESS SLIDER#################
    #This slider control controls the thickness of the brushes and shapes

def thickSlider(x):
    global sliderRect
    thicknessSliderSurface.fill(GREY)
    draw.line(thicknessSliderSurface, BLACK, (0,19),(160,19),2)
    sliderRect = Rect(x,14,11,11)
    draw.rect(thicknessSliderSurface, BLACK, sliderRect)
    toolSet2Surface.blit(thicknessSliderSurface,thicknessSliderPos)
    #screen.blit(toolSet2Surface,(10,335))
    t2Blit()

    thicknessText=("Thickness: %i"%(thickness))
    thicknessSurface=iconFont.render(thicknessText, True, BLACK)
    #t2SetText(thicknessSurface, thicknessSliderRect,thicknessText)
    toolSet2Surface.blit(thicknessSurface, (thicknessSliderRect.x+thicknessSliderRect.width/2-iconFont.size(thicknessText)[0]/2, thicknessSliderRect.y+26))
    t2Blit()


thicknessSliderSurface=Surface((160,40))#initialize the slider for thickness
thicknessSliderRect=Rect(10,325,160,40)
thicknessSliderSurface.fill(surfaceColor)#fill the slider box with surface color
thicknessSliderPos=(10,325)
sliderPos=0#starting position is 0
draw.line(thicknessSliderSurface, BLACK, (0,19),(160,19),2)#make the slider line
sliderRect = Rect(sliderPos,14,11,11)
draw.rect(thicknessSliderSurface, BLACK, sliderRect)#draw the slider select box
toolSet2Surface.blit(thicknessSliderSurface,thicknessSliderPos)#blit to surface
screen.blit(toolSet2Surface,(10,335))#blit to screen


thickness=1#starting value for thickness
thicknessText=("Thickness: %i"%(thickness))#update the thickness text programmatically based on the thickness variable
thicknessSurface=iconFont.render(thicknessText, True, BLACK)#Make initial text surface nd add it to the screen
toolSet2Surface.blit(thicknessSurface, (thicknessSliderRect.x+thicknessSliderRect.width/2-iconFont.size(thicknessText)[0]/2, thicknessSliderRect.y+26))#blit to surface
t2Blit()


#Note: the following is a departure from previous style layouts in toolset 1. ZThis is because tool set 2 functions are very different from each other and should be segregated completely

#FILLED ICON
filledIcon=image.load("filled.png")#import all filled icons and create all rect arguments
pressedFilledIcon=image.load("filledClicked.png")
unfilledIcon=image.load("unfilled.png")
pressedUnfilledIcon=image.load("unfilledClicked.png")
filledText="Filled"#text for icons
unfilledText="Unfilled"
filledRect=Rect(15,5,40,40)
filled=False
def filledReset():#make icon the filled icon
    global filled
    draw.rect(toolSet2Surface, surfaceColor, filledRect)#clear the area
    toolSet2Surface.blit(filledIcon, (filledRect.x, filledRect.y))#add icon
    draw.rect(toolSet2Surface, BLACK, filledRect, 1)#draw border
    filledTextSurface=iconFont.render(filledText, True, BLACK)#make and draw the text
    placeHolderSurface=iconFont.render(unfilledText, True, surfaceColor)
    t2SetText(placeHolderSurface, filledRect, unfilledText)
    t2SetText(filledTextSurface, filledRect, filledText)
    filled=True

def unfilledReset():#make icon the unfilled icon
    global filled
    draw.rect(toolSet2Surface, surfaceColor, filledRect)#
    toolSet2Surface.blit(unfilledIcon, (filledRect.x, filledRect.y))
    draw.rect(toolSet2Surface, BLACK, filledRect, 1)
    unfilledTextSurface=iconFont.render(unfilledText, True, BLACK)
    t2SetText(unfilledTextSurface, filledRect, unfilledText)
    filled=False

unfilledReset()

#UNDO
undoIcon=image.load("undo.png")#load the undo icon
pressedUndoIcon=image.load("undoClicked.png")
undoRect=Rect(70,5,40,40)#make undo rect
undoText="Undo"
def undoReset():#fast function for undo icon reset
    iconReset2(undoIcon, undoRect, undoText)
undoReset()
undoArray=[]#empty undo array

#REDO
redoIcon=image.load("redo.png")#load redo icon
pressedRedoIcon=image.load("redoClicked.png")
redoRect=Rect(125,5,40,40)#make redo rect
redoText="Redo"
def redoReset():#redo function for fast redo icon reset
    iconReset2(redoIcon, redoRect, redoText)
redoReset()
redoArray=[]#empty redo array

def undoArrayAddition():#this functions adds the current canvas to the undo array. Clears redo array, as if you draw something after undoing you cant redo it anymore
    global undoArray
    global canvasSurface
    global redoArray
    undoArray.append(canvasSurface.copy())
    redoArray=[]
    print(len(redoArray), len(undoArray))
def undoArrayActivate():#add the last item in the array to the canvas, and put it in the redo array
    global undoArray
    global canvasSurface
    global redoArray
    if len(undoArray)>0:
        redoArray.append(canvasSurface.copy())
        canvasSurface.blit(undoArray[-1], (0,0))#add the last thing in array to screen
        canvasCopy=undoArray[-1]
        undoArray.pop()
        canvasBlit()
    print(len(redoArray), len(undoArray))
def redoArrayActivate():#make the last item in the redo array the canvas,move it to the undo array
    global undoArray
    global canvasSurface
    global redoArray
    if len(redoArray)>0:
        undoArray.append(canvasSurface.copy())
        canvasSurface.blit(redoArray[-1], (0,0))#add last thing in array to screen
        canvasCopy=redoArray[-1]
        redoArray.pop()
        canvasBlit()
    print(len(redoArray), len(undoArray))

##############COLOR SWABBER#########
colorGrabIcon=image.load("colorIcon.png")#load the icons and create the rectangle objects
pressedColorGrabIcon=image.load("colorClicked.png")
colorGrabIconRect=Rect(15,65,40,40)
colorGrabIconText="Color Grab"

def colorGrabIconReset():#functionfor a fast icon reset
    iconReset2(colorGrabIcon, colorGrabIconRect, colorGrabIconText, "colorGrab")
colorGrabIconReset()#initialize the colorGrab icon


############FILL###########
fillIcon=image.load("fill.png")#get fill icon
pressedFillIcon=image.load("fillClicked.png")
fillIconRect=Rect(70, 65, 40, 40)#make fill rect object
fillIconText="Fill"#fill icon text

def fillIconReset():#function for fast fill icon reset
    iconReset2(fillIcon, fillIconRect, fillIconText, "fill")
fillIconReset()

###############TRASH############
trashIcon=image.load("trash.png")#get trash icon
pressedTrashIcon=image.load("trashClicked.png")
trashIconRect=Rect(125, 65, 40, 40)#make trash rect
trashIconText="Clear"#trash icon text

def trashIconReset():#function for fast icon reset
    iconReset2(trashIcon, trashIconRect, trashIconText)
trashIconReset()

###################XY UPDATE BOX#################
xySurfaceRect=Rect(820,30,100,60)#create xy box rect
xySurface=Surface((xySurfaceRect.width, xySurfaceRect.height))#new surface for the x-y preview box
xySurfaceText="Mouse Location:"#title text creation and blit
screen.blit(iconFont.render(xySurfaceText, True, BLACK), (xySurfaceRect.x, xySurfaceRect.y-iconFont.size(xySurfaceText)[1]-2))
def xySurfaceUpdate(x,y):#function to update the x and y text surface based on the mx and my. These are parameters that will be passed in
    xySurface.fill(surfaceColor)
    if canvasRect.collidepoint(x,y):
        xText="X: %i"%(x)
        yText="Y: %i"%(y)
    else:
        xText="X: Off Canvas"
        yText="Y: Off Canvas"
    xySurface.blit(welcomeFont.render(xText, True, BLACK), (xySurfaceRect.centerx-xySurfaceRect.x-int(round(welcomeFont.size(xText)[0]/2)),10))#center the text
    xySurface.blit(welcomeFont.render(yText, True, BLACK), (xySurfaceRect.centerx-xySurfaceRect.x-int(round(welcomeFont.size(yText)[0]/2)),35))
    screen.blit(xySurface, (xySurfaceRect.x, xySurfaceRect.y))
xySurfaceUpdate(0,0)#initialize first frame with an x and y of 0,0
####################SAVE AND LOAD BUTTONS#################
saveIcon=image.load("save.png")#get save icon
pressedSaveIcon=image.load("saveClicked.png")
saveRect=Rect(930, 30, 40, 40)#make save rect
saveText="Save"
saveTextObject=iconFont.render(saveText, True, BLACK)#make save texts
clickedSaveTextObject=iconFont.render(saveText, True, CLICKEDBLUE)
#get under text subsurface, as icon is "transparent"
underText=screen.subsurface(saveRect.x+saveRect.width/2-iconFont.size(saveText)[0]/2, saveRect.y+saveRect.height+5, iconFont.size(saveText)[0], iconFont.size(saveText)[1])
underTextSurface=underText.copy()
underIcon=screen.subsurface(saveRect)
underIconSurface=underIcon.copy()
def saveTextSet(saveTextObject=saveTextObject):#function for puting text under save icon
    screen.blit(underTextSurface, (saveRect.x+saveRect.width/2-iconFont.size(saveText)[0]/2, saveRect.y+saveRect.height+5))#add and centre text
    screen.blit(saveTextObject, (saveRect.x+saveRect.width/2-iconFont.size(saveText)[0]/2, saveRect.y+saveRect.height+5))
    
def saveReset():#reset save icon to normal
    draw.rect(screen, BLACK, saveRect, 1)
    screen.blit(saveIcon, (saveRect.x, saveRect.y))
    saveTextSet()
saveReset()



def clickedSave():#function for clickedBlue effect on the saved icon
    screen.blit(underIconSurface, (saveRect.x, saveRect.y))
    #draw.rect(screen, surfaceColor, saveRect)
    draw.rect(screen, CLICKEDBLUE, saveRect,1)
    screen.blit(pressedSaveIcon, (saveRect.x, saveRect.y))
    saveTextSet(clickedSaveTextObject)

loadIcon=image.load("load.png")#get load icon
pressedLoadIcon=image.load("loadClicked.png")
loadRect=Rect(980, 30, 40, 40)#make load rect
loadText="Load"
loadTextObject=iconFont.render(loadText, True, BLACK)#make text objects
clickedLoadTextObject=iconFont.render(loadText, True, CLICKEDBLUE)
#Make load subsurfaces for "trasnparent" background 
loadTextU=screen.subsurface(loadRect.x+loadRect.width/2-iconFont.size(loadText)[0]/2, loadRect.y+loadRect.height+5, iconFont.size(loadText)[0], iconFont.size(loadText)[1])
loadTextUnder=loadTextU.copy()
loadU=screen.subsurface(loadRect)
loadUnder=loadU.copy()

def loadTextSet(loadTextObject=loadTextObject):#function to add text under the load icon
    screen.blit(loadTextUnder, (loadRect.x+loadRect.width/2-iconFont.size(loadText)[0]/2, loadRect.y+loadRect.height+5))#centre the text
    screen.blit(loadTextObject, (loadRect.x+loadRect.width/2-iconFont.size(loadText)[0]/2, loadRect.y+loadRect.height+5))

def loadReset():#function to reset load icon back to normal
   # draw.rect(screen, surfaceColor, loadRect)
    draw.rect(screen, BLACK, loadRect, 1)
    screen.blit(loadIcon, (loadRect.x, loadRect.y))
    loadTextSet()
loadReset()
def clickedLoad():#function to get cliked blue effect on the load icon
    screen.blit(loadUnder, (loadRect.x, loadRect.y))
    #draw.rect(screen, surfaceColor, loadRect)
    draw.rect(screen, CLICKEDBLUE, loadRect, 1)
    screen.blit(pressedLoadIcon, (loadRect.x, loadRect.y))
    loadTextSet(clickedLoadTextObject)

###################################LAST LOADED BAR##########################
#when images are loaded, they will be accessed from the last loaded bar. Up to 3 can be held at a time
loadedImages=[]#empty loaded images array
questionMarkIcon=image.load("questionMark.png")
for t in range(3):#add 3 question marks to the arry to appear in the last loaded bar befor adding images
    loadedImages.append(questionMarkIcon)
loadedImagesSurface=Surface((160,60))#make surface and rect arguments
loadedImagesSurface.fill(surfaceColor)
loadedImagesRect=Rect(1030,30,160,60)

def loadedImagesSurfaceBlit():#function to add the images to the last loaded bar. Basically blit the images and ad text underneath indicating photo number
    for n in range(3):
        draw.rect(loadedImagesSurface, surfaceColor, (10+50*n-iconFont.size(str(n+1))[0]/2+20, 45, iconFont.size(str(n+1))[0], iconFont.size(str(n+1))[1]))
        newTextObj=iconFont.render(str(n+1), True, BLACK)
        loadedImagesSurface.blit(newTextObj, (10+50*n-iconFont.size(str(n+1))[0]/2+20, 45))
    screen.blit(loadedImagesSurface, (loadedImagesRect.x,loadedImagesRect.y))
def loadBarReset():#function to reset the last load bar from clicking effects
    loadedImagesSurface.fill(surfaceColor)
    if tool=="load1":#making an arbitrary number equal to the index number of the icon to add the green selected rect
        xCheck=0
    elif tool=="load2":
        xCheck=1
    elif tool=="load3":
        xCheck=2
    else:
        xCheck=3#make impossible number if none of the icons are the tool
    for x in range(3):
        if x == xCheck:
            col=GREEN
        else:
            col=BLACK
        draw.rect(loadedImagesSurface, col, (10+50*x, 5, 40, 40),1)#draw the rects and blit the icons
        scaledPic=transform.scale(loadedImages[x], (40,40)) 
        loadedImagesSurface.blit(scaledPic,(10+50*x,5))
    loadedImagesSurfaceBlit()
loadBarReset()

load1Rect=Rect(10,5,40,40)#create rects for each indidivdual icon
load2Rect=Rect(60,5,40,40)
load3Rect=Rect(110,5,40,40)

def clickedLoadedIcon(iconRect, iconNumber):#function for the clicking effect on the loaded images icons
    #global pTool
    pToolCheck()#get rid of old selected rectangles
    text=str(iconNumber)#create text for icon
    textObject=iconFont.render(text, True, CLICKEDBLUE)#blue border
    draw.rect(loadedImagesSurface, surfaceColor, (iconRect.x-iconFont.size(text)[0]/2+20, 45, iconFont.size(text)[0], iconFont.size(text)[1]))#clear rect area
    loadedImagesSurface.blit(textObject, (iconRect.x-iconFont.size(str(iconNumber))[0]/2+20, 45))#blit the icon
    draw.rect(loadedImagesSurface, CLICKEDBLUE, iconRect, 1) #add border rect
    screen.blit(loadedImagesSurface, (loadedImagesRect.x,loadedImagesRect.y))#blit the surface to screen
loadedImagesText="Loaded Images:"#make text for the title of the surface
loadedImagesTextObject=iconFont.render(loadedImagesText, True, BLACK)
screen.blit(loadedImagesTextObject, (loadedImagesRect.x, loadedImagesRect.y-3-iconFont.size(loadedImagesText)[1]))

###############COLOR SELECT############

selectedColor=(0,0,0)#default color
#make rect argument for the color wheel surface and color wheel. Color wheel surface is bigger for the title and the cursor
colorWheelSurfaceRect=Rect(canvasRect.x+canvasRect.width+10, 460, int(size[0]-(canvasRect.x+canvasRect.width)-10), int(size[0] -(canvasRect.x+canvasRect.width)+20))
colorWheelRect=Rect(colorWheelSurfaceRect.x, colorWheelSurfaceRect.y+40, colorWheelSurfaceRect.width-10, colorWheelSurfaceRect.height-40)#leaves buffer for the cursor, and for borders
cleanColorWheel=transform.scale(image.load("colorWheel.png"), (colorWheelRect.width,colorWheelRect.height))#This is never to be edited. a clean copy for buffer purposes
editColorWheel=cleanColorWheel.copy()#a color wheel to edit with darkness slider

colorSurface=screen.subsurface(colorWheelSurfaceRect).copy()
colorBuffer=colorSurface.copy()#This is never to be edited. This is so we can add this as a clean slate

colorCursorNeeded=False#This is a flag variable that will identify if we have to add the cursor to the color wheel or not

def colorSurfaceBlit():#this is for every blit of the color surface to the screen.
    colorSurface.unlock()
    screen.blit(colorSurface, (colorWheelSurfaceRect.x, colorWheelSurfaceRect.y))
def updateColorWheel():#this is for every time an update to the color wheel is required
    colorSurface.blit(colorBuffer, (0,0))#new subsurface pasted
    colorSurface.blit(headerFont.render("Color Select:", True, BLACK), (0,0))#add header font
    colorSurface.blit(descriptionFont.render(("R: %i G: %i B: %i"%(selectedColor[0], selectedColor[1], selectedColor[2])), True, BLACK), (0,20))
    colorSurface.blit(editColorWheel, (colorWheelRect.x-colorWheelSurfaceRect.x,colorWheelRect.y-colorWheelSurfaceRect.y))#this is done so if we edit the rects, the system will update the positions as well
    if colorCursorNeeded:
        colorSurface.blit(colorCursor, (smx, smy-colorCursor.get_height()+3))#this adds the cursor if needed
    colorSurfaceBlit()
updateColorWheel()

##Subsection: the block that shows what color is selected
colorSelectBlockSurface=Surface((colorWheelSurfaceRect.width-10, 30))
colorSelectBlockRect=Rect(colorWheelSurfaceRect.x, colorWheelSurfaceRect.y+colorWheelSurfaceRect.height+5, colorWheelSurfaceRect.width-10, 30)

def colorSelectBlockUpdate():#updates the color preview block under the color wheel
    global selectedColor#accesses global selected color
    colorSelectBlockSurface.fill(selectedColor)
    screen.blit(colorSelectBlockSurface, (colorSelectBlockRect.x, colorSelectBlockRect.y))
    updateColorWheel()
colorSelectBlockUpdate()

omx,omy=0,0#declare mx and my and omx and omy to prevent crashing
mx,my=0,0

def wheelCollide():#this checks if the user actually hit the circle or if they hit the area around the circle
    cmx=mx-colorWheelRect.x-(colorWheelRect.width/2)
    cmy=my-colorWheelRect.y-(colorWheelRect.height/2)
    if cmx**2+cmy**2<(colorWheelRect.height/2)**2:#check if its in the circle using the circle equation
        return True
    else:
        return False

colorCursor=image.load("colorIcon.png")#this is the actual cursor itself
        

##################COLOR SELECT SLIDER###############

colorSliderRect=Rect(colorSelectBlockRect.x, colorSelectBlockRect.y+colorSelectBlockRect.height+5, colorSelectBlockRect.width, 25)#make rect objects
colorSliderSurface=screen.subsurface(colorSliderRect).copy()
buffer=screen.subsurface(colorSliderRect).copy()#create a color slider buffer for the background to make it "transparent"
darkness=0


def colorSliderUpdate(x):#update the color slider based on the x position of the selector rect
    global colorSliderSurface#access the follwing varibales on a global scope
    global selectorRect
    global darkness
    global editColorWheel
    colorSliderSurface.blit(buffer, (0,0))#add the buffer to the surface
    screen.blit(buffer, (colorSliderRect.x, colorSliderRect.y))
    draw.line(colorSliderSurface, BLACK, (3, 4), (colorSliderRect.width-3, 4), 1)#draw the slider line
    if x>(colorSliderRect.width-8):#if the width was going to be above max possible, make it max
        x=colorSliderRect.width-8
    if x<0:#If below 0, make it 0
        x=0
    selectorRect=Rect(x,0,8,8)#new rect argument based on arguments passd in
    draw.rect(colorSliderSurface, BLACK, selectorRect)

    if darkness<0:#if darkness is below 0, make it 0
        darkness=0
    elif darkness>100:#if darkness is above max, make it max
        darkness=100

    darknessText=("Darkness: %i"%(darkness))#add darkness text
    darknessTextObject=iconFont.render(darknessText, True, BLACK)
    colorSliderSurface.blit(darknessTextObject, (int((colorSliderRect.width-4)/2-iconFont.size(darknessText)[0]/2)+4, 8))

    screen.blit(colorSliderSurface, (colorSliderRect.x, colorSliderRect.y))
    
    tempDarkness=100-darkness#basically inverts it so it can be used as a multiplier
    
    for x in range(cleanColorWheel.get_width()):#within the wheel, change the brightness and darkess of each pixel
        for y in range(cleanColorWheel.get_height()):
            if (x-colorWheelRect.width/2)**2+(y-colorWheelRect.height/2)**2<=(colorWheelRect.width/2)**2:
                origColor=tuple(cleanColorWheel.get_at((x,y)))
                #change the color args based on brightness and darkness algorithms
                origColor=(max(0,min(int((origColor[0]/100*tempDarkness)),255)), max(0,min((origColor[1]/100*tempDarkness),255)), max(0,min((origColor[2]/100*tempDarkness),255)))
                editColorWheel.set_at((x,y), origColor)
                
    updateColorWheel()
    
colorSliderUpdate(0)#init the color slider

tempPos=selectorRect.x

###############COLOR ICON###############
paintBrushColor=image.load("paintBrushColor.png")#get icon images
paintBrushBlack=image.load("paintBrushBlack.png")
pressedPaintBrush=image.load("paintBrushClicked.png")
paintBrushIconRect=Rect(toolSet3Rect.width+toolSet3Rect.x+20, toolSet3Rect.y+15, 40, 40)#create rect arguments

colorfulText="Color"#make text for under the icon
blackText="Greyscale"
#make a rect to fit the text
paintBrushTextRect=Rect(paintBrushIconRect.x-4, paintBrushIconRect.y+paintBrushIconRect.height+3, paintBrushIconRect.width+8, iconFont.size(colorfulText)[1])
colorful=False#flag variable to check if color is toggled or not

paintBuffer=screen.subsurface(paintBrushIconRect).copy()#get this buffer for the backgouund as its "transparent"
paintTextBuffer=screen.subsurface(paintBrushTextRect).copy()


colorfulTextObject=iconFont.render(colorfulText, True, BLACK)#make text arguments for both color and grey
blackTextObject=iconFont.render(blackText, True, BLACK)
clickedColorTextObject=iconFont.render(colorfulText, True, CLICKEDBLUE)
clickedBlackTextObject=iconFont.render(blackText, True, CLICKEDBLUE)

def bufferColorIcon():#blit to screen a reset for the painticon
    screen.blit(paintBuffer, (paintBrushIconRect.x, paintBrushIconRect.y))
    screen.blit(paintTextBuffer, (paintBrushTextRect.x, paintBrushTextRect.y))
def colorIconClicked():#function to quickly add the clicked effect to the paint tool
    bufferColorIcon()
    screen.blit(pressedPaintBrush, (paintBrushIconRect.x, paintBrushIconRect.y))
    if colorful:
        screen.blit(clickedColorTextObject,((paintBrushTextRect.x+paintBrushTextRect.width//2-iconFont.size(colorfulText)[0]//2), paintBrushTextRect.y))
    else:
        screen.blit(clickedBlackTextObject, ((paintBrushTextRect.x+paintBrushTextRect.width//2-iconFont.size(blackText)[0]//2), paintBrushTextRect.y))
    draw.rect(screen, CLICKEDBLUE, paintBrushIconRect,1)
def updateColorIcon():#function to switch between grey and color depending on what was last chosed
    global colorful
    global cleanColorWheel
    global editColorWheel
    if colorful:
        colorful=False#if it was color ful now it isnt and vice versa
    else:
        colorful=True
    bufferColorIcon()
    if colorful:# if its colorful, add the colorful icon and text indicating color
        cleanColorWheel=transform.scale(image.load("colorWheel.png"), (colorWheelRect.width, colorWheelRect.height))
        editColorWheel=transform.scale(image.load("colorWheel.png"), (colorWheelRect.width, colorWheelRect.height))
        colorSliderUpdate(tempPos)
        screen.blit(paintBrushColor, (paintBrushIconRect.x, paintBrushIconRect.y))
        screen.blit(colorfulTextObject, ((paintBrushTextRect.x+paintBrushTextRect.width//2-iconFont.size(colorfulText)[0]//2), paintBrushTextRect.y))
    else:# otherwise, add the grey icon and text indicating grey
        cleanColorWheel=transform.scale(image.load("greyWheel.png"), (colorWheelRect.width, colorWheelRect.height))
        editColorWheel=transform.scale(image.load("greyWheel.png"), (colorWheelRect.width, colorWheelRect.height))
        colorSliderUpdate(tempPos)
        screen.blit(paintBrushBlack, (paintBrushIconRect.x, paintBrushIconRect.y))
        screen.blit(blackTextObject, ((paintBrushTextRect.x+paintBrushTextRect.width//2-iconFont.size(blackText)[0]//2), paintBrushTextRect.y))
    draw.rect(screen, BLACK, paintBrushIconRect,1)
updateColorIcon()

##########CUSTOM COLOR SURFACE#########
customColorSurface=Surface((int(round(colorWheelSurfaceRect.width))-10, 90))#make a new surface
customColorRect=Rect(colorWheelSurfaceRect.x, colorWheelSurfaceRect.y-95, int(round(colorWheelSurfaceRect.width))-10, 90)#make rect args

customColorSurface.fill(surfaceColor)
customColorSurface.blit(headerFont.render("Adjust Color", True, BLACK), (5,1))#add custom title font

#######functions init
def customColorBlit():#function to blit surface to screen
    screen.blit(customColorSurface, (customColorRect.x, customColorRect.y))

def customIconReset(icon, iconRect):# function to reset icons
    draw.rect(customColorSurface, surfaceColor, iconRect)
    customColorSurface.blit(icon, (iconRect.x, iconRect.y))
    draw.rect(customColorSurface, BLACK, iconRect, 1)
    customColorBlit()

def customIconClicked(icon, iconRect):# function to add clicked effect to icons
    draw.rect(customColorSurface, surfaceColor, iconRect)
    draw.rect(customColorSurface, CLICKEDBLUE, iconRect, 1)
    customColorSurface.blit(icon, (iconRect.x, iconRect.y))
    customColorBlit()

customColorBlit()

##########get icons for this surface
redIcon=image.load("red.png")#get images, make rects, make texts, make small functions to reset the logos to the way they are and not have to type full functuion
redIconRect=Rect(5,headerFont.size("Adjust Color:")[1]+2,30,30)
#redText="More Red"
def redIconReset():
    customIconReset(redIcon, redIconRect)
redIconReset()

greenIcon=image.load("green.png")
greenIconRect=Rect(63,redIconRect.y,30,30)
#greenText="More Green"
def greenIconReset():
    customIconReset(greenIcon, greenIconRect)
greenIconReset()

blueIcon=image.load("blue.png")
blueIconRect=Rect(121, redIconRect.y, 30, 30)
#blueText="More Blue"
def blueIconReset():
    customIconReset(blueIcon, blueIconRect)
blueIconReset()

lessRedIcon=image.load("lessRed.png")
lessRedIconRect=Rect(5,redIconRect.y+redIconRect.height+2, 30, 30)
def lessRedIconReset():
    customIconReset(lessRedIcon, lessRedIconRect)
lessRedIconReset()

lessGreenIcon=image.load("lessGreen.png")
lessGreenIconRect=Rect(63, lessRedIconRect.y, 30,30)
def lessGreenIconReset():
    customIconReset(lessGreenIcon, lessGreenIconRect)
lessGreenIconReset()

lessBlueIcon=image.load("lessBlue.png")
lessBlueIconRect=Rect(121, lessRedIconRect.y, 30,30)
def lessBlueIconReset():
    customIconReset(lessBlueIcon, lessBlueIconRect)
lessBlueIconReset()

########TEXT WRAP FUNCTION########
def drawText(surface, text, color, rect, font, aa=True, bkg=None):#source: pygame documentation
    rect = Rect(rect)
    y = rect.y
    lineSpacing = -2
 
    # get the height of the font
    fontHeight = font.size("Tg")[1]
 
    while text:
        #print("Hello")
        i = 1
 
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
           # print(y+fontHeight)
            #print(rect.bottom)
            break
 
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
 
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
 
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
            #print("This happened!")
            #print(text[:i])
 
        surface.blit(image, (rect.x, y))
        y += fontHeight + lineSpacing
 
        # remove the text we just blitted
        text = text[i:]
        #print(text)
 
    #return text

################DESCRIPTION BOX#############
descriptionSurface=Surface((size[0]-20-canvasRect.x-canvasRect.width, colorWheelSurfaceRect.y-canvasRect.y-100))#make a new surface for the welcome text on the right
descriptionRect=Rect(canvasRect.x+canvasRect.width+10, canvasRect.y,size[0]-20-canvasRect.x-canvasRect.width, colorWheelSurfaceRect.y-canvasRect.y)#rect argument for new surface
quickFactsRect=Rect(5,30,descriptionRect.width-5, descriptionRect.height-5)
#toolDescriptionRect=Rect(quickFactsRect.x,quickFactsRect.y+quickFactsRect.height+6, quickFactsRect.width, quickFactsRect.height-30)
toolDescriptionRect=Rect(5,135,toolSet2Rect.width-10, toolSet2Rect.height-195)#make new description rect for the second tool set where tool descriptions are
toolDescriptionSurface=Surface((toolDescriptionRect.width, toolDescriptionRect.height))

#Make text to be put in the tool describe on the left side of the screen
pencilTextBox="This is the pencil tool. This tool is ideal for drawing fine, refined lines. However, thickness is restricted on this tool."
eraserTextBox="This is the eraser tool. This tool will wipe over any of those ugly mistakes you may have happened to make"
lineTextBox="This is the line tool. Use this tool to draw straight lines. Click once for your starting position, and then again for your ending position. Hold shift for a horiztonal/vertical line. Thickness is restricted for this tool."
brushTextBox="This is the brush tool. Use this tool to draw smooth, rich lines. There are no thickness restrictions, so have fun!"
boxTextBox="This is the rectangle/square tool. Use this tool to create a rectangle. Press once for your starting position, and then drag to the other corner of your desired rectangle. Hold shift to create a square. To fill/unfill, press the fill/unfill button above."
ovalTextBox="This is the oval/circle tool. Use this tool to create an oval/circle. Press once for your starting posititon, and then press again for your ending posititon. Hold shift to make a circle. To fill/unfill, press the fill/unfilled button above."
calligraphyTextBox="This is the calligraphy tool. Use this tool to create beautiful, cursive font. Thickness is restricted."
polygonTextBox="This is the polygon tool. Use this tool to create regular polygons of any size. Control the size with the thickness control. Control the amount of sides with the sides control. To fill/unfill, press the fill/unfill button above."
spraypaintTextBox="This is the spraypaint tool. Use this to add some graffiti to your design."
colorGrabTextBox="This is the Color Grab tool. Use this tool to change your current selected color by grabbing the color of an object already on the screen."
loadTextBox="This is the loaded objects tool. Use this tool to paste your loaded images onto the canvas. Hold shift for an aspect ratio lock."
stampTextBox="This is the stamp tool. Use this tool to stamp pre-brewed designs to the canvas. Hold shift for an aspect ratio lock."
fillTextBox="This is the fill tool. Use this tool to fill areas of the canvas with your selected color. Hold shift to fill only enclosed areas. Without shift, this will fill the screen."
#declare dictionary containing all of these strings
toolTextDict={"pencil": pencilTextBox, "eraser": eraserTextBox, "line": lineTextBox, "brush": brushTextBox, "box": boxTextBox, "oval": ovalTextBox, "calligraphy": calligraphyTextBox,
    "polygon": polygonTextBox, "spraypaint": spraypaintTextBox, "colorGrab": colorGrabTextBox, "load": loadTextBox, "stamp": stampTextBox, "fill": fillTextBox}    


def textUpdate():#function to update the text in the description boxes based on changes in tool selection
    descriptionSurface.fill((169,171,173))
    descriptionText="Welcome to Starpaint! Use this program to explore your creative passions, create something new, and design your own Starbucks Red Cup. A variety of tools are available to your left for your art. Additionally, if you right click the canvas, the screen will clear for you."
    descriptionSurface.blit(headerFont.render("Hey There!", True, BLACK), (5,5))
    drawText(descriptionSurface, descriptionText, BLACK, quickFactsRect, welcomeFont)
    if tool[:len(tool)-1]=="stamp" or tool[:len(tool)-2]=="stamp":
        index="stamp"
    elif tool[:len(tool)-1]=="load":
        index="load"
    else:
        index=tool
    toolDescriptionSurface.fill((169,171,173))
    toolDescriptionSurface.blit(headerFont.render("Tool:", True, BLACK), (0,0))
    drawText(toolDescriptionSurface, toolTextDict[index], BLACK, (0,25,toolDescriptionRect.width, toolDescriptionRect.height), descriptionFont)
    toolSet2Surface.blit(toolDescriptionSurface, (toolDescriptionRect.x, toolDescriptionRect.y))
    t2Blit()
    screen.blit(descriptionSurface, (canvasRect.x+canvasRect.width+10, canvasRect.y))
textUpdate()





###########STAMPS############
goldOrnament=image.load("goldOrnament.png")#get stamp images loaded
silverOrnament=image.load("silverOrnament.png")
lights=image.load("lights.png")
siren=image.load("siren.png")
star=image.load("star.png")
tree=image.load("tree.png")
wreath=image.load("wreath.png")
tower=image.load("tower.png")
bean=image.load("coffeeBean.png")
starbucksCup=image.load("starbucksCup.png")
whiteStarbucksCup=image.load("whiteStarbucksCup.png")
#load those into an array
stampImageArray=[goldOrnament.copy(), silverOrnament.copy(), lights.copy(), siren.copy(), star.copy(), tree.copy(), wreath.copy(), tower.copy(), bean.copy(), starbucksCup.copy(), whiteStarbucksCup.copy()]#.copy is so the original files can be kept pure
#make stamp rects
stamp1IconRect=Rect(15,5,60,60)
stamp2IconRect=Rect(80,5,60,60)
stamp3IconRect=Rect(145,5,60,60)
stamp4IconRect=Rect(210,5,60,60)
stamp5IconRect=Rect(275,5,60,60)
stamp6IconRect=Rect(340,5,60,60)
stamp7IconRect=Rect(405,5,60,60)
stamp8IconRect=Rect(470,5,60,60)
stamp9IconRect=Rect(535,5,60,60)
stamp10IconRect=Rect(600,5,60,60)
stamp11IconRect=Rect(665,5,60,60)
#add stamp icons into an array
stampIconRect=[stamp1IconRect, stamp2IconRect, stamp3IconRect, stamp4IconRect, stamp5IconRect, stamp6IconRect, stamp7IconRect, stamp8IconRect, stamp9IconRect, stamp10IconRect, stamp11IconRect]
#make stamp texts
stamp1Text="Ornament 1"
stamp2Text="Ornament 2"
stamp3Text="Lights"
stamp4Text="Siren"
stamp5Text="Star"
stamp6Text="Tree"
stamp7Text="Wreath"
stamp8Text="Tower"
stamp9Text="Coffee Bean"
stamp10Text="Red Cup"
stamp11Text="White Cup"
#add stamp texts to an array
stampText=[stamp1Text, stamp2Text, stamp3Text, stamp4Text, stamp5Text, stamp6Text, stamp7Text, stamp8Text, stamp9Text, stamp10Text, stamp11Text]


def stampIconReset(stampNumber):#function to reset the stamp icons after they have been clicked
    global tool
    if tool == "stamp"+str(stampNumber):#rectangle select tool - check what tool is being selected
        col=GREEN
    else:
        col=BLACK
    index=stampNumber-1
    asp=stampImageArray[index].get_height()/stampImageArray[index].get_width()#get aspect ration in case it has to lock (hold shift)
    draw.rect(toolSet3Surface, surfaceColor, (stampIconRect[index].x, stampIconRect[index].y, stampIconRect[index].width, stampIconRect[index].height+13))
    if 60*asp<=60:#if itll fit in the box, scale this way
        toolSet3Surface.blit(transform.smoothscale(stampImageArray[index], (60,60)), (stampIconRect[index].x, stampIconRect[index].y))
    else:
        asp=stampImageArray[index].get_width()/stampImageArray[index].get_height()
        toolSet3Surface.blit(transform.smoothscale(stampImageArray[index], (60,60)), (stampIconRect[index].x, stampIconRect[index].y))
    draw.rect(toolSet3Surface, col, stampIconRect[index],1)
     
    tempTextObj = iconFont.render(stampText[index], True, BLACK)
    toolSet3Surface.blit(tempTextObj, (stampIconRect[index].x + stampIconRect[index].width/2 - iconFont.size(stampText[index])[0]/2, stampIconRect[index].y + stampIconRect[index].height + 3))
    t3Blit()
for t in range(1,len(stampImageArray)+1):#call thsis function once for every stamp
    stampIconReset(t)

def stampIconClicked(stampNumber):#function for the clicked effects on the stamp icons
   # global pTool
    pToolCheck()
    index=stampNumber-1
    asp=stampImageArray[index].get_height()/stampImageArray[index].get_width()
    draw.rect(toolSet3Surface, surfaceColor, (stampIconRect[index].x, stampIconRect[index].y, stampIconRect[index].width, stampIconRect[index].height+13))
    draw.rect(toolSet3Surface, CLICKEDBLUE, stampIconRect[index],1)
    toolSet3Surface.blit(transform.smoothscale(stampImageArray[index], (60,60)), (stampIconRect[index].x, stampIconRect[index].y))
    #toolSet3Surface.blit(transform.smoothscale(stampImageArray[index], (60,60)), (stampIconRect[index].x, stampIconRect[index].y))

    tempTextObj = iconFont.render(stampText[index], True, CLICKEDBLUE)
    toolSet3Surface.blit(tempTextObj, (stampIconRect[index].x + stampIconRect[index].width/2 - iconFont.size(stampText[index])[0]/2, stampIconRect[index].y + stampIconRect[index].height + 3))
    #toolSet3Surface.blit(transform.scale(stampImageArray[index], (40*int(round((stampImageArray[index].get_height()/stampImageArray[index].get_width()))),40)), (stampIconRect[index].x, stampIconRect[index].y))
    t3Blit()

def canvasBlit(surface=canvasSurface):
    screen.blit(surface, (200,100))

moveBox=False#flag variable to move the slider box
copyNeeded=False#flag variable for resetting the canvas
copyNeededCount=1

pressing=False#flag variable to see if ur pressing icons
clicked=False#flag variable to see if ur clicking the canvas

fillReset=False#flag to see if the fill tool needed a reset after being clicked

clickCount=0#count the clicks for the rect tool
ovalClickCount=0#count clicks for oval tool
loadClickCount=0#count clicks for the load tool
loadPress=False#flag to see if the load was pressed
press=False#flag to see if save was pressed

square=False#flags to control the spect ratio for box and circle if shift is held
circle=False

holdX,holdY=False,False#bools for hold straight control on lines

saveResetNeeded=False# see if icons need reseting
loadResetNeeded=False

aspectLock=False#flag for aspect ration lock

colorCopyNeeded=False#flag for a color copy being needed

moveDarkness=False#flag for darkness slider being moved
canvasPressed=False#flag for canvas being pressed

smx=0#color cursor mouse coordinates
smy=0

colorCopiesMadeCount=0#counter to see if color copies are needed/already done

paintIconReset=False#flags to see if affected function icons need reseting
undoIconReset=False
redoIconReset=False

movePolygonBox=False#flag to see if polygon slider was moved
polygonToolClicked=False#flag to see if the polygon tool was clicked

clear=False#is screen being cleared

floodFill=False#flag to see if fill is flood fill

canvasClearNeeded=False#flag to see if the canvas must be cleared

moreRed=False#flags to see if any of the custom color icons were triggered
moreGreen=False
moreBlue=False
lessRed=False
lessGreen=False
lessBlue=False

sides=5



while running:#while the program is running
    for evt in event.get():#gets all events occuring every frame
        #print(evt)
        if evt.type==QUIT:#if you quit, then leave
            running=False
        if evt.type==MOUSEBUTTONUP:#if the mouse button is released. In ever if statement below, the icons are reset
            pressing=False
            moveBox=False#reset all flag variables
            movePolygonBox=False
            moveDarkness=False
            canvasPressed=False
            if canvasClearNeeded:#if the canvas is supposed to be cleared due to the trash icon
                canvasClearNeeded=False
                trashIconReset()
                undoArrayAddition()
                canvasSurface.fill(WHITE)
                canvasCopy.fill(WHITE)
                canvasBlit()
            if moreBlue:#the next six if statements refer to the custom color icons and change the color according to those icons. Inside, flags are reset as well
                moreBlue=False
                blueIconReset()
                selectedColor=(selectedColor[0], selectedColor[1], min(selectedColor[2]+1,255))
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if moreGreen:
                moreGreen=False
                greenIconReset()
                selectedColor=(selectedColor[0], min(selectedColor[1]+1,255), selectedColor[2])
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if moreRed:
                moreRed=False
                redIconReset()
                selectedColor=(min(selectedColor[0]+1,255), selectedColor[1], selectedColor[2])
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if lessBlue:
                lessBlue=False
                lessBlueIconReset()
                selectedColor=(selectedColor[0], selectedColor[1], max(selectedColor[2]-1,0))
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if lessGreen:
                lessGreen=False
                lessGreenIconReset()
                selectedColor=(selectedColor[0], max(selectedColor[1]-1,0), selectedColor[2])
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if lessRed:
                lessRed=False
                lessRedIconReset()
                selectedColor=(max(selectedColor[0]-1,0), selectedColor[1], selectedColor[2])
                colorSelectBlockUpdate()
                updateColorWheel()#to update text
            if fillReset:#if the fill icon needs to be reset, reset it to the appropriate toggle
                if filled:
                    unfilledReset()
                else:
                    filledReset()
                fillReset=False
            if saveResetNeeded:# if save was triggered
                saveReset()
                try:#try to save it to the specified file name
                    fname=filedialog.asksaveasfilename(defaultextension=".png")
                    image.save(canvasSurface, fname)
                except:#if the user is dumb and does something dumb then just ignore them they dont deserve a saved file
                    pass#prevents crashing in the event of failure
                saveResetNeeded=False
            if loadResetNeeded:# if load was triggered
                loadReset()
                fname=filedialog.askopenfilename(filetypes=[("Images","*.png; *.bmp; *.jpg; *.jpeg")])#list of accepted file names
                if fname!="":# if the file name isnt nothing
                    loadedImages.insert(0,image.load(fname))#insert this image at the start of the loaded images array
                    loadedImages.pop()
                loadBarReset()#reset load bar
                loadResetNeeded=False
            if undoIconReset:# if undo is triggered
                undoReset()
                if len(undoArray)>0:#if undo array isnt empty
                    canvasCopy=undoArray[-1]#perform undo
                    undoIconReset=False
                    undoArrayActivate()
            if redoIconReset:# if redo is triggered
                redoReset()
                if len(redoArray)>0:#if redo array isnt empty
                    canvasCopy=redoArray[-1]#perform redo
                    redoIconReset=False
                    redoArrayActivate()
            elif tool=="colorGrab":#if the tool is colorgrab
                colorGrabIconReset()
            elif tool=="pencil":#if pencil is activated
                pencilReset()
            elif tool=="eraser":#eraser triggered
                eraserReset()
            elif tool=="line":#line triggered
                lineReset()
            elif tool=="box":#box triggered
                boxReset()
                press=False
                if clickCount==2:#if its the final click
                    if filled:# if its filled, then just draw the rectangle
                        newRect=Rect(startX,startY,mx-startX-canvasRect.x,my-startY-canvasRect.y)
                        draw.rect(canvasSurface, selectedColor, newRect)
                    else:# if it isnt
                        if mx-startX-canvasRect.x<0:#manually normalize (no one told me about normalize so i just did this and now i refuse to change it)
                            if my-startY-canvasRect.y<0:
                                newRect=Rect(mx-canvasRect.x, my-canvasRect.y, startX-(mx-canvasRect.x), startY-(my-canvasRect.y))
                            else:
                                newRect=Rect(mx-canvasRect.x, startY, startX-(mx-canvasRect.x), my-startY-canvasRect.y)
                        else:
                            if my-startY-canvasRect.y<0:
                                newRect=Rect(startX, my-canvasRect.y, mx-startX-canvasRect.x, startY-(my-canvasRect.y))
                            else:
                                newRect=Rect(startX, startY, mx-startX-canvasRect.x, my-startY-canvasRect.y)#yes
                        if newRect.width>=thickness and newRect.height>=thickness:
                            for t in range(thickness):
                                draw.rect(canvasSurface, selectedColor, (newRect.x+t, newRect.y+t, newRect.width-t*2, newRect.height-t*2),1)#draw several rects based on thickness. this gets rid of the glitch in pygame where boxes cant go over a certain width without breaking
                    canvasBlit()
                    clickCount=0
            elif tool=="oval":
                ovalReset()
                press=False
                if ovalClickCount==2:#if its the final click
                    try:#try this. THere are sometimes errors with width radius. I could manually check for this, but i think this is inaccurate for the user. If the user asks for something impossible, then give them nothing, not a misrepresentation of the truth
                        if filled:#if its filled the width arg is 0. Else, its just the thcikness
                            width=0
                        else:
                            width=thickness
                        if circle==False:# if it isnt a circle
                            if mx-startX-canvasRect.x<0:
                                if my-startY-canvasRect.y<0:#manually normalize
                                    newRect=Rect(mx-canvasRect.x, my-canvasRect.y, startX-(mx-canvasRect.x), startY-(my-canvasRect.y))
                                else:
                                    newRect=Rect(mx-canvasRect.x, startY, startX-(mx-canvasRect.x), my-startY-canvasRect.y)
                            else:
                                if my-startY-canvasRect.y<0:
                                    newRect=Rect(startX, my-canvasRect.y, mx-startX-canvasRect.x, startY-(my-canvasRect.y))
                                else:
                                    newRect=Rect(startX, startY, mx-startX-canvasRect.x, my-startY-canvasRect.y)#yes
                            if filled:
                                draw.ellipse(canvasSurface, selectedColor, newRect)#draw rect as per newRect
                            else:
                                selectedColor=(selectedColor[0], selectedColor[1], selectedColor[2], 255)#draw filled rect with transparent in centre to avoid gross oval
                                ellipseSurface=Surface((newRect.width, newRect.height), SRCALPHA)
                                draw.ellipse(ellipseSurface, selectedColor, (0,0,newRect.width, newRect.height))
                                draw.ellipse(ellipseSurface, (255,255,255,0), (thickness, thickness, newRect.width-thickness*2, newRect.height-thickness*2))
                                canvasSurface.blit(ellipseSurface, (newRect.x, newRect.y))
                                canvasBlit()
                                
                                #pygame.gfxdraw.aaellipse(canvasSurface, newRect.x+int(newRect.width/2), newRect.y+int(newRect.height/2), int(newRect.width/2), int(newRect.width/2), selectedColor)
                        #print(newRect)
                        canvasBlit()
                    except:
                        pass#prevent doing anything if the user's input doesnt work
                    try:#if its a circle, do everything the same as above, but contrain the height argument to be proportional to the width
                        if circle:
                            tmx=mx-canvasRect.x
                            tmy=startY+(tmx-startX)
                            if filled:
                                width=0
                            else:
                                width=thickness
                            if (mx-canvasRect.x)-startX<0:
                                if (my-canvasRect.y)-startY<0:
                                    tmy=startY-(startX-tmx)
                                    newRect=(tmx+round((startX-tmx)*.5), tmy+round((startY-tmy)*.5), round((startY-tmy)*.5))
                                    draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                                else:
                                    tmy=startY+(startX-tmx)
                                    newRect=(tmx+round((startX-tmx)*.5), tmy-round((tmy-startY)*.5), round((tmy-startY)*.5))
                                    draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                            else:
                                if (my-canvasRect.y)-startY<0:
                                    tmy=startY-(tmx-startX)
                                    newRect=(tmx-round((tmx-startX)*.5), tmy+round((startY-tmy)*.5), round((startY-tmy)*.5))
                                    draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                                else:
                                    newRect=(tmx-round((tmx-startX)*.5),tmy-round((tmy-startY)*.5), round((tmy-startY)*.5))
                                    draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                            canvasBlit()
                            #this works
                    except ValueError:
                        pass
                    ovalClickCount=0
            elif tool=="brush":#if brush reset brush
                brushReset()
            elif tool=="calligraphy":
                calligraphyReset()
            #if load or stamp is triggered
            elif tool=="load1" or tool=="load2" or tool=="load3" or tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6" or tool=="stamp7" or tool=="stamp8" or tool=="stamp9" or tool=="stamp10" or tool=="stamp11":
                loadPress=False
                loadBarReset()
                if loadClickCount==2:# if its the final click
                    try:#as with the ellipse, if they ask for something impossible, dont give it to them
                        if tool=="load1" or tool=="load2" or tool=="load3":#if its load, access the load array to find the image and add it to the screen. 
                            if tool=="load1":
                                index=0
                            elif tool=="tool2":
                                index=1
                            else:
                                index=2
                            if aspectLock:#if theres an aspect lock, transform it only to locked specifications that are proportional
                                tempImage=transform.scale(loadedImages[index], (mx-canvasRect.x-startX, round((mx-canvasRect.x-startX)*aspectRatio)))
                                
                            else:
                                tempImage=transform.scale(loadedImages[index], (mx-canvasRect.x-startX, my-canvasRect.y-startY))
                        else:#if stamp
                            if tool=="stamp1":#get index in array
                                index=0
                            elif tool=="stamp2":
                                index=1
                            elif tool=="stamp3":
                                index=2
                            elif tool=="stamp4":
                                index=3
                            elif tool=="stamp5":
                                index=4
                            elif tool=="stamp6":
                                index=5
                            elif tool=="stamp7":
                                index=6
                            elif tool=="stamp8":
                                index=7
                            elif tool=="stamp9":
                                index=8
                            elif tool=="stamp10":
                                index=9
                            elif tool=="stamp11":
                                index=10

                            if aspectLock:#if theres an apsect lock, transofrm image proportionally
                                tempImage=transform.scale(stampImageArray[index], (mx-canvasRect.x-startX, round((mx-canvasRect.x-startX)*aspectRatio)))
                            else:
                                tempImage=transform.scale(stampImageArray[index], (mx-canvasRect.x-startX, my-canvasRect.y-startY))
                        canvasSurface.blit(tempImage, (startX, startY))#blit whatever image was just retreieved
                        canvasBlit()
                    except:
                        pass
                    loadClickCount=0
            if tool=="polygon":#if polygon
                polygonReset()
                if polygonToolClicked:#if you click the polygon tool
                    polygonToolClicked=False
                    undoArrayAddition()#add to undo array
                    polygonPointsArray=[]
                    quadrant=0 # is NOT correlated with caesarian plane
                    polygonSurface=Surface((thickness*2, thickness*2), SRCALPHA)#make a surface for the polygon at its max size rectangularily
                    polygonSurfaceRect=Rect(mx-canvasRect.x-thickness, my-canvasRect.y-thickness, thickness*2, thickness*2)
                    for s in range(sides):#this is all code that makes a list of points that are on the regular polygon
                        theta=360/sides*s #It searchs around by an equal angle going clockwise, collecting points on the polygon basd on the polygon being joined chords of a circle
                        if theta<90:
                            quadrant=1
                        elif theta<180:#assign quadrant basled on angle 
                            quadrant=2
                        elif theta<270:
                            quadrant=3
                        elif theta<360:
                            quadrant=4
                        #if theta>45:
                            #theta=90-theta
                        #print(theta)
                        if quadrant==1:
                            if theta==0:
                                theta=90
                            theta=90-theta
                        elif quadrant==2:
                            theta-=90
                        elif quadrant==3:
                            theta-=180
                            if theta==0:
                                theta=90
                            theta=90-theta
                        else:
                            theta-=270
                        #print(theta,s)
                        if theta!=0:
                            if quadrant==1 or quadrant==2:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+cos(radians(theta))*thickness)#get coordinate and save it based on qusdtrant
                            else:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-cos(radians(theta))*thickness)
                            if quadrant==1 or quadrant==4:
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y-sin(radians(theta))*thickness)
                            else:
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y+sin(radians(theta))*thickness)
                        else:
                            if quadrant==1:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y-thickness)
                            elif quadrant==2:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+thickness)
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                            elif quadrant==3:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y+thickness)
                            elif quadrant==4:
                                xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-thickness)
                                yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                        polygonPointsArray=[(xCoord, yCoord)]+polygonPointsArray#add to points array
                    draw.polygon(polygonSurface, selectedColor, polygonPointsArray)#draw thne polygon
                    if filled==False:# if it isnt filled, do all of the same things, but then have a filled polygon and a smaller transparent one in the centre. Not repeating comments. Its the same thing
                        polygonPointsArray=[]
                        tempThickness=thickness-3
                        for s in range(sides):
                            theta=360/sides*s
                            if theta<90:
                                quadrant=1
                            elif theta<180:
                                quadrant=2
                            elif theta<270:
                                quadrant=3
                            elif theta<360:
                                quadrant=4

                            if quadrant==1:
                                if theta==0:
                                    theta=90
                                theta=90-theta
                            elif quadrant==2:
                                theta-=90
                            elif quadrant==3:
                                theta-=180
                                if theta==0:
                                    theta=90
                                theta=90-theta
                            else:
                                theta-=270

                            if theta!=0:
                                if quadrant==1 or quadrant==2:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+cos(radians(theta))*tempThickness)
                                else:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-cos(radians(theta))*tempThickness)
                                if quadrant==1 or quadrant==4:
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y-sin(radians(theta))*tempThickness)
                                else:
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y+sin(radians(theta))*tempThickness)
                            else:
                                if quadrant==1:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y-tempThickness)
                                elif quadrant==2:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+tempThickness)
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                                elif quadrant==3:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y+tempThickness)
                                elif quadrant==4:
                                    xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-tempThickness)
                                    yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                            polygonPointsArray=[(xCoord, yCoord)]+polygonPointsArray
                        draw.polygon(polygonSurface, (0,0,0,0), polygonPointsArray)
                    canvasSurface.blit(polygonSurface, (polygonSurfaceRect.x, polygonSurfaceRect.y))
                    canvasBlit()
            elif tool=="spraypaint":#if spraypoint reset
                spraypaintReset()
            elif tool=="fill":#if fill then reset and fill
                fillIconReset()
                if clear==False:#if its a straight fill then just fill it as a color. check to ensure it isnt someone just tryna clear the screen via right click
                    if floodFill==False:
                        undoArrayAddition()#add to undmo arry and fill screen
                        canvasSurface.fill(selectedColor)
                    else:#####Flood fill. Source: Maconovik Edsby
                        undoArrayAddition()
                        rc=canvasSurface.get_at((mx-canvasRect.x,my-canvasRect.y)) #gets the colour of pixel where the user clicked 
                        spots=[(mx-canvasRect.x,my-canvasRect.y)] #the point clicked is part of the spots list
                        print(spots)
                        while len(spots)>0: #when the spots list has at least one element 
                            newSpots=[] #list of new spots
                            for fx,fy in spots:
                                if 0<=fx<canvasRect.width and 0<=fy<canvasRect.height and canvasSurface.get_at((fx,fy))==rc:  #if fx and fy are within the range of the canvas
                                    canvasSurface.set_at((fx,fy),selectedColor)                  #and the colour of the pixel of fx,fy is the same colour as
                                                                               #the inital one selected earlier, then begin to fill the area 
                                                 #right    #left      #down    #up
                                    newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy+1),(fx,fy-1)]  #these are the 4 points we fill
                                                                     #from the initial point
                                spots=newSpots #each time, from the newSpots, they become spots and the right, left, up and down of
                                            #these points are counted as newSpots and we colour in those pixels
                        canvasBlit()
            if tool=="stamp1":#check every stamp and then reset stamp
                stampIconReset(1)
            elif tool=="stamp2":
                stampIconReset(2)
            elif tool=="stamp3":
                stampIconReset(3)
            elif tool=="stamp4":
                stampIconReset(4)
            elif tool=="stamp5":
                stampIconReset(5)
            elif tool=="stamp6":
                stampIconReset(6)
            elif tool=="stamp7":
                stampIconReset(7)
            elif tool=="stamp8":
                stampIconReset(8)
            elif tool=="stamp9":
                stampIconReset(9)
            elif tool=="stamp10":
                stampIconReset(10)
            elif tool=="stamp11":
                stampIconReset(11)
            if paintIconReset:#reset paint icon if need
                paintIconReset=False
                updateColorIcon()
            textUpdate()
            clear=False
        if evt.type==KEYDOWN:
            if evt.key==K_LSHIFT or evt.key==K_RSHIFT:#checks for shift keys
                if tool=="line":#if line, determine if the angle is more vertical or horizontal and hold the x or y coordinate in place based on the start x and star y accordingly
                    if holdX==False and holdY==False:
                        dx=mx-startingX-canvasRect.x
                        dy=(my-startingY-canvasRect.y)*-1
                        if dx==0:
                            dx=.00001
                        theta=degrees(atan(dy/dx))
                        if abs(theta)>45:
                            holdX=True
                        else:
                            holdY=True
                elif tool=="box":#if box its a square
                    square=True
                elif tool=="load1" or tool=="load2" or tool=="load3" or tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6" or tool=="stamp7" or tool=="stamp8" or tool=="stamp9" or tool=="stamp10" or tool=="stamp11":
                    aspectLock=True#if its a load tool oor stamp, aspect lock
                elif tool=="oval":#if oval, its a circle
                    circle=True
                elif tool=="fill":#if its a fill, its a flood fill
                    floodFill=True
        if evt.type==KEYUP:
            if evt.key==K_LSHIFT or evt.key==K_RSHIFT:#checks for shift keys
                if holdX or holdY:#reset all appropriate flag variables
                    holdX=False
                    holdY=False
                if square:
                    square=False
                if aspectLock:
                    aspectLock=False
                if circle:
                    circle=False
                if floodFill:
                    floodFill=False
    leftClick,middleClick,rightClick=mouse.get_pressed()#get the left and right click events
    mx,my = mouse.get_pos()# get mouse pittion
    xySurfaceUpdate(mx,my)#update xy box

    if holdX or holdY:#if there is a restriction on the x and or y, basically dont change it and leave it as it shoudl be 
        if holdX:
            mx=startingX+canvasRect.x
        else:
            my=startingY+canvasRect.y
    if square:#if its supposed to be a square, make the y the same distance from start y as start x and x
        if my<=startY:
            my=startY+canvasRect.y-abs(mx-canvasRect.x-startX)
        else:
            my=startY+canvasRect.y+abs(mx-canvasRect.x-startX)
#################SELECTING TOOLS AND SETTINGS##################
    if leftClick==1:#if left click
        if canvasPressed==False:#if you arent on the canvas . In each of these statements, the clicked version of the icon is triggered, and if tool is every changed, then the tool for the canvas was also changed. these will not be commented. it will be very redundant for no reason
            if sliderRect.collidepoint(mx-toolSet2Rect.x-thicknessSliderRect.x,my-toolSet2Rect.y-thicknessSliderRect.y):#access the x and y relative to the sliderRect
                moveBox=True
            if polygonSliderBoxRect.collidepoint(mx-toolSet1Rect.x-polygonSliderRect.x, my-toolSet1Rect.y-polygonSliderRect.y):#moving polygon slider
                movePolygonBox=True
            if pencilRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#SELECT PENCIL
                pTool=tool#pencil is tool
                tool="pencil"
                clickedIcon(pressedPencilIcon, pencilRect, pencilText)
                
                #screen.blit(pencilTextSurface, (toolSet1Rect.x+pencilRect.x+pencilRect.width/2-iconFont.size(pencilText)[0]/2, toolSet1Rect.y+pencilRect.y+pencilRect.height+5))
            if eraserRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):# SELECT ERASER
                pTool=tool
                tool="eraser"
                clickedIcon(pressedEraserIcon, eraserRect, eraserText)
                
                #screen.blit(eraserTextSurface, (toolSet1Rect.x+eraserRect.x+eraserRect.width/2-iconFont.size(eraserText)[0]/2, toolSet1Rect.y+eraserRect.y+eraserRect.height+5))
            if lineRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):# SELECT LINE
                pTool=tool
                tool="line"
                clickedIcon(pressedLineIcon, lineRect, lineText)
            
            if filledRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#select fill
                fillReset=True
                if filled:
                    clickedIcon2(pressedFilledIcon, filledRect, filledText)
                else:
                    clickedIcon2(pressedUnfilledIcon, filledRect, unfilledText)
            if boxRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select rectangle
                pTool=tool
                tool="box"
                clickedIcon(pressedBoxIcon, boxRect, boxText)
                
            if ovalRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select oval
                pTool=tool
                tool="oval"
                clickedIcon(pressedOvalIcon, ovalRect, ovalText)
            if brushRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select brush
                pTool=tool
                tool="brush"
                clickedIcon(pressedBrushIcon, brushRect, brushText)
            if polygonRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select polygon
                pTool=tool
                tool="polygon"
                clickedIcon(pressedPolygonIcon, polygonRect, polygonText)
            if spraypaintRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select spraypaint
                pTool=tool
                tool="spraypaint"
                clickedIcon(pressedSpraypaintIcon, spraypaintRect, spraypaintText)
            if saveRect.collidepoint(mx,my):#select save
                clickedSave()
                saveResetNeeded=True
            if loadRect.collidepoint(mx,my):#select load
                clickedLoad()
                loadResetNeeded=True
            if load1Rect.collidepoint(mx-loadedImagesRect.x, my-loadedImagesRect.y):#select the load image1, (next is 2 and 3)
                pTool=tool
                tool="load1"
                clickedLoadedIcon(load1Rect,1)
            if load2Rect.collidepoint(mx-loadedImagesRect.x, my-loadedImagesRect.y):
                pTool=tool
                tool="load2"
                clickedLoadedIcon(load2Rect,2)
            if load3Rect.collidepoint(mx-loadedImagesRect.x, my-loadedImagesRect.y):
                pTool=tool
                tool="load3"
                clickedLoadedIcon(load3Rect,3)
            if selectorRect.collidepoint(mx-colorSliderRect.x, my-colorSliderRect.y):#if darkness slider is moving
                moveDarkness=True
            if paintBrushIconRect.collidepoint(mx,my):#select paint brush/color toggle
                paintIconReset=True
                colorIconClicked()
            if undoRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#select undo
                undoIconReset=True
                clickedIcon2(pressedUndoIcon, undoRect, undoText)
            if redoRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#select redo
                redoIconReset=True
                clickedIcon2(pressedRedoIcon, redoRect, redoText)
            if calligraphyRect.collidepoint(mx-toolSet1Rect.x, my-toolSet1Rect.y):#select calligraphy
                pTool=tool
                tool="calligraphy"
                clickedIcon(pressedCalligraphyIcon, calligraphyRect, calligraphyText)
            if colorGrabIconRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#if color grab is selected
                pTool=tool
                tool="colorGrab"
                clickedIcon2(pressedColorGrabIcon, colorGrabIconRect, colorGrabIconText)
            if fillIconRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#select fill
                pTool=tool
                tool="fill"
                clickedIcon2(pressedFillIcon, fillIconRect, fillIconText)
            if trashIconRect.collidepoint(mx-toolSet2Rect.x, my-toolSet2Rect.y):#select clear
                clickedIcon2(pressedTrashIcon, trashIconRect, trashIconText)
                canvasClearNeeded=True
            if blueIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):#select the custom color icons (this and 5 below it)
                moreBlue=True
                customIconClicked(blueIcon, blueIconRect)
            if greenIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):
                moreGreen=True
                customIconClicked(greenIcon, greenIconRect)
            if redIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):
                moreRed=True
                customIconClicked(redIcon, redIconRect)
            if lessBlueIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):
                lessBlue=True
                customIconClicked(lessBlueIcon, lessBlueIconRect)
            if lessGreenIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):
                lessGreen=True
                customIconClicked(lessGreenIcon, lessGreenIconRect)
            if lessRedIconRect.collidepoint(mx-customColorRect.x, my-customColorRect.y):
                lessRed=True
                customIconClicked(lessRedIcon, lessRedIconRect)
            
            if stamp1IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):#select stamps. Make stamp tool, add effect to respective stamp
                pTool=tool
                tool="stamp1"
                stampIconClicked(1)
            if stamp2IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp2"
                stampIconClicked(2)
            if stamp3IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp3"
                stampIconClicked(3)
            if stamp4IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp4"
                stampIconClicked(4)
            if stamp5IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp5"
                stampIconClicked(5)
            if stamp6IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp6"
                stampIconClicked(6)
            if stamp7IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp7"
                stampIconClicked(7)
            if stamp8IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp8"
                stampIconClicked(8)
            if stamp9IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp9"
                stampIconClicked(9)
            if stamp10IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp10"
                stampIconClicked(10)
            if stamp11IconRect.collidepoint(mx-toolSet3Rect.x, my-toolSet3Rect.y):
                pTool=tool
                tool="stamp11"
                stampIconClicked(11)
        if canvasRect.collidepoint(mx,my):#TOUCHING THE CANVAS
            ########PENCIL TOOL######
            if tool=="pencil":#this is drawing with pencil tool. sharp lines. 
                if canvasPressed==False:
                    undoArrayAddition()
                canvasPressed=True
                draw.line(canvasSurface,selectedColor,(mx-canvasRect.x,my-canvasRect.y),(omx-canvasRect.x,omy-canvasRect.y),thickness)#dra wline from omx and mx
                canvasBlit()
                
            if tool=="eraser":#this is eraser. gets rid of mistakes
                if canvasPressed==False:
                    undoArrayAddition()
                canvasPressed=True  
                dx=mx-omx
                dy=my-omy
                distance=int((dx**2+dy**2)**.5)
                for x in range(1,distance):
                    dotX=int(omx+x*dx/distance) #(run)
                    dotY=int(omy+x*dy/distance) #(rise)
                    draw.circle(canvasSurface, WHITE, (dotX-canvasRect.x, dotY-canvasRect.y), thickness)#draw several circlesbetween omx and mx and omy and my in a line
                canvasBlit()
            if tool=="line":#line tool. Makes straight lines
                if pressing==False:
                    if clicked==False:#on first click establish start x and y
                        if canvasPressed==False:
                            undoArrayAddition()
                        canvasPressed=True
                        startingX=mx-canvasRect.x
                        startingY=my-canvasRect.y
                        clicked=True
                    else:#if there is no final click, show user prospective line 
                        canvasPressed=True
                        draw.line(canvasSurface, selectedColor, (startingX, startingY), (mx-canvasRect.x,my-canvasRect.y), thickness)
                        canvasBlit()
                        clicked=False
                    pressing=True
            if tool=="box":#rect/square tool
                if clickCount==0 and press==False:#first click - establish start x and y
                    if canvasPressed==False:
                        undoArrayAddition()
                    canvasPressed=True
                    startX=mx-canvasRect.x
                    startY=my-canvasRect.y
                    press=True
                    clickCount+=1
                elif clickCount==1 and press==False:#second click, add one to the click count and wait for button release
                    canvasPressed=True
                    clickCount+=1
                    press=True
            if tool=="oval":#oval tool
                if ovalClickCount==0:#if there are no clicks, ho,d the start x and y
                    if canvasPressed==False:
                        undoArrayAddition()
                    canvasPressed=True
                    ovalClickCount+=1
                    startX=mx-canvasRect.x
                    startY=my-canvasRect.y
                    press=True
                elif ovalClickCount==1 and press==False:#if its second click, wait fro the release of the users button
                    canvasPressed=True
                    ovalClickCount+=1
                    press=True
            if tool=="brush":#brush tool is like pencil but works for all sizes and looks nice
                if canvasPressed==False:
                    undoArrayAddition()
                canvasPressed=True
                dx=mx-omx
                dy=my-omy
                distance=int((dx**2+dy**2)**.5)#works same as eraser but with color. draw several circles between omx and omy and mx and my
                for x in range(1,distance):
                    dotX=int(omx+x*dx/distance) #(run)
                    dotY=int(omy+x*dy/distance) #(rise)
                    draw.circle(canvasSurface, selectedColor, (dotX-canvasRect.x, dotY-canvasRect.y), thickness)
                draw.circle(canvasSurface, selectedColor, (mx-canvasRect.x, my-canvasRect.y), thickness)
                canvasBlit()
            elif tool=="load1" or tool=="load2" or tool=="load3" or tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6" or tool=="stamp7" or tool=="stamp8" or tool=="stamp9" or tool=="stamp10" or tool=="stamp11":
                #if load or stamp tool
                if tool=="load1" or tool=="load2" or tool=="load3":#if load tool
                    if tool=="load1":#determine index in array
                        index=0
                    elif tool=="load2":
                        index=1
                    else:
                        index=2
                    if loadClickCount==0 and loadPress==False:#if its the first click, get the start x and y as well as the aspect ratio of the image
                        if canvasPressed==False:
                            undoArrayAddition()
                        canvasPressed=True
                        loadClickCount+=1
                        startX=mx-canvasRect.x
                        startY=my-canvasRect.y
                        aspectRatio=loadedImages[index].get_size()[1]/loadedImages[index].get_size()[0]
                        loadPress=True
                    if loadClickCount==1 and loadPress==False:
                        canvasPressed=True
                        loadClickCount+=1
                        loadPress=True
                else:#if its the stamp tool
                    if tool=="stamp1":#get the index from the stamp array
                        index=0
                    elif tool=="stamp2":
                        index=1
                    elif tool=="stamp3":
                        index=2
                    elif tool=="stamp4":
                        index=3
                    elif tool=="stamp5":
                        index=4
                    elif tool=="stamp6":
                        index=5
                    elif tool=="stamp7":
                        index=6
                    elif tool=="stamp8":
                        index=7
                    elif tool=="stamp9":
                        index=8
                    elif tool=="stamp10":
                        index=9
                    elif tool=="stamp11":
                        index=10
                    if loadClickCount==0:#if first click, get start X and startY as well as find out aspect ratio
                        if canvasPressed==False:
                            undoArrayAddition()
                        canvasPressed=True
                        loadClickCount+=1
                        startX=mx-canvasRect.x
                        startY=my-canvasRect.y
                        aspectRatio=stampImageArray[index].get_size()[1]/stampImageArray[index].get_size()[0]
                        loadPress=True
                    if loadClickCount==1 and loadPress==False:#if second click, wait fro user to release second button
                        canvasPressed=True
                        loadClickCount+=1
                        loadPress=True
            elif tool=="calligraphy":#if calligraphy tool
                if canvasPressed==False:
                    undoArrayAddition()
                canvasPressed=True
                if thickness == 1:#thickness is either one or half of whateveer it shoudl be 
                    thick = 1
                else:
                    thick = thickness//2
                dx=mx-omx
                dy=my-omy
                distance=int((dx**2+dy**2)**.5)#same idea as the brush tool but instead of circles, draw lines. this creates a nice cursive effect
                for x in range(1,distance):
                    dotX=int(omx+x*dx/distance) #(run)
                    dotY=int(omy+x*dy/distance) #(rise)
                    cx,cy = (dotX-canvasRect.x, dotY-canvasRect.y)
                    draw.line(canvasSurface, selectedColor, (cx-thickness, cy-thickness), (cx+thickness, cy+thickness), thick)
                cx,cy = (mx-canvasRect.x, my-canvasRect.y)
                draw.line(canvasSurface, selectedColor, (cx-thickness, cy-thickness), (cx+thickness, cy+thickness), thick)
                canvasBlit()
            elif tool=="spraypaint":#if spraypaint tool is the tool
                if canvasPressed==False:
                    undoArrayAddition()
                canvasPressed=True
                dx=mx-omx
                dy=my-omy
                distance=int((dx**2+dy**2)**.5)#do everything the same as the brush tool and all other similar tools, but instead of drawing circles
                for x in range(1,distance):    #generate random numbers inside of a circle and draw little circles
                    dotX=int(omx+x*dx/distance) #(run)
                    dotY=int(omy+x*dy/distance) #(rise)
                    for n in range(30):
                        while True:
                            randX=randint(dotX-canvasRect.x-thickness, dotX-canvasRect.x+thickness)#generate rand x and rand y
                            randY=randint(dotY-canvasRect.y-thickness, dotY-canvasRect.y+thickness)
                            tempX, tempY = randX+canvasRect.x-dotX, randY+canvasRect.y-dotY
                            if tempX**2+tempY**2<=thickness**2:#if the rand x and y arent in the circle then do it again
                                break
                        draw.circle(canvasSurface, selectedColor, (randX, randY), 1)#draw a small circle at the randx and randy
                    #draw.circle(canvasSurface, selectedColor, (dotX-canvasRect.x, dotY-canvasRect.y), thickness)
                
                for n in range(50):
                    while True:
                        randX=randint(mx-canvasRect.x-thickness, mx-canvasRect.x+thickness)#all of this is a repeat of the previous code for the place the mouse is currently
                        randY=randint(my-canvasRect.y-thickness, my-canvasRect.y+thickness)
                        tempX, tempY = randX+canvasRect.x-mx, randY+canvasRect.y-my
                        if tempX**2+tempY**2<=thickness**2:
                            break
                    draw.circle(canvasSurface, selectedColor, (randX, randY), 1)
                
                canvasBlit()
            elif tool=="colorGrab":#if the tool is color grab, take the color at the mx and mx when clicked and make that the selected color
                selectedColor=canvasSurface.get_at((mx-canvasRect.x, my-canvasRect.y))
                colorSelectBlockUpdate()
            if tool=="polygon":#if its polygon, trigger a flag and wait for the mouse to release
                if polygonToolClicked==False:
                    polygonToolClicked=True

                    
    if rightClick==1 and canvasRect.collidepoint(mx,my):#right click to clear
        clear=True#flag to avoid setting off fill if thats the tool
        canvasSurface.fill(WHITE)#fill with white to clear
        canvasBlit()#b-lit
########DARKNESS SLIDER#########
    
    if moveDarkness:#if the slider is being movied, make the tempPos the xlocation of the little dragger rectangle and run that x value in the colorSlider Update
        tempPos=selectorRect.x
        tempPos+=mx-omx
        darkness=int(round(tempPos/(colorSliderRect.width-6)*101))
        
        colorSliderUpdate(tempPos)
##########COLOR WHEEL COLLISION#############

    if wheelCollide():#if the user collides with the color wheel 
        colorCopyNeeded=True
        colorCursorNeeded=True
        colorCopiesMadeCount=0
        cmx=mx-colorWheelRect.x#color wheel mx and my and then the surface mx and my
        cmy=my-colorWheelRect.y
        smx=cmx
        smy=cmy+40
        if leftClick==1:#if theres a click, grab the color and make that the selected color
            selectedColor=editColorWheel.get_at((cmx,cmy))
            colorSelectBlockUpdate()
        
    elif wheelCollide()==False and colorCopiesMadeCount<2:#if it isnt on the wheel, then no colo copies are needed anymore ( color copies were needed for the cursor)
        colorCursorNeeded=False
    

                
            

    if canvasRect.collidepoint(mx,my):#if the user is touching the canvas, but isnt pressing anything nessesarily
        canvasCopy=canvasSurface.copy()#make a canvas copy. From now on we will be working on the canvas but it will later be replaced
        copyNeeded=True
        copyNeededCount=0
        if tool=="pencil":#if the tool is pencil, show a pencil
            canvasSurface.blit(pencilIcon, (mx-canvasRect.x,my-pencilIcon.get_height()-canvasRect.y+3))
            canvasBlit()
        elif tool=="eraser":#if the tool is eraser,show a circle
            draw.circle(canvasSurface, BLACK, (mx-canvasRect.x, my-canvasRect.y), thickness, 1)
            canvasBlit()
        elif tool=="line":#show prospective lines after first click
            if clicked:
                draw.line(canvasSurface, selectedColor, (startingX, startingY), (mx-canvasRect.x, my-canvasRect.y),thickness)
                canvasBlit()
        elif tool=="box":#show the outline of the square or rect ablut to be created
            if clickCount==1:
                if filled:
                    newRect=Rect(startX,startY,mx-startX-canvasRect.x,my-startY-canvasRect.y)
                    draw.rect(canvasSurface, selectedColor, newRect)
                else:
                    if mx-startX-canvasRect.x<0:
                        if my-startY-canvasRect.y<0:
                            newRect=Rect(mx-canvasRect.x, my-canvasRect.y, startX-(mx-canvasRect.x), startY-(my-canvasRect.y))
                        else:
                            newRect=Rect(mx-canvasRect.x, startY, startX-(mx-canvasRect.x), my-startY-canvasRect.y)
                    else:
                        if my-startY-canvasRect.y<0:
                            newRect=Rect(startX, my-canvasRect.y, mx-startX-canvasRect.x, startY-(my-canvasRect.y))
                        else:
                            newRect=Rect(startX, startY, mx-startX-canvasRect.x, my-startY-canvasRect.y)#yes
                    if newRect.width>=thickness and newRect.height>=thickness:
                        for t in range(thickness):
                            draw.rect(canvasSurface, selectedColor, (newRect.x+t, newRect.y+t, newRect.width-t*2, newRect.height-t*2),1)
                canvasBlit()
        elif tool=="oval":#show oval or circle ablut to be made
            if ovalClickCount==1:
                try:
                    if filled:
                        width=0
                    else:
                        width=thickness
                    if circle==False:
                        if mx-startX-canvasRect.x<0:
                            if my-startY-canvasRect.y<0:
                                newRect=Rect(mx-canvasRect.x, my-canvasRect.y, startX-(mx-canvasRect.x), startY-(my-canvasRect.y))
                            else:
                                newRect=Rect(mx-canvasRect.x, startY, startX-(mx-canvasRect.x), my-startY-canvasRect.y)
                        else:
                            if my-startY-canvasRect.y<0:
                                newRect=Rect(startX, my-canvasRect.y, mx-startX-canvasRect.x, startY-(my-canvasRect.y))
                            else:
                                newRect=Rect(startX, startY, mx-startX-canvasRect.x, my-startY-canvasRect.y)#yes
                        if filled:
                            draw.ellipse(canvasSurface, selectedColor, newRect)
                        else:
                            #for t in range(width*2):
                                #newRect=Rect(newRect.x+t/2, newRect.y+t/2, newRect.width-t, newRect.height-t)
                            selectedColor=(selectedColor[0], selectedColor[1], selectedColor[2], 255)
                            ellipseSurface=Surface((newRect.width, newRect.height), SRCALPHA)
                            draw.ellipse(ellipseSurface, selectedColor, (0,0,newRect.width, newRect.height))
                            draw.ellipse(ellipseSurface, (255,255,255,0), (thickness, thickness, newRect.width-thickness*2, newRect.height-thickness*2))
                            canvasSurface.blit(ellipseSurface, (newRect.x, newRect.y))
                            canvasBlit()
                            
                            #pygame.gfxdraw.aaellipse(canvasSurface, newRect.x+int(newRect.width/2), newRect.y+int(newRect.height/2), int(newRect.width/2), int(newRect.width/2), selectedColor)
                    #print(newRect)
                    canvasBlit()
                except:
                    pass
                try:
                    if circle:
                        tmx=mx-canvasRect.x
                        tmy=startY+(tmx-startX)
                        if filled:
                            width=0
                        else:
                            width=thickness
                        if (mx-canvasRect.x)-startX<0:
                            if (my-canvasRect.y)-startY<0:
                                tmy=startY-(startX-tmx)
                                newRect=(tmx+round((startX-tmx)*.5), tmy+round((startY-tmy)*.5), round((startY-tmy)*.5))
                                draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                            else:
                                tmy=startY+(startX-tmx)
                                newRect=(tmx+round((startX-tmx)*.5), tmy-round((tmy-startY)*.5), round((tmy-startY)*.5))
                                draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                        else:
                            if (my-canvasRect.y)-startY<0:
                                tmy=startY-(tmx-startX)
                                newRect=(tmx-round((tmx-startX)*.5), tmy+round((startY-tmy)*.5), round((startY-tmy)*.5))
                                draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                            else:
                                newRect=(tmx-round((tmx-startX)*.5),tmy-round((tmy-startY)*.5), round((tmy-startY)*.5))
                                draw.circle(canvasSurface, selectedColor, (newRect[0], newRect[1]), newRect[2], width)
                        canvasBlit()
                        #this works
                except ValueError:
                    pass

        elif tool=="brush":#show a circle
            draw.circle(canvasSurface, selectedColor, (mx-canvasRect.x,my-canvasRect.y), thickness, 1)
            canvasBlit()
        elif tool=="load1" or tool=="load2" or tool=="load3" or tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6" or tool=="stamp7" or tool=="stamp8" or tool=="stamp9" or tool=="stamp10" or tool=="stamp11":
            if tool=="load1" or tool=="load2" or tool=="load3":#show a model of what the image will look like if the user confirmed
                try:
                    if loadClickCount==1 and loadPress==False:
                        if aspectLock:
                            tempStampObj=transform.scale(loadedImages[index], (mx-canvasRect.x-startX, round((mx-canvasRect.x-startX)*aspectRatio)))
                        else:
                            tempStampObj=transform.scale(loadedImages[index],(mx-canvasRect.x-startX, my-canvasRect.y-startY))
                        canvasSurface.blit(tempStampObj, (startX, startY))
                        canvasBlit()
                except:
                    pass
            else:#show a model of what the image will look like if the user confirmed
                try:
                    if loadClickCount==1 and loadPress==False:
                        if aspectLock:
                            tempStampObj=transform.scale(stampImageArray[index], (mx-canvasRect.x-startX, round((mx-canvasRect.x-startX)*aspectRatio)))
                        else:
                            tempStampObj=transform.scale(stampImageArray[index],(mx-canvasRect.x-startX, my-canvasRect.y-startY))
                        canvasSurface.blit(tempStampObj, (startX, startY))
                        canvasBlit()
                except:
                    pass
        elif tool=="polygon":# show an outline of the polygon that would be saved on the canvas using the same math as before
            polygonPointsArray=[]
            quadrant=0 # is NOT correlated with caesarian plane
            polygonSurface=Surface((thickness*2, thickness*2), SRCALPHA)
            polygonSurfaceRect=Rect(mx-canvasRect.x-thickness, my-canvasRect.y-thickness, thickness*2, thickness*2)
            for s in range(sides):
                theta=360/sides*s
                if theta<90:
                    quadrant=1
                elif theta<180:
                    quadrant=2
                elif theta<270:
                    quadrant=3
                elif theta<360:
                    quadrant=4
                #if theta>45:
                    #theta=90-theta
                #print(theta)
                if quadrant==1:
                    if theta==0:
                        theta=90
                    theta=90-theta
                elif quadrant==2:
                    theta-=90
                elif quadrant==3:
                    theta-=180
                    if theta==0:
                        theta=90
                    theta=90-theta
                else:
                    theta-=270
                #print(theta,s)
                if theta!=0:
                    if quadrant==1 or quadrant==2:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+cos(radians(theta))*thickness)
                    else:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-cos(radians(theta))*thickness)
                    if quadrant==1 or quadrant==4:
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y-sin(radians(theta))*thickness)
                    else:
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y+sin(radians(theta))*thickness)
                else:
                    if quadrant==1:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y-thickness)
                    elif quadrant==2:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+thickness)
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                    elif quadrant==3:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y+thickness)
                    elif quadrant==4:
                        xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-thickness)
                        yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                polygonPointsArray=[(xCoord, yCoord)]+polygonPointsArray
            draw.polygon(polygonSurface, selectedColor, polygonPointsArray)
            if filled==False:
                polygonPointsArray=[]
                tempThickness=thickness-3
                for s in range(sides):
                    theta=360/sides*s
                    if theta<90:
                        quadrant=1
                    elif theta<180:
                        quadrant=2
                    elif theta<270:
                        quadrant=3
                    elif theta<360:
                        quadrant=4

                    if quadrant==1:
                        if theta==0:
                            theta=90
                        theta=90-theta
                    elif quadrant==2:
                        theta-=90
                    elif quadrant==3:
                        theta-=180
                        if theta==0:
                            theta=90
                        theta=90-theta
                    else:
                        theta-=270

                    if theta!=0:
                        if quadrant==1 or quadrant==2:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+cos(radians(theta))*tempThickness)
                        else:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-cos(radians(theta))*tempThickness)
                        if quadrant==1 or quadrant==4:
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y-sin(radians(theta))*tempThickness)
                        else:
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y+sin(radians(theta))*tempThickness)
                    else:
                        if quadrant==1:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y-tempThickness)
                        elif quadrant==2:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x+tempThickness)
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                        elif quadrant==3:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x)
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y+tempThickness)
                        elif quadrant==4:
                            xCoord=(mx-canvasRect.x-polygonSurfaceRect.x-tempThickness)
                            yCoord=(my-canvasRect.y-polygonSurfaceRect.y)
                    polygonPointsArray=[(xCoord, yCoord)]+polygonPointsArray
                draw.polygon(polygonSurface, (0,0,0,0), polygonPointsArray)
            canvasSurface.blit(polygonSurface, (polygonSurfaceRect.x, polygonSurfaceRect.y))
            canvasBlit()
        elif tool=="calligraphy":#if its calligraphy, show a quill
            canvasSurface.blit(quill, (mx-canvasRect.x, my-canvasRect.y-quill.get_height()))
            canvasBlit()
        elif tool=="spraypaint":#if spreaypaint, show a circle
            draw.circle(canvasSurface, BLACK, (mx-canvasRect.x, my-canvasRect.y), thickness, 1)
            canvasBlit()
        elif tool=="colorGrab":#if color grab show a swabber
            canvasSurface.blit(colorGrabIcon, (mx-canvasRect.x, my-canvasRect.y))
            canvasBlit()
        elif tool=="fill":#if fill, show a small bucket
            canvasSurface.blit(transform.smoothscale(fillIcon, (20,20)), (mx-canvasRect.x-10, my-canvasRect.y-10))#make bucket small
            canvasBlit()
    else:
        copyNeeded=False
        if copyNeededCount==0:#if there are no more copies needed to be made, blit back the canvas copy
            canvasSurface.blit(canvasCopy,(0,0))
            canvasBlit()
                
                
#################SLIDERS#################
    if moveBox:#if the box was moved, 
        if mx>toolSet2Rect.x+thicknessSliderRect.x and mx<toolSet2Rect.x+thicknessSliderRect.x+toolSet2Rect.width+thicknessSliderRect.width:
            sliderPos+=mx-omx#change the positiong of the box on the slider and in the variable. 
        if sliderPos<0:
            sliderPos=0
        elif sliderPos>149:
            sliderPos=149
        if tool=="line" and sliderPos>149/99*9:#restrict thickness for line to <10
            sliderPos=149/99*9
        if tool=="pencil" and sliderPos>149/99*4:#restrict thickness for pencil to <5
            sliderPos=149/99*4
        if tool=="calligraphy" and sliderPos!=149/99*3:#restrict thickness for callifraphy to 4
            sliderPos=149/99*3
        #if tool=="oval" and sliderPos>149/99*2 :
           # sliderPos=149/99*2
        thickness=int(round(sliderPos/149*99+1))
        thickSlider(sliderPos)#use the new variable value to actually change the thickness text and the thickness for tools
    if movePolygonBox:
        if mx>toolSet1Rect.x+polygonSliderRect.x and mx<toolSet1Rect.x+polygonSliderRect.x+toolSet1Rect.width+polygonSliderRect.width:
            polygonSliderPos+=mx-omx#change the positioning o the rect on the slider, and then use the polygonSLiderPos to trigger functions that 
        if polygonSliderPos<0:      #will effectively change the vbairable sides allowing it to work for the polygon tool as intended
            polygonSliderPos=0
        elif polygonSliderPos>149:
            polygonSliderPos=149
        sides=int(round(polygonSliderPos/149*17+3))#up to 20 sides, min 3 sides
        polygonSlider(polygonSliderPos)
        

###############SPECIAL CONDITIONS###########
    if tool=="line" and thickness>10:#if line thickness is somehow above 10, change thickness to 10
        thickness=10
        sliderPos=int(149/99*9)
        thickSlider(sliderPos)
    if tool=="pencil" and thickness>5:#if line thickness is somehow above 5, change it to 5
        thickness=5
        sliderPos=149/99*4
        thickSlider(sliderPos)
    if tool=="calligraphy" and thickness!=4:#if line thickness is somehow not 4, change it to 4
        thickness=4
        sliderPos=149/99*4
        thickSlider(sliderPos)

    if copyNeeded:#if there was a copy needed, blit the copy
        canvasSurface.blit(canvasCopy,(0,0))
 
    if colorCopyNeeded or colorCopiesMadeCount==1:# if the color wheel needed a copy, then basically give it one
        colorCopiesMadeCount+=1
        if colorCopiesMadeCount==2:
            colorCursorNeeded=False
        updateColorWheel()
        colorCopyNeeded=False


    
        
    
    omx,omy=mx,my#the old mx and my are now the same as the mx and my
    #myClock.tick(1)
    display.flip()
    #everything we "draw" is actually copied
                #to a place in RAM
            #display.flip copies that to the actual screen
            
quit() #closing the pygame window







    
