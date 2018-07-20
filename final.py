from pygame import *
from random import *
from tkinter import *
from textinput import *

# how to timing,surface
init()
#root = Tk()
#root.withdraw()#hide tk window
size = width, height = 1350, 800
green = 0, 255, 0
red = 255, 0, 0
black=0,0,0,255
blue = 0, 0, 255
white=255,255,255
wolve=229,228,223
chose=""
myfont = font.SysFont("monospace", 15)
screen = display.set_mode(size)
logo="harry"
logocol=black
canBuff1=screen

#title 
title = transform.scale(image.load("image/title.png"),(width,height))
screen.blit(title,(0,0)) 
display.flip()
#harry
harryPic=image.load("image/harry.jpg")
harryLo=image.load("image/LogoHP.png")
harryLoRec=Rect(width-70,5,70,70)
harryPicRec=Rect(0,50,200,400)

#wolverine
clawPic = image.load("image/claw.png")
wolverinePic=transform.scale(image.load("image/wolverine.jpg"), (200,400))
wolverinePicRec=Rect(0,50,200,400)
wolverineLo=transform.scale(image.load("image/wolverineLo.jpg"), (70,70))
wolverineLoRec=Rect(width-140,5,70,70)
wolverine1=image.load("image/wolverine1s.png")
wolverine1Rec=Rect(0,50,100,100)
wolverine2=image.load("image/wolverine2s.png")
wolverine2Rec=Rect(100,50,100,100)
magneto = image.load("image/magnetos.png")
magnetoRec = Rect(0,150,100,100)
magnetoO = image.load("image/magnetoOs.png")
magnetoORec = Rect(100,150,100,100)
charles1 = image.load("image/charles1s.png")
charles1Rec = Rect(0,250,100,100)
deadpool = image.load("image/deadpools.png")
deadpoolRec = Rect(100,250,100,100)

#christmas
santaLo = transform.scale(image.load("image/santa.png"), (70,70))
santaLoRec=Rect(width-210,5,70,70)
santa1Lo = transform.scale(image.load("image/santa.png"), (70,70))
santa1LoRec=Rect(100,50,100,100)
hatPic = transform.scale(image.load("image/hat.png"), (200,400))
hatPicRec=Rect(0,50,200,400)
tree = image.load("image/trees.png")
treeRec = Rect(0,50,100,100)
bell = image.load("image/bells.png")
bellRec = Rect(0,150,100,100)
snowman = image.load("image/snowmans.png")
snowmanRec = Rect(100,150,100,100)
snowman1 = image.load("image/snowman1s.png")
snowman1Rec = Rect(0,250,100,100)
santa2 = image.load("image/santa2s.png")
santa2Rec = Rect(100,250,100,100)
col=black
Fullscreen = False

toolSize=5
tool=""
mmode = "up"
x=0
y=0

canvasRec=Rect(200,80,width-200,height-180)
toolbar1=Rect(0,0,width,80)
toolbar2=Rect(200,height-100,width,height)
toolbar3=Rect(0,0,200,height)
portion=screen.subsurface(toolbar3)
#new
newRec = Rect(200,70,10,10)
#color 
colorPic = image.load("image/color.png")
colorRec = Rect(1150,745,200,100)

# Size
sizeRec = Rect(1150,705,200,40)
# tool
toolRec = Rect(300,0,40,40)
#eyedropper
#get color from where the mouse is
eyePic = image.load("image/eye.png")
for i in range(40):
	for j in range(40): 
		r,g,b,a = eyePic.get_at((i,j))
		if r==40 and g==45 and b==42: 
			draw.rect(eyePic,white,[i,j,2,2]) 
eyex=450
eyey=height-100
eyeSt=eyex,eyey
eyeRec = Rect(eyex,eyey,40,40)


#stamp
stampS=0
def stamp(mx,my):
#blit picture on the canvas
	global mmode, canBuff, x, y,chose
	if chose!="":
		if mmode == "up" and mouse.get_pressed()[0]==1:
			canBuff = screen.copy()
			mmode = "down"
		if mmode == "down" and mouse.get_pressed()[0]==0:
			mmode = "up"
		if mmode == "down":
			screen.blit(canBuff, (0,0))
			choseP = transform.scale(image.load("image/%s.png"%chose), (100+stampS,100+stampS))
			x = mx-choseP.get_width() / 2
			y = my-choseP.get_height() / 2
			screen.blit(choseP,(x,y))

