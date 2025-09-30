import pygame
import random

cell_size = 12
rows, cols = 100, 100

총인구 = 100
치료기간 = 100
발병빈도 = 4 # 1/발병빈도 확률로 감염
이동속도 = 1

class 사람:
    def __init__(self, row, col, 감염상태=False):
        self.row = row
        self.col = col
        self.감염상태 = 감염상태
        self.앓은시간 = 0
        self.last_dir = random.choice(['up', 'down', 'left', 'right'])

    def 돌아다니기(self):
        if random.random() > 이동속도:
            return
        dirs = ['up', 'down', 'left', 'right']
        if random.random() < 0.7:
            d = self.last_dir
        else:
            d = random.choice(dirs)
        self.last_dir = d
        if d == 'up': self.row = max(0, self.row-1)
        if d == 'down': self.row = min(rows-1, self.row+1)
        if d == 'left': self.col = max(0, self.col-1)
        if d == 'right': self.col = min(cols-1, self.col+1)

    def 회복(self):
        if self.감염상태:
            self.앓은시간 += 1
            if self.앓은시간 >= 치료기간:
                self.감염상태 = False
                self.앓은시간 = 0

    def 전염(self, 다른사람):
        if self.감염상태 and not 다른사람.감염상태:
            if (self.row - 다른사람.row)**2 <= 1 and (self.col - 다른사람.col)**2 <= 1:
                다른사람.감염상태 = True

def 세상그리기(screen, 모든사람):
    for r in range(rows):
        for c in range(cols):
            color = (255,255,255)
            rect = pygame.Rect(c*cell_size, r*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0,0,0), rect, 1)

    for 한사람 in 모든사람:
        r, c = 한사람.row, 한사람.col
        color = (255,0,0) if 한사람.감염상태 else (0,200,0)
        rect = pygame.Rect(c*cell_size, r*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((cols*cell_size, rows*cell_size))
    pygame.display.set_caption("Simple Infection Simulation")

    모든사람 = []
    for i in range(총인구):
        r = random.randint(0, rows-1)
        c = random.randint(0, cols-1)
        감염상태 = (i % 발병빈도 == 0)
        모든사람.append(사람(r, c, 감염상태))

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ####################################### 움직이는 세상
        # 돌아다니기 and 회복 모든사람
        for 각자 in 모든사람:
            각자.돌아다니기()
        # Infection spread
        for h1 in 모든사람:
            for h2 in 모든사람:
                h1.전염(h2)
                
        for h in 모든사람:
            h.회복()

        세상그리기(screen, 모든사람)
        ####################################### 움직이는 세상

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()