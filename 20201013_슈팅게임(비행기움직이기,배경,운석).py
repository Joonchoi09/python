import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #빛의 3원색 RGB
size = (500,800) #(가로,세로)
sc = p.display.set_mode(size) #해상도크기설정
p.display.set_caption("게임판") #게임창제목
playing = True
#비행기이미지 변수에 넣기 
plane = p.image.load("os.png")
p_rect = plane.get_rect(left = 195,top =700)
p_x = 0
#배경 변수넣기
bg = p.image.load("sp.jpg")
#미사일 변수 넣기
bullet = p.image.load("og.png")
b_list = []


while playing: # while true - 계속 반복하기

      for event in p.event.get(): #사용자가뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #계속 반복하기를 종료
                  p.quit() #게임창 종료
                  quit() #shell 창 종료
            if event.type == p.KEYDOWN:
                  if event.key == p.K_LEFT:
                        p_x = -8
                  if event.key == p.K_RIGHT:
                        p_x = +8
                  if event.key == p.K_SPACE:
                        b_rect = bullet.get_rect(left = p_rect.left+37,top = p_rect.top)
                        b_list.append(b_rect)
                        
            if event.type == p.KEYUP:
                  if event.key == p.K_LEFT:
                        p_x = -2
                  if event.key == p.K_RIGHT:
                        p_x = +2

      p_rect.left += p_x
      sc.fill(white) #배경화면색 설정
      #배경업로드
      sc.blit(bg,(0,0))
      #비행기 화면 업로드
      sc.blit(plane,p_rect)
      if p_rect.left <= -100:
            p_rect.left = 500
      if p_rect.left >= 501:
            p_rect.left = -100

      #미사일 화면 업로드
      for b_rect in b_list:
            sc.blit(bullet,b_rect)#미사일 화면 업로드
            b_rect.top -= 20
            if b_rect.top <=0:   #총알이 위쪽벽에 닿으면
                  b_list.remove(b_rect)

      
      p.display.flip() #화면 업데이트
