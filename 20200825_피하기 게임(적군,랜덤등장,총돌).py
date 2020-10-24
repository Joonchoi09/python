import pygame as p
import random as r

p.init() #라이브러리 초기화
white = (255,255,255) #빛의 3원색 RGB
size = (900,500) #(가로,세로)
sc = p.display.set_mode(size) #해상도크기설정
p.display.set_caption("게임판") #게임창제목
playing = True
#비행기 생성
b = p.image.load("b3.png")
p_rect = b.get_rect(left = 25, top = 150) #left = x , top = y
p_y = 0
#배경
bg = p.image.load("sky.png")
bg_x=0
bg_y=0
#복사본 배경
bg1 = bg.copy()
bg1_x=900
bg1_y=0
#적군
en = p.image.load("e.png")
e_rect = en.get_rect(left =850, top=175)
#적군2
en2 = p.image.load("l.png")
e2_rect = en2.get_rect(left =700, top=100)
#먹이
fd = p.image.load("d.png")
f_rect = fd.get_rect(left =850, top=175)

while playing: # while true - 계속 반복하기

      for event in p.event.get(): #사용자가뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #계속 반복하기를 종료
                  p.quit() #게임창 종료
                  quit() #shell 창 종료

            if event.type == p.KEYDOWN: #키보드를 눌렀을때
                  if event.key == p.K_UP: #방항키 위 눌렀을때
                        p_y = -5
                  if event.key == p.K_DOWN: #방항키 아래 눌렀을때
                        p_y = 5
            if event.type == p.KEYUP: #키보드를 눌렀을때
                  if event.key == p.K_UP: #방항키 위 눌렀을때
                        p_y = 0
                  if event.key == p.K_DOWN: #방항키 아래 눌렀을때
                        p_y = 0 
                 

      p_rect.top += p_y # p_rect.left = p_rect.left + p_y            

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
      
      sc.blit(b,p_rect)
      #위쪽아래쪽 막는 코드
      if p_rect.top <= 0: #위쪽벽 닿으면
          p_rect.top = 0
      if p_rect.top >= 435: #아래쪽벽 닿으면
          p_rect.top = 435

      sc.blit(en,e_rect)
      #적군 움직이기
      e_rect.left-= 10#e_rect.left = e_rect.left - 25
      if e_rect.left <= 0:#적이 왼쪽벽에 닿으면
            e_rect.left = 850
            e_rect.top = r.randint(0,350)
            
      sc.blit(en2,e2_rect)      
      #적군 움직이기2
      e2_rect.left-= 25#e_rect.left = e_rect.left - 25
      if e2_rect.left <= 0:#적이 왼쪽벽에 닿으면
            e2_rect.left = 850
            e2_rect.top = r.randint(0,350)
            
      sc.blit(fd,f_rect)
      #먹이 움직이기
      f_rect.left-= 5#e_rect.left = e_rect.left - 25
      if f_rect.left <= 0:#적이 왼쪽벽에 닿으면
            f_rect.left = 850
            f_rect.top = r.randint(0,450)
      
      if p_rect.colliderect(e_rect):
            playing = False
            
      
      
            
      p.display.flip() #화면 업데이트




















      