#draw line
def dLine(mx,my):
#draw a straight line
	global mmode, canBuff, beforex, beforey
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		draw.line(screen, col, (beforex,beforey),(mx,my),toolSize)
dLinex=250
dLiney=height-50
dLineSt=dLinex,dLiney
dLineRec = Rect(dLinex,dLiney,40,40)

#draw circle
def dCircle(mx,my):
# draw a fill circle
	global mmode, canBuff, beforex, beforey,radius
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		radius=int(((mx-beforex)**2+(my-beforey)**2)**0.5)
		draw.circle(screen, col, (beforex,beforey),radius)
dCirclex=300
dCircley=height-50
dCircleSt=dCirclex,dCircley
dCircleRec = Rect(dCirclex,dCircley,40,40)

def dCircleE(mx,my):
# draw a unfill circle
	global mmode, canBuff, beforex, beforey,radius
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		radius=int(((mx-beforex)**2+(my-beforey)**2)**0.5)
		if radius > toolSize:
			draw.circle(screen, col, (beforex,beforey),radius,toolSize)
dCircleEx=350
dCircleEy=height-50
dCircleESt=dCircleEx,dCircleEy
dCircleERec = Rect(dCircleEx,dCircleEy,40,40)

#draw Rect
def dRect(mx,my):
#draw a fill rectangle
	global mmode, canBuff, beforex, beforey,wid,leng
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		wid=mx-beforex
		leng=my-beforey
		draw.rect(screen, col, [beforex,beforey,wid,leng])
dRectx=300
dRecty=height-100
dRectSt=dRectx,dRecty
dRectRec = Rect(dRectx,dRecty,40,40)

def dRectE(mx,my):
#draw a unfill rectangle
	global mmode, canBuff, beforex, beforey,wid,leng
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		wid=mx-beforex
		leng=my-beforey
		draw.rect(screen, col, [beforex,beforey,wid,leng],toolSize)
dRectEx=350
dRectEy=height-100
dRectESt=dRectEx,dRectEy
dRectERec = Rect(dRectEx,dRectEy,40,40)
#draw Triangle
def dTri(mx,my):
#draw a fill triangle
	global mmode, canBuff, beforex, beforey,dis
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		dis=int(((mx-beforex)**2+(my-beforey)**2)**0.5)
		point=[(beforex,beforey),(mx-dis,my),(mx+dis,my)]
		draw.polygon(screen, col, point)
dTrix=400
dTriy=height-50
dTriSt=dTrix,dTriy
dTriRec = Rect(dTrix,dTriy,40,40)

def dTriE(mx,my):
#draw a unfill triangle 
	global mmode, canBuff, beforex, beforey,dis
	if mmode == "up" and mouse.get_pressed()[0]==1:
		canBuff = screen.copy()
		beforex = mx 
		beforey = my 
		mmode = "down"
	if mmode == "down" and mouse.get_pressed()[0]==0:
		mmode = "up"
	if mmode == "down":
		screen.blit(canBuff, (0,0))
		dis=int(((mx-beforex)**2+(my-beforey)**2)**0.5)
		point=[(beforex,beforey),(mx-dis,my),(mx+dis,my)]
		draw.polygon(screen, col, point,toolSize)
dTriEx=400
dTriEy=height-100
dTriESt=dTriEx,dTriEy
dTriERec = Rect(dTriEx,dTriEy,40,40)

#fill
def fill(mx,my):
# fill a surface that has same color
	rc=screen.get_at((mx,my))
	
	spots = [(mx,my)] #list of points
	while len(spots)>0:
		print(len(spots))
		newSpots =[]
		for fx,fy in spots:			
			if 0<fx<width and 0<fy<height and screen.get_at((fx,fy))==rc:
				screen.set_at((fx,fy),col)		
				newSpots += [(fx+1,fy),(fx-1,fy),(fx,fy-1),(fx,fy+1)]
				#mark the 4 points for filling (right, left, up and down from the current point)
				
				
		spots = newSpots	
