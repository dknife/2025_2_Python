import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Etch-a-Sketch - 완전 완벽 최종판")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_RED = (139, 0, 0)
GOLD = (255, 215, 0)
BORDER_COLOR = (160, 82, 45)

clock = pygame.time.Clock()

# 그리기 영역
DRAW_LEFT, DRAW_TOP = 100, 100
DRAW_WIDTH, DRAW_HEIGHT = 700, 500
draw_surf = pygame.Surface((DRAW_WIDTH, DRAW_HEIGHT))
draw_surf.fill(GRAY)

# 시작점 보이게!!
pen_x = DRAW_WIDTH // 2
pen_y = DRAW_HEIGHT // 2
pygame.draw.circle(draw_surf, WHITE, (pen_x, pen_y), 3)

# 노브
knob1_center = (120, 550)
knob2_center = (780, 550)
knob_radius = 60
knob_inner_radius = 45

total_angle1 = total_angle2 = 0.0
start_angle1 = start_angle2 = 0.0
dragging_knob = 0  # 0없음, 1왼쪽, 2오른쪽, 3오른클릭, 4휠클릭

def calculate_angle(center, pos):
    dx = pos[0] - center[0]
    dy = pos[1] - center[1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle + 360 if angle < 0 else angle

def draw_knob(surf, center, angle, active=False):
    color = GOLD if active else DARK_RED
    pygame.draw.circle(surf, LIGHT_GRAY, center, knob_radius)
    pygame.draw.circle(surf, WHITE, center, knob_radius, 8)
    pygame.draw.circle(surf, color, center, knob_inner_radius)
    rad = math.radians(angle)
    ex = center[0] + knob_inner_radius * math.cos(rad)
    ey = center[1] + knob_inner_radius * math.sin(rad)
    pygame.draw.line(surf, WHITE, center, (int(ex), int(ey)), 8)
    pygame.draw.circle(surf, WHITE, center, 6)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    left, middle, right = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            draw_surf.fill(GRAY)
            pen_x, pen_y = DRAW_WIDTH // 2, DRAW_HEIGHT // 2
            pygame.draw.circle(draw_surf, WHITE, (pen_x, pen_y), 3)
            total_angle1 = total_angle2 = 0.0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            d1 = math.hypot(mouse_pos[0] - knob1_center[0], mouse_pos[1] - knob1_center[1])
            d2 = math.hypot(mouse_pos[0] - knob2_center[0], mouse_pos[1] - knob2_center[1])

            if left:  # 왼클릭
                if d1 <= knob_radius:
                    dragging_knob = 1
                    start_angle1 = calculate_angle(knob1_center, mouse_pos)
                elif d2 <= knob_radius:
                    dragging_knob = 2
                    start_angle2 = calculate_angle(knob2_center, mouse_pos)

            elif right:  # 오른클릭 → 대각선
                if d1 <= knob_radius or d2 <= knob_radius:
                    dragging_knob = 3
                    start_angle1 = calculate_angle(knob1_center, mouse_pos)
                    start_angle2 = calculate_angle(knob2_center, mouse_pos)

            elif middle:  # 휠클릭 → 반대 대각선
                if d1 <= knob_radius or d2 <= knob_radius:
                    dragging_knob = 4
                    start_angle1 = calculate_angle(knob1_center, mouse_pos)
                    start_angle2 = calculate_angle(knob2_center, mouse_pos)

        # 핵심 수정: 어떤 버튼이든 떼면 무조건 해제!!!
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_knob = 0

    # 드래그 처리 (이제 진짜 완벽)
    if dragging_knob:
        if dragging_knob == 1:
            a = calculate_angle(knob1_center, mouse_pos)
            da = a - start_angle1
            if da > 180: da -= 360
            if da < -180: da += 360
            pen_x += int(da * 1.5)
            total_angle1 += da
            start_angle1 = a

        elif dragging_knob == 2:
            a = calculate_angle(knob2_center, mouse_pos)
            da = a - start_angle2
            if da > 180: da -= 360
            if da < -180: da += 360
            pen_y += int(da * 1.5)
            total_angle2 += da
            start_angle2 = a

        elif dragging_knob == 3:  # 오른클릭 대각선
            a1 = calculate_angle(knob1_center, mouse_pos)
            a2 = calculate_angle(knob2_center, mouse_pos)
            da = (a1 - start_angle1 + a2 - start_angle2) / 2
            if abs(da) > 180: da += -360 if da > 0 else 360
            pen_x += int(da * 1.5)
            pen_y += int(da * 1.5)
            total_angle1 += da
            total_angle2 += da
            start_angle1, start_angle2 = a1, a2

        elif dragging_knob == 4:  # 휠클릭 반대 대각선
            a1 = calculate_angle(knob1_center, mouse_pos)
            da = a1 - start_angle1
            if da > 180: da -= 360
            if da < -180: da += 360
            pen_x += int(da * 1.5)
            pen_y -= int(da * 1.5)
            total_angle1 += da
            total_angle2 -= da
            start_angle1 = a1

        pen_x = max(0, min(DRAW_WIDTH - 1, pen_x))
        pen_y = max(0, min(DRAW_HEIGHT - 1, pen_y))
        pygame.draw.circle(draw_surf, WHITE, (int(pen_x), int(pen_y)), 3)

    # 화면 출력
    screen.fill(BLACK)
    pygame.draw.rect(screen, BORDER_COLOR, (80, 80, 740, 540), 25, border_radius=20)
    screen.blit(draw_surf, (DRAW_LEFT, DRAW_TOP))
    draw_knob(screen, knob1_center, total_angle1, dragging_knob in (1,3,4))
    draw_knob(screen, knob2_center, total_angle2, dragging_knob in (2,3,4))

    font = pygame.font.SysFont("malgungothic", 30, bold=True) or pygame.font.SysFont(None, 30)
    screen.blit(font.render("완성! 시작점 있음 / 모든 버튼 반응함", True, WHITE), (150, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()