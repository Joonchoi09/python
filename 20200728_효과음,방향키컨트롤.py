import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #빛의 3원색 RGB
size = (600,800) #(가로,세로)
sc = p.display.set_mode(size) #해상도크기설정
p.display.set_caption("게임판") #게임창제목
playing = True

#이미지 추가
g = p.image.load("g.png")
c = p.image.load("c.png")
#음악 추가
p.mixer.music.load("cat.mp3") #음악 불러오는 역활
p.mixer.music.play() # (0) -무한재생,(-1) - 한번만재생


while playing: # while true - 계속 반복하기

      for event in p.event.get(): #사용자가뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #계속 반복하기를 종료
                  p.quit() #게임창 종료
                  quit() #shell 창 종료

      sc.fill(white) #배경화면색 설정
      
      sc.blit(g,(250,350))
      sc.blit(c,(10,700))
      
      p.display.flip() #화면 업데이트