fillPic=transform.scale(image.load("image/fill.png"), (40,40))
fillRec = Rect(450,height-50,40,40)

#pencil
#basic tool, to draw lines
pencilPic=image.load("image/pencil.png")
def pencil(mx,my):
	dist=int(((mx-ox)**2+(my-oy)**2)**0.5)
	if dist<5:
		draw.circle(screen,col,(mx,my),toolSize)
	else:
		for cir in range(2,dist):
			cirx=int((mx-ox)*cir/dist)
			ciry=int((my-oy)*cir/dist)
			draw.circle(screen,col,(ox+cirx,oy+ciry),toolSize)
pencilx=250
pencily=height-100
pencilSt=pencilx,pencily
pencilRec=Rect(pencilx,pencily,40,40)

#spray
#draw random dot in a circle
sprayPic=image.load("image/spray.png")
def spray (mx,my):
	sprayx=randint(mx-toolSize-5,mx+toolSize+5)
	sprayy=randint(my-toolSize-5,my+toolSize+5)
	for i in range(8):
		if (sprayx-mx)**2+(sprayy-my)**2<=(toolSize+5)**2:
			draw.circle(screen,col,(sprayx,sprayy),1)
sprayx=200
sprayy=height-100
spraySt=sprayx,sprayy
sprayRec=Rect(sprayx,sprayy,40,40)

#eraser
eraserPic=transform.scale(image.load("image/eraser.png"), (40,40))
#eraserPic.set_colorkey(white)
def eraser (mx,my):
	draw.line(screen,white,(ox,oy),(mx,my),toolSize)
eraserx=200
erasery=height-50
eraserSt=eraserx,erasery
eraserRec=Rect(eraserx,erasery,40,40)

#claw 
def claw(mx,my):
#draw wolverine's claw, there is difference between left click and right click
	if mb[2]==1:
		dist=int(((mx-ox)**2+(my-oy)**2)**0.5)
		draw.circle(screen,col,(mx+20+toolSize,my+20+toolSize),toolSize)
		draw.circle(screen,col,(mx,my),toolSize)
		draw.circle(screen,col,(mx-20-toolSize,my-20-toolSize),toolSize)
		for cir in range(2,dist):
			cirx=int((mx-ox)*cir/dist)
			ciry=int((my-oy)*cir/dist)
			draw.circle(screen,col,(ox+cirx+toolSize+20,oy+ciry+toolSize+20),toolSize)
			draw.circle(screen,col,(ox+cirx,oy+ciry),toolSize)
			draw.circle(screen,col,(ox+cirx-toolSize-20,oy+ciry-toolSize-20),toolSize)
	if mb[0]==1:
		dist=int(((mx-ox)**2+(my-oy)**2)**0.5)
		draw.circle(screen,col,(mx+20+toolSize,my-20-toolSize),toolSize)
		draw.circle(screen,col,(mx,my),toolSize)
		draw.circle(screen,col,(mx-20-toolSize,my+20+toolSize),toolSize)
		for cir in range(2,dist):
			cirx=int((mx-ox)*cir/dist)
			ciry=int((my-oy)*cir/dist)
			draw.circle(screen,col,(ox+cirx+toolSize+20,oy+ciry-toolSize-20),toolSize)
			draw.circle(screen,col,(ox+cirx,oy+ciry),toolSize)
			draw.circle(screen,col,(ox+cirx-toolSize-20,oy+ciry+toolSize+20),toolSize)
clawx=150
clawy=height-100
clawSt=clawx,clawy
clawRec = Rect(clawx,clawy,40,40)

