import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
width,height=420, 420
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Environment Maze")
osurf1=pygame.image.load("flower.png")
osurf=pygame.transform.scale(osurf1,(20,20))
msurf1=pygame.image.load("Orange_Block.png")
msurf=pygame.transform.scale(msurf1,(20,20))
endp=pygame.image.load("end1.png")
end=pygame.transform.scale(endp,(20,20))
scoreg=0
obstacles=[(4,2),(5,15),(6,15),(7,8),(7,15),(8,8),(8,15),(9,5),(9,8),(9,9),(10,5),(10,9),(10,12),(11,5),(11,9),(11,10),(12,5),(12,10),(12,15),(13,5),(13,10),(14,10),(14,11),(15,11),(15,18),(16,3),(16,11),(16,18),(17,7),(18,7),(20,5),(20,9)]

maze=[[0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1],
[0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1],
[1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0],
[1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0],
[0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1],
[1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,2,0,0,0],
[0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0],
[1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0],
[0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0],
[1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0],
[0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1],
[1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0],
[1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0],
[0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0],
[1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1],
[0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1],
[0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0],
[0,0,1,0,1,0,1,0,1,1,0,1,3,0,0,1,1,0,1,0,0],
[1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0],
[8,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1]]
count=0
scrsub=0

def openmaze(tx,ty):
    global scoreg
    global count
    import pygame
    pygame.font.init()
    width,height=420, 420
    big_font=pygame.font.SysFont("microsofthimalaya",50,bold=True)
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Environment Maze")
    osurf1=pygame.image.load("flower.png")
    osurf=pygame.transform.scale(osurf1,(20,20))
    msurf1=pygame.image.load("Orange_Block.png")
    msurf=pygame.transform.scale(msurf1,(20,20))
    endp=pygame.image.load("end1.png")
    end=pygame.transform.scale(endp,(20,20))

    maze=[[0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1],
    [0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0],
    [1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0],
    [0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,2,0,0,0],
    [0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0],
    [1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0],
    [1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0],
    [0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1],
    [1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0],
    [0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0],
    [1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0],
    [0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0],
    [1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1],
    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1],
    [0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0],
    [0,0,1,0,1,0,1,0,1,1,0,1,3,0,0,1,1,0,1,0,0],
    [1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0],
    [8,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1]]
    px=tx*20
    py=ty*20
    move=0
    right=True
    left=True
    delay=500
    bg=pygame.Surface((420,420))
    bg.fill((0,0,0))
    placex=0
    placey=0
    for row in maze:
        placex=0
        for wall in row:
            if wall==1:
                bg.blit(msurf,(placex*20, placey*20))
            elif wall==8:
                bg.blit(end,(placex*20, placey*20))
            placex+=1 
        placey+=1
        
    while True:
        pygame.event.get()
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        screen.blit(osurf,(px,py))
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            if left:
               if move== 0:
                   move= delay
                   px -= 20
                   scoreg+=100
                   if px < 0:
                       px = 0
        if keys[K_RIGHT]:
            if right:
               if move== 0:   
                   move= delay
                   px += 20
                   scoreg+=100
                   if px > 400:
                       px = 400
        if keys[K_DOWN]:
            if down:
                if move== 0:   
                    move= delay   
                    py += 20
                    scoreg+=100
                    if py >= 400:
                        py = 400
        if keys[K_UP]:
            if up:
                if move== 0:   
                    move= delay 
                    py -= 20
                    scoreg+=100
                    if py < 0:
                        py = 0
        if move > 0:
           move -= 1
        truex = int(px / 20)
        truey = int(py / 20)
        if (truey,truex) in obstacles:
            count+=1

        if truex==0 and truey==20:
            scrsub=count//200
            scoreg-=scrsub*30
            screen.fill((255,165,0))
            message="YOUR SCORE IS:"
            text_surface=big_font.render(message,True,(0,0,0))
            score_surface=big_font.render(str(scoreg),True,(0,0,0))
            screen.blit(text_surface,(30,50))
            screen.blit(score_surface,(100,150))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
        num1=maze[truey][truex]

        
        if num1==3:#sliding puzz cond
            import pygame
            import random
            import math
            pygame.font.init()
            pygame.init()
            win=pygame.display.set_mode((900,454))
            pygame.display.set_caption("SLIDING PUZZLE")
            timer=0
            score=0
            teem=pygame.Surface((150,40))
            teem.fill((14,240,240))
            BLANK = "Empty"
            P=["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png"]
            L=["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png"]
            random.shuffle(L)
            M=L+["Empty"]
            print(M)
            big_font=pygame.font.SysFont("microsofthimalaya",80,bold=True)
            base_font=pygame.font.Font(None,32)
            mess_font=pygame.font.Font(None,25)
            win.fill((0,0,0))
            line1="Welcome to Marine Puzzle Game!"
            line2="Just click on image to slide into blank space"
            line3="(like a sliding puzzle)"
            line4="You have 5:00 minutes to arrange given"
            line5="puzzle pieces into image below-"
            text1=mess_font.render(line1,True,(255,255,255))
            text2=mess_font.render(line2,True,(255,255,255))
            text3=mess_font.render(line3,True,(255,255,255))
            text4=mess_font.render(line4,True,(255,255,255))
            text5=mess_font.render(line5,True,(255,255,255))
            win.blit(text1,(500,50))
            win.blit(text2,(500,70))
            win.blit(text3,(500,90))
            win.blit(text4,(500,110))
            win.blit(text5,(500,130))
            pygame.draw.line(win, (128,128,128), (458, 0), (458,454),8)
            pic=pygame.image.load("fullimg.png")
            pic1=pygame.transform.scale(pic,(250,250))
            win.blit(pic1,(515,160))
            pygame.display.update()


            mc=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
            def blankpos(M):
                for i in range(9):
                    if M[i]=="Empty":
                        a=mc[i]
                return a
            def printpuzzle(M):
                b=0
                p=0
                for i in range(3):
                    a=0
                    for j in range(3):
                        if M[p] != "Empty":
                            user=pygame.image.load(M[p])
                            user1=pygame.transform.scale(user,(150,150))
                            win.blit(user1,(a,b))
                            a+=152
                            p+=1
                        else:
                            pygame.draw.rect(win,(0,0,0),(a,b,150,150))
                            a+=152
                            p+=1
                    b+=152
            def check(x,y):
                bl=blankpos(M)
                m=bl[0]
                n=bl[1]
                if (x,y) in mc:
                    if n!=0:
                        if (x,y)==(m,n-1):
                            for i in range(9):
                                if mc[i]==(x,y):
                                    k=i
                            for i in range(9):
                                if mc[i]==(m,n):
                                    l=i
                            for i in range(9):
                                M[k],M[l]=M[l],M[k]
                    if n!=2:
                        if (x,y)==(m,n+1):
                            for i in range(9):
                                if mc[i]==(x,y):
                                    k=i
                            for i in range(9):
                                if mc[i]==(m,n):
                                    l=i
                            for i in range(9):
                                M[k],M[l]=M[l],M[k]
                            
                    if m!=0:
                        if (x,y)==(m-1,n):
                            for i in range(9):
                                if mc[i]==(x,y):
                                    k=i
                            for i in range(9):
                                if mc[i]==(m,n):
                                    l=i
                            for i in range(9):
                                M[k],M[l]=M[l],M[k]
                    if m!=2:
                        if (x,y)==(m+1,n):
                            for i in range(9):
                                if mc[i]==(x,y):
                                    k=i
                            for i in range(9):
                                if mc[i]==(m,n):
                                    l=i
                            for i in range(9):
                                M[k],M[l]=M[l],M[k]
                
                printpuzzle(M)
                pygame.display.update()
            def checkcomp():
                c=0
                a=False
                for i in range(8):
                    if M[i]==P[i]:
                        c+=1
                if c==8:
                    a=True
                return a
            def timescore():
                c=0
                sc=0
                for i in range(8):
                    if M[i]==P[i]:
                        c+=1
                sc=100*c
                return sc
            printpuzzle(M)
            pygame.display.update()
            clock = pygame.time.Clock()
            run=True
            while run:
                pygame.time.delay(100)
                sec=clock.tick()/1000.0
                timer+=sec
                displaytimer=math.trunc(timer)
                s=displaytimer%60
                sd2=s%10
                sd1=s//10
                m=displaytimer//60
                timertext=base_font.render('Timer: '+str(m)+':'+str(sd1)+str(sd2),True,(245,93,5))
                teem.fill((14,240,240))
                teem.blit(timertext,(7,5))
                win.blit(teem,(500,0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                    if event.type ==pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed():
                            pos=pygame.mouse.get_pos()
                            x=pos[0]//150
                            y=pos[1]//150
                            check(x,y)
                            cond=checkcomp()
                            if cond==True:
                                ft=displaytimer
                                if ft>0 and ft<=60:
                                    score=1000
                                if ft>60 and ft<=120:
                                    score=950
                                if ft>120 and ft<=180:
                                    score=900
                                if ft>180 and ft<=240:
                                    score=850
                                if ft>240 and ft<=300:
                                    score=800
                                scoreg+=score
                                win.fill((14,240,240))
                                message="YOUR SCORE IS:"
                                text_surface=big_font.render(message,True,(0,0,0))
                                score_surface=big_font.render(str(score),True,(0,0,0))
                                win.blit(text_surface,(200,30))
                                win.blit(score_surface,(400,190))
                                pygame.display.update()
                                pygame.time.delay(3000)
                                openmaze(truex,truey+1)
                if displaytimer==300:######
                    tscore=timescore()
                    scoreg+=tscore
                    win.fill((14,240,240))
                    timeup="TIMES UP!!!"
                    message="YOUR SCORE IS:"
                    mess_surface=big_font.render(timeup,True,(0,0,0))
                    text_surface=big_font.render(message,True,(0,0,0))
                    score_surface=big_font.render(str(tscore),True,(0,0,0))
                    win.blit(mess_surface,(250,30))
                    win.blit(text_surface,(200,115))
                    win.blit(score_surface,(400,275))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    openmaze(truex,truey+1)
        
        right = True
        left = True
        up = True
        down = True
        try:
            if truey !=20:
                if maze[truey-1][truex]==1:
                    up = False
                if maze[truey+1][truex]==1:
                    down = False
                if maze[truey][truex-1]==1:
                    left = False
                if maze[truey][truex+1]==1:
                    right = False
            elif truey==20:
                if maze[truey-1][truex]==1:
                    up = False
                if maze[truey][truex]==1:
                    down = False
                if maze[truey][truex-1]==1:
                    left = False
                if maze[truey][truex+1]==1:
                    right = False
                
               
        except IndexError:
            pass
            
        pygame.display.flip()
        
    
px=0
py=0
move=0
right=True
left=True
delay=500
bg=pygame.Surface((420,420))
bg.fill((0,0,0))
placex=0
placey=0
for row in maze:
    placex=0
    for wall in row:
        if wall==1:
            bg.blit(msurf,(placex*20, placey*20))
        elif wall==8:
                bg.blit(end,(placex*20, placey*20))
        placex+=1
    placey+=1
while True:
    pygame.event.get()
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(osurf,(px,py))
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        if left:
           if move== 0:
               move= delay
               px -= 20
               scoreg+=100
               if px < 0:
                   px = 0
    if keys[K_RIGHT]:
        if right:
           if move== 0:   
               move= delay
               px += 20
               scoreg+=100
               if px > 400:
                   px = 400
    if keys[K_DOWN]:
        if down:
            if move== 0:   
                move= delay   
                py += 20
                scoreg+=100
                if py >= 400:
                    py = 400
    if keys[K_UP]:
        if up:
            if move== 0:   
                move= delay 
                py -= 20
                scoreg+=100
                if py < 0:
                    py = 0
    if move > 0:
       move -= 1
    truex = int(px / 20)
    truey = int(py / 20)
    num=maze[truey][truex]
    
    if num==2:#quiz condition
        import pygame,sys
        import math
        from pygame.locals import *
        pygame.init()
        pygame.font.init()
        screen=pygame.display.set_mode((800,600))
        pygame.display.set_caption("Eco Pop-Quiz")
        teem=pygame.Surface((110,110))
        teem.fill((166, 245, 20))
        base_font=pygame.font.SysFont("arial",25,bold=True)
        message_font=pygame.font.SysFont("microsofthimalaya",80,bold=True)
        user_text=''
        a=0
        score=0
        timer=0
        LT=[]
        L=["Q1.png","Q2.png","Q3.png","Q4.png","Q5.png","Q6.png","Q7.png","Q8.png","Q9.png","Q10.png"]
        LA=['C','B','C','C','A','B','D','C','C','B']
        screen.fill((0,0,0))
        user=pygame.image.load('Instructions.png')
        user1=pygame.transform.scale(user,(600,400))
        screen.blit(user1,(0,0))
        text_surface=base_font.render(user_text,True,(255,255,255))
        screen.blit(text_surface,(3,504))
        pygame.draw.rect(screen,(255,255,255),(0,402,140,32),2)
        timertext=base_font.render('Timer: '+str(timer),True,(0,0,0))
        teem.blit(timertext,(8,45))
        screen.blit(teem,(650,50))
        pygame.display.flip()
        def printq(a):
            if a<=9:
                screen.fill((0,0,0))
                user=pygame.image.load(L[a])
                user1=pygame.transform.scale(user,(600,400))
                screen.blit(user1,(0,0))
                pygame.display.flip()
        def enta():
                text_surface=base_font.render(user_text,True,(255,255,255))
                pygame.draw.rect(screen,(255,255,255),(0,402,140,32),2)
                screen.blit(text_surface,(5,404))
                pygame.display.flip()
        def timescore():
            sco=0
            La=LT[1:]
            l=len(La)
            ccw=0
            for i in range(l):
                if La[i]==LA[i]:
                    ccw+=1
            sco=ccw*100
            return sco
        clock=pygame.time.Clock()
        run=True
        while run:
            pygame.time.delay(100)
            sec=clock.tick()/1000.0
            timer+=sec
            displaytimer=math.trunc(timer)
            timertext=base_font.render('Timer: '+str(displaytimer),True,(0,0,0))
            teem.fill((166, 245, 20))
            teem.blit(timertext,(8,45))
            screen.blit(teem,(650,50))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        LT.append(user_text.upper())
                        user_text=''
                        pos=pygame.mouse.get_pos()
                        x=0
                        y=0
                        for i in range(600):
                            if pos[0]==i:
                                x+=1
                        for j in range(400):
                            if pos[1]==j:
                                y+=1
                        if x==1 and y==1:
                            if a<=9:
                                printq(a)
                                a+=1
                            else:
                                LT=LT[1:]
##                                print(LT)
##                                print(LA)
                                ca=0
                                wa=0
                                for i in range(10):
                                    if LA[i]==LT[i]:
                                        ca+=1
                                    else:
                                        wa+=1
                                score=ca*100
                                scoreg+=score
                                screen.fill((166, 245, 20))
                                message="YOUR SCORE IS:"
                                text_surface=message_font.render(message,True,(0,0,0))
                                score_surface=message_font.render(str(score),True,(0,0,0))
                                screen.blit(text_surface,(150,100))
                                screen.blit(score_surface,(375,300))
                                pygame.display.flip()
                                pygame.time.delay(3000)
                                openmaze(truex,truey)
                            
                                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        user_text=user_text[:-1]
                    else:
                        user_text+=event.unicode
            enta()
            if displaytimer==100:
                tscore=timescore()
                scoreg+=tscore
                screen.fill((166, 245, 20))
                timeup="TIMES UP!!!"
                message="YOUR SCORE IS:"
                mess_surface=message_font.render(timeup,True,(0,0,0))
                text_surface=message_font.render(message,True,(0,0,0))
                score_surface=message_font.render(str(tscore),True,(0,0,0))
                screen.blit(mess_surface,(210,50))
                screen.blit(text_surface,(150,115))
                screen.blit(score_surface,(375,350))
                pygame.display.flip()
                pygame.time.delay(3000)
                openmaze(truex,truey)
    else:
        pass
    right = True
    left = True
    up = True
    down = True
    try:
        if truey !=20:
            if maze[truey-1][truex]==1:
                up = False
            if maze[truey+1][truex]==1:
                down = False
            if maze[truey][truex-1]==1:
                left = False
            if maze[truey][truex+1]==1:
                right = False
        elif truey==20:
            if maze[truey-1][truex]==1:
                up = False
            if maze[truey][truex]==1:
                down = False
            if maze[truey][truex-1]==1:
                left = False
            if maze[truey][truex+1]==1:
                right = False
    except IndexError:
        pass
    pygame.display.flip()
