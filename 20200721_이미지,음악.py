import pygame as p

p.init() #라이브리리 초기화
size = (800,400) # (가로,세로)
w = (255,255,255) #빛의 3원색RGB
sc = p.display.set_mode(size) #해상도 설정
p.display.set_caption("이미지 삽입")

a = p.image.load("a.png")
b = p.image.load("b.png")

playing = True



while playing: #while tuue - 계속반복하기

      for event in p.event.get(): #사용자가 뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False

      sc.fill(w)

      sc.blit(a,(350,130)) #이미지변수,(x좌표,y좌표)
      sc.blit(b,(450,130))
      
      p.display.flip() #화면 업데이트
      