#brush
#draw transparent line
brushHead = Surface((100,100),SRCALPHA)
#draw.circle(brushHead,(255,255,255,10),(12,12),12)
brushPic = image.load("image/brush.png")
def brush(mx,my):
	col1,col2,col3,col4=col
	draw.circle(brushHead,(col1,col2,col3,10),(50,50),toolSize)
	dist=max(1,int(((mx-ox)**2+(my-oy)**2)**0.5))
	if ox != mx or oy != my:
		for cir in range(dist):
			cirx=int((mx-ox)*cir/dist)
			ciry=int((my-oy)*cir/dist)
			screen.blit(brushHead,(ox+cirx-50,oy+ciry-50))
brushx=500
brushy=height-50
brushSt=brushx,brushy
brushRec = Rect(brushx,brushy,40,40)

#pen
#adjust size depend on the speed
penPic = image.load("image/pen.png")
penSize=1
def pen(mx,my):
	global penSize
	dist=int(((mx-ox)**2+(my-oy)**2)**0.5)
	for cir in range(2,dist):
		penSize =  int(max(toolSize/10,toolSize*3-dist) ** .6) 
		if penSize == 0:
			penSize=1
		cirx=int((mx-ox)*cir/dist)
		ciry=int((my-oy)*cir/dist)
		draw.circle(screen,col,(ox+cirx,oy+ciry),penSize)
	draw.circle(screen,col,(mx,my),penSize)
penx=500
peny=height-100
penSt=penx,peny
penRec = Rect(penx,peny,40,40)

#save
#save your drawing
savePic = image.load("image/save.png")
def save():
	image.save(screen.subsurface(canvasRec),filedialog.asksaveasfilename(defaultextension=".png"))
	#saveP=screen.subsurface(canvasRec).copy()
	#fname = filedialog.asksaveasfilename(defaultextension=".png")

saveRec = Rect(10,height-50,40,40)

#open 
#open other file
openPic = image.load("image/open.png")
def openF():
	fname = filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
	openN = fname.find("image/")
	screen.set_clip(canvasRec)
	print(fname[openN:])
	openE = image.load(fname[openN:])
	screen.blit(openE,canvasRec)
openRec = Rect(10,height-100,40,40)
#music
stop = 0
playPic= image.load("image/play.png")
pausePic= image.load("image/pause.png")
xmen = mixer.Sound("music/xmen.ogg")
jingle = mixer.Sound("music/jingle.ogg")
harrysong = mixer.Sound("music/harrysong.ogg")
def musicPlay():
# to play the music
	channel=mixer.Channel(1)
	
	channel.play(sound)

sound = harrysong
musicPlay()
def musicpause():
#to pause and unpause music
	global stop, clicked
	
	if stop==1:
		stop=0
		mixer.unpause()
	else:
		stop=1
		mixer.pause()
musicRec = Rect(10,height-150,40,40)

#undo   
#a important tool for everything, to cancel the last step
undoPic = image.load("image/undo.png")
redoPic = image.load("image/redo.png")
undoL=[]
redoL=[]
undoPor=screen.subsurface(canvasRec)
def undo():
	undoEnd=len(undoL)-1
	if undoEnd != -1:
		screen.blit(undoL[undoEnd],canvasRec)
		redoL.append(undoL[undoEnd])
		del undoL[undoEnd]
def redo():
	redoEnd=len(redoL)-1
	if redoEnd != -1:
		screen.blit(redoL[redoEnd],canvasRec)
		undoL.append(redoL[redoEnd])
		del redoL[redoEnd]
undoRec = Rect(10,height-250,40,40)
redoRec = Rect(10,height-200,40,40)

#TEXT allow user to type on the canvas
textRec = Rect(150,height-100,40,40)
textPic = image.load("image/text.png")
running = True
 ###################################################################################################
 ###################################################################################################
