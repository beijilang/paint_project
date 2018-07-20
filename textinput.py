from pygame import *

def getText(screen,xx,yy):
    ans = ""        # final text will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 25)
    back = screen.copy()  
    length = 0

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                        if len(ans)*10>=length:
                            length-=14
                        else:
                            continue
                        
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    if len(ans)*10>=length:
                        length+=14

        textArea = Rect(xx,yy,20+length,30)    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        
        myclock.tick(100)
        display.flip()
    screen.blit(back,(0,0))
   
    return ans
       
