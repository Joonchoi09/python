import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #빛의 3원색 RGB
size = (600,800) #(가로,세로)
sc = p.display.set_mode(size) #해상도크기설정
p.display.set_caption("키보드 주작") #게임창제목
playing = True

b = p.image.load("b.png")
x = 100
y = 100

while playing: # while true - 계속 반복하기

      for event in p.event.get(): #사용자가뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #계속 반복하기를 종료
                  p.quit() #게임창 종료
                  quit() #shell 창 종료
            if event.type == p.KEYDOWN: #만일 키보드를 눌렀을때
                  if event.key == p.K_UP: #위 방향키를 눌렀을때
                        y -= 30
                  if event.key == p.K_DOWN: #아래 방향키를 눌렀을때
                        y += 30
                  if event.key == p.K_LEFT: #왼쪽 방향키를 눌렀을때
                        x -= 30
                  if event.key == p.K_RIGHT: #오른쪽 방향키를 눌렀을때
                        x += 30

            if event.type == p.KEYUP: #만일 키보드를 때렀을때
                  if event.key == p.K_UP: #위 방향키를 때렀을때
                        y -= 0
                  if event.key == p.K_DOWN: #아래 방향키를 때렀을때
                        y += 0
                  if event.key == p.K_LEFT: #왼쪽 방향키를 때렀을때
                        x -= 0
                  if event.key == p.K_RIGHT: #오른쪽 방향키를 때렀을때
                        x += 0

      sc.fill(white) #배경화면색 설정
      sc.blit(b,(x,y))
      
      p.display.flip() #화면 업데이트
