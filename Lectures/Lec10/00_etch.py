import pygame
import math
import sys

# pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Etch-a-Sketch Knob - 이제 확실히 동작!")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_RED = (139, 0, 0)
BORDER_COLOR = (160, 82, 45)

# 클락
clock = pygame.time.Clock()

# 그리기 영역 (중앙)
DRAW_LEFT, DRAW_TOP = 100, 100
DRAW_WIDTH, DRAW_HEIGHT = 700, 500
draw_surf = pygame.Surface((DRAW_WIDTH, DRAW_HEIGHT))
draw_surf.fill(GRAY)  # 배경 회색

# 펜 초기 위치 (중앙)
pen_x = DRAW_WIDTH // 2
pen_y = DRAW_HEIGHT // 2

# Knob 위치와 크기
knob1_center = (120, 550)  # 왼쪽 (X 제어)
knob2_center = (780, 550)  # 오른쪽 (Y 제어)
knob_radius = 60
knob_inner_radius = 45

# 각도 변수 (누적 각도)
total_angle1 = 0.0  # 왼쪽 knob 누적
total_angle2 = 0.0  # 오른쪽 knob 누적
start_angle1 = 0.0
start_angle2 = 0.0
dragging_knob = 0  # 0: 없음, 1: 왼쪽, 2: 오른쪽

def calculate_angle(center, mouse_pos):
    """마우스 위치로부터 knob 각도 계산 (도 단위)"""
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    angle = math.degrees(math.atan2(dy, dx))
    if angle < 0:
        angle += 360
    return angle

def draw_knob(surface, center, total_angle):
    """knob 그리기 (손잡이 각도 반영)"""
    # 외곽 원
    pygame.draw.circle(surface, LIGHT_GRAY, center, knob_radius)
    pygame.draw.circle(surface, WHITE, center, knob_radius, 8)
    
    # 내부 원
    pygame.draw.circle(surface, DARK_RED, center, knob_inner_radius)
    
    # 손잡이 선 (12시 기준으로 total_angle만큼 회전)
    handle_angle = math.radians(total_angle)
    end_x = center[0] + knob_inner_radius * math.cos(handle_angle)
    end_y = center[1] + knob_inner_radius * math.sin(handle_angle)
    pygame.draw.line(surface, WHITE, center, (int(end_x), int(end_y)), 8)
    
    # 중앙
    pygame.draw.circle(surface, WHITE, center, 6)

# 메인 루프
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_surf.fill(GRAY)
                pen_x = DRAW_WIDTH // 2
                pen_y = DRAW_HEIGHT // 2
                total_angle1 = total_angle2 = 0.0
        
        # 마우스 클릭으로 knob 잡기
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dist1 = math.hypot(mouse_pos[0] - knob1_center[0], mouse_pos[1] - knob1_center[1])
            dist2 = math.hypot(mouse_pos[0] - knob2_center[0], mouse_pos[1] - knob2_center[1])
            if dist1 <= knob_radius:
                dragging_knob = 1
                start_angle1 = calculate_angle(knob1_center, mouse_pos)
            elif dist2 <= knob_radius:
                dragging_knob = 2
                start_angle2 = calculate_angle(knob2_center, mouse_pos)
        
        # 마우스 뗌
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_knob = 0
    
    # 드래그 중일 때 (MOUSEMOTION 이벤트 없이도 mouse_pos로 처리)
    if dragging_knob == 1:
        current_angle = calculate_angle(knob1_center, mouse_pos)
        delta_angle = current_angle - start_angle1
        # 각도 보정 (360도 넘지 않게)
        if delta_angle > 180:
            delta_angle -= 360
        elif delta_angle < -180:
            delta_angle += 360
        
        # 펜 X 움직임 (delta * 민감도)
        pen_x += int(delta_angle * 1.5)
        pen_x = max(0, min(DRAW_WIDTH - 1, pen_x))
        
        # knob 손잡이 업데이트
        total_angle1 += delta_angle
        start_angle1 = current_angle
        
        # 선 그리기
        pygame.draw.circle(draw_surf, WHITE, (pen_x, pen_y), 3)
    
    elif dragging_knob == 2:
        current_angle = calculate_angle(knob2_center, mouse_pos)
        delta_angle = current_angle - start_angle2
        if delta_angle > 180:
            delta_angle -= 360
        elif delta_angle < -180:
            delta_angle += 360
        
        # 펜 Y 움직임
        pen_y += int(delta_angle * 1.5)
        pen_y = max(0, min(DRAW_HEIGHT - 1, pen_y))
        
        total_angle2 += delta_angle
        start_angle2 = current_angle
        
        # 선 그리기
        pygame.draw.circle(draw_surf, WHITE, (pen_x, pen_y), 3)

    # 화면 지우기 & 그리기
    screen.fill(BLACK)
    
    # 그리기 영역 테두리
    pygame.draw.rect(screen, BORDER_COLOR, (DRAW_LEFT - 20, DRAW_TOP - 20, DRAW_WIDTH + 40, DRAW_HEIGHT + 40), 20, border_radius=15)
    screen.blit(draw_surf, (DRAW_LEFT, DRAW_TOP))
    
    # Knob 그리기
    draw_knob(screen, knob1_center, total_angle1)
    draw_knob(screen, knob2_center, total_angle2)
    
    # 안내 텍스트 (폰트 에러 방지 위해 기본 폰트 사용)
    try:
        font = pygame.font.SysFont("malgungothic", 24, bold=True)
    except:
        font = pygame.font.SysFont(None, 24)  # 기본 폰트 fallback
    text = font.render("왼쪽 Knob: 좌우 / 오른쪽 Knob: 상하 | 스페이스: 지우기 | 마우스 드래그로 돌리기!", True, WHITE)
    screen.blit(text, (20, 20))
    
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)  # 60 FPS로 안정화

# 종료
pygame.quit()
sys.exit()