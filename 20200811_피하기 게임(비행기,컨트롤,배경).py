import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #빛의 3원색 RGB
size = (900,500) #(가로,세로)
sc = p.display.set_mode(size) #해상도크기설정
p.display.set_caption("게임판") #게임창제목
playing = True
#비행기 생성
b = p.image.load("b3.png")
#배경
bg = p.image.load("sky2.png")
bg_x=0
bg_y=0
bg1 = bg.copy()
bg1_x=900
bg1_y=0

while playing: # while true - 계속 반복하기

      for event in p.event.get(): #사용자가뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #계속 반복하기를 종료
                  p.quit() #게임창 종료
                  quit() #shell 창 종료

      sc.fill(white) #배경화면색 설정
      sc.blit(bg,(bg_x,bg_y))
      sc.blit(bg1,(bg1_x,bg1_y))
      bg_x -= 2 #bg_x = bg_x - 1
      bg1_x -= 2
      #배경 왼쪽벽에 닿게 되면
      if bg_x <= -900:
            bg_x = 900
      if bg1_x <= -900:
            bg1_x = 900
      
      sc.blit(b,(25,150))
      
      p.display.flip() #화면 업데이트