screen.fill(black)
draw.rect(screen,(255,255,255),canvasRec)
while running:
	clicked = False
	screen.blit(canBuff1, (0,0))
	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
	ml=mx,my
	if mb[0]==1:
		screen.set_clip(None)
		#Logo
		if harryLoRec.collidepoint(mx,my):
			logo="harry"
			logocol=black
			sound = harrysong
			musicPlay()
			screen.set_clip(toolbar1)
			screen.fill(black)
			screen.set_clip(toolbar2)
			screen.fill(black)
			screen.set_clip(toolbar3)
			screen.fill(black)
		if wolverineLoRec.collidepoint(mx,my):
			logo="wolverine"
			logocol=wolve
			sound = xmen
			musicPlay()
			screen.set_clip(toolbar1)
			screen.fill(wolve)
			screen.set_clip(toolbar2)
			screen.fill(wolve)
			screen.set_clip(toolbar3)
			screen.fill(wolve)
		if santaLoRec.collidepoint(mx,my):
			logo="christmas"
			logocol=red
			sound = jingle
			musicPlay()
			screen.set_clip(toolbar1)
			screen.fill(red)
			screen.set_clip(toolbar2)
			screen.fill(red)
			screen.set_clip(toolbar3)
			screen.fill(red)
	#Theme
	if logo=="harry":
		screen.blit(harryPic,(0,50))
	if logo == "wolverine":
		screen.blit(wolverinePic,(0,50))
	if logo == "christmas":
		if tool != "stamp":
			portion.fill(red)
		screen.blit(hatPic,(0,50))
		
	# Logo
	screen.blit(harryLo,harryLoRec)
	screen.blit(wolverineLo,wolverineLoRec)
	screen.blit(santaLo,santaLoRec)
	# picture display
	
	screen.blit(pencilPic,pencilRec)
	screen.blit(sprayPic,sprayRec)
	screen.blit(eraserPic,eraserRec)
	screen.blit(colorPic,(1150,720))
	draw.rect(screen,black,colorRec,4)
	screen.blit(eyePic,eyeRec)
	screen.blit(fillPic,fillRec)
	screen.blit(brushPic,brushRec)
	screen.blit(savePic,saveRec)
	screen.blit(openPic,openRec)
	screen.blit(undoPic,undoRec)
	screen.blit(redoPic,redoRec)
	screen.blit(penPic,(500,height-85))
	if stop == 1:
		screen.blit(pausePic,musicRec)
	else:
		screen.blit(playPic,musicRec)

	if logo == "wolverine":
		screen.blit(clawPic,clawRec)
	if logo == "harry":
		screen.blit(textPic,textRec)
	draw.line(screen,blue,(255,height-45),(285,height-15),3)
	draw.circle(screen,blue,(320,height-25),10)
	draw.rect(screen,blue,[310,height-90,20,20])
	draw.circle(screen,blue,(370,height-25),10,2)
	draw.rect(screen,blue,[360,height-90,20,20],2)
	draw.polygon(screen,blue,[(420,height-95),(440,height-70),(400,height-70)],2)
	draw.polygon(screen,blue,[(420,height-45),(440,height-20),(400,height-20)])
	#new
	draw.rect(screen,white,newRec)
	#col
	draw.rect(screen,col,[200,0,40,40])
	draw.rect(screen,white,[200,0,40,40],1)
	draw.rect(screen,white,(1155,height-10,190,5))

	#Size
	draw.rect(screen,white,sizeRec)
	draw.circle(screen,logocol,(270,20),30)
	draw.circle(screen,white,(270,20),toolSize)
	draw.rect(screen,red,[1150+toolSize*10,705,20,40])

	for evnt in event.get():
		#print (evnt)# checks all events that happen
		if evnt.type == QUIT:
			running = False
		'''if evnt.type == KEYDOWN:
			if evnt.key == K_f:
				Fullscreen = not Fullscreen
				if Fullscreen:
					size = width, height = 1550, 800
					screen = display.set_mode(size, FULLSCREEN, 32)
				else:
					size = width, height = 1350, 800
					screen = display.set_mode(size, 0, 32)'''
		if evnt.type == MOUSEBUTTONDOWN:
			clicked=True
			#increase or decrease the tool size
			if tool != "stamp":
				if evnt.button==4:
					if toolSize<20:
						toolSize+=1
				
				elif evnt.button==5:
					if toolSize>1:
						toolSize-=1
			#increase or decrease the stamp size
			else:
				if evnt.button==4:
					stampS+=10
				
				elif evnt.button==5:
					stampS-=10
		if canvasRec.collidepoint(mx,my):
			if evnt.type == MOUSEBUTTONUP:
				undoP=undoPor.copy()
				undoL.append(undoP)
	

	# new paint
	#create a new canvas and set tool to pencil
	if tool =="new":
		screen.set_clip(canvasRec)
		if mb[0]==1:
			point = [(mx,80),(mx,my),(200,my),(200,80)]
			draw.polygon(screen,white,point)
		if mb[0]==0:
			draw.rect(screen,white,canvasRec)
			tool="pencil"

		
	# Stamp
	if tool == "stamp":
		if logo=="wolverine":
			draw.rect(screen,wolve,wolverinePicRec)
			screen.blit(wolverine1,wolverine1Rec)
			screen.blit(wolverine2,wolverine2Rec)
			screen.blit(magneto,magnetoRec)
			screen.blit(magnetoO,magnetoORec)
			screen.blit(charles1,charles1Rec)
			screen.blit(deadpool,deadpoolRec)
			if mb[0]==1:
				if wolverine1Rec.collidepoint(mx,my):
					chose="wolverine1"
				elif wolverine2Rec.collidepoint(mx,my):
					chose="wolverine2"
				elif magnetoRec.collidepoint(mx,my):
					chose="magneto"
				elif magnetoORec.collidepoint(mx,my):
					chose="magnetoO"
				elif charles1Rec.collidepoint(mx,my):
					chose="charles1"
				elif deadpoolRec.collidepoint(mx,my):
					chose="deadpool"
		if logo == "christmas":
			draw.rect(screen,red,wolverinePicRec)
			screen.blit(tree,treeRec)
			screen.blit(santa1Lo,santa1LoRec)
			screen.blit(bell,bellRec)
			screen.blit(snowman,snowmanRec)
			screen.blit(snowman1,snowman1Rec)
			screen.blit(santa2,santa2Rec)
			if mb[0]==1:
				if treeRec.collidepoint(mx,my):
					chose="tree"
				elif santa1LoRec.collidepoint(mx,my):
					chose="santa1Lo"
				elif bellRec.collidepoint(mx,my):
					chose="bell"
				elif snowmanRec.collidepoint(mx,my):
					chose="snowman"
				elif snowman1Rec.collidepoint(mx,my):
					chose="snowman1"
				elif santa2Rec.collidepoint(mx,my):
					chose="santa2"
				
	# draw tool
	if clicked:
		# to undo, redo and puase the music
		if musicRec.collidepoint(mx,my):
			musicpause()
		if undoRec.collidepoint(mx,my):
			undo()
		if redoRec.collidepoint(mx,my):
			redo()
	if canvasRec.collidepoint(mx,my):
		screen.set_clip(canvasRec)
		if tool == "dLine":
			dLine(mx,my)
		elif tool == "dCircle":
			dCircle(mx,my)
		elif tool == "dRect":
			dRect(mx,my)
		elif tool == "dCircleE":
			dCircleE(mx,my)
		elif tool == "dRectE":
			dRectE(mx,my)
		elif tool == "dTri":
			dTri(mx,my)
		elif tool == "dTriE":
			dTriE(mx,my)
		
		elif tool== "claw":
			claw(mx,my)


	#tool 300 0 40 40
	#to draw shapes on thee canvas
	draw.rect(screen,logocol,toolRec)
	if tool=="claw":
		screen.blit(clawPic,toolRec)
	elif tool == "dLine":
		draw.line(screen,blue,(300,0),(335,40),3)
	elif tool == "dCircle":
		draw.circle(screen,blue,(320,20),10)
	elif tool == "dRect":
		draw.rect(screen,blue,[305,10,20,20])
	elif tool == "dCircleE":
		draw.circle(screen,blue,(320,20),10,2)
	elif tool == "dRectE":
		draw.rect(screen,blue,[305,10,20,20],3)
	elif tool == "dTri":
		draw.polygon(screen,blue,[(320,5),(300,25),(340,25)])
	elif tool == "dTriE":
		draw.polygon(screen,blue,[(320,5),(300,25),(340,25)],2)
	elif tool == "fill":
		screen.blit(fillPic,toolRec)
	elif tool=="pencil":
		screen.blit(pencilPic,toolRec)
	elif tool=="spray":
		screen.blit(sprayPic,toolRec)
	elif tool=="eraser":
		screen.blit(eraserPic,toolRec)
	elif tool == "eye":
		screen.blit(eyePic,toolRec)
	elif tool=="stamp":
		if chose == "":
			continue
		else:
			choseLo= transform.scale(image.load("image/%s.png"%(chose+"s")), (40,40))
			screen.blit(choseLo,toolRec)
	elif tool=="brush":
		screen.blit(brushPic,toolRec)
	elif tool=="pen":
		screen.blit(penPic,(300,15))



	if mb[0]==1:
		screen.set_clip(None)

		#toolbar
		#to select tools
		if pencilRec.collidepoint(mx,my):#is the mouse point inside the pencilRec
			tool="pencil"
		elif sprayRec.collidepoint(mx,my):
			tool="spray"
		elif eraserRec.collidepoint(mx,my):
			tool="eraser"
		elif colorRec.collidepoint(mx,my):
			col=screen.get_at((mx,my))
		elif newRec.collidepoint(mx,my):
			tool="new"
		elif dLineRec.collidepoint(mx,my):
			tool="dLine"
		elif dCircleRec.collidepoint(mx,my):
			tool="dCircle"
		elif dRectRec.collidepoint(mx,my):
			tool="dRect"
		elif dCircleERec.collidepoint(mx,my):
			tool="dCircleE"
		elif dRectERec.collidepoint(mx,my):
			tool="dRectE"
		elif eyeRec.collidepoint(mx,my):
			tool="eye"
		elif dTriRec.collidepoint(mx,my):
			tool="dTri"
		elif dTriERec.collidepoint(mx,my):
			tool="dTriE"
		elif harryPicRec.collidepoint(mx,my):
			tool="stamp"
		elif fillRec.collidepoint(mx,my):
			tool="fill"
		elif brushRec.collidepoint(mx,my):
			tool="brush"
		elif penRec.collidepoint(mx,my):
			tool="pen"
		elif saveRec.collidepoint(mx,my):
			save()
		elif openRec.collidepoint(mx,my):
			openF()
		
		if logo == "wolverine":
			if clawRec.collidepoint(mx,my):
				tool="claw"
		if logo == "harry":
			if textRec.collidepoint(mx,my):
				tool="text"
		
			
		if sizeRec.collidepoint(mx,my):
			toolSize=(mx-1150)//10
			

		#canvas
		# to use the tool that is selected on the canvas
		if canvasRec.collidepoint(mx,my):
			screen.set_clip(canvasRec)

			if tool=="pencil":
				pencil(mx,my)
			elif tool=="spray":
				spray(mx,my)
			elif tool=="eraser":
				eraser(mx,my)
			elif tool == "eye":
				col=screen.get_at((mx,my))
			elif tool=="stamp":
				stamp(mx,my)
			elif tool=="claw":
				claw(mx,my)
			elif tool=="brush":
				brush(mx,my)
			elif tool=="pen":
				pen(mx,my)
			elif tool=="text":
				txt = getText(screen,mx,my) 
				txtPic = myfont.render(txt, True, (255,0,0))
				screen.blit(txtPic,(mx,my))
			elif tool=="fill":
				fill(mx,my)
				tool = "pencil"
			
			
	#x,y coordinate
	screen.set_clip(None)
	
	draw.rect(screen,logocol,[0,0,100,50])
	xCoor = myfont.render("x:%5s "%(mx-200), 10, (0,255,0))
	screen.blit(xCoor, (2, 0))
	yCoor= myfont.render("y:%5s "%(my-80), 10, (0,255,0))
	screen.blit(yCoor, (2, 25))
	ox=mx 
	oy=my 
	canBuff1 = screen.copy()
	mouse.set_visible(1)
	if canvasRec.collidepoint(mx,my):
		mouse.set_visible(0)
		current=screen.get_at((mx,my))
		opposite=(255-current[0],255-current[1],255-current[2])#use the opposite color
		draw.circle(screen, opposite, (mx,my),4,1)#to blit the mouse cursor
		
	display.flip()
quit()
