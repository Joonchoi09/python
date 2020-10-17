import pygame as pg

pg.init()  #라이브러리 초기화

size = [1000,600] #[가로,세로]
screen = pg.display.set_mode(size) #해상도 설정

pg.display.set_caption("파이게임 기초") #게임창제목
#색깔 (빛의 3원색 RGB)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
green = (200,255,51)
playing = True

while playing: #while True - 게속 반복하기

      for event in pg.event.get(): # 사용자가 뭘 눌렀는지 감지
            if  event.type == pg.QUIT: #만일 창x 버튼 누른다면 (== 서로같다)
                playing = False
                pg.quit() #게임판이 없어서
                quit() 



      screen.fill(green) # 배경색

      pg.draw.rect(screen,black,[450,250,100,100],10)
                              #[x좌표,y좌표,가로크기,세로크기],선굵기
      
      pg.draw.rect(screen,white,[475,275,50,50],)
                              #[x좌표,y좌표,가로크기,세로크기],선굵기
      
      pg.draw.circle(screen,red,[900,70],60)
                              #[x좌표,y좌표,],반지름,선굵기
      
      pg.draw.polygon(screen,black,[[500,150],[550,250],[450,250]],10)
                                    #[[꼭짓점1],[꼭짓점2],[꼭짓점3]],선굵기)
                      
      pg.display.flip() #회면 업데이트
      

      
      
