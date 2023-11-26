# Nhập các thư viện cần thiết
import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Tạo một màn hình có kích thước 600x600 pixel
screen = pygame.display.set_mode((600, 600))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Trò chơi snack")

# Tạo một đối tượng snack có màu vàng, kích thước 20x20 pixel và vị trí ban đầu là (300, 300)
snack = pygame.Rect(300, 300, 20, 20)
snack_color = (255, 255, 0)

# Tạo một danh sách để lưu trữ các phần thân của snack
snack_body = [snack]

# Tạo một biến để lưu trữ hướng di chuyển của snack, ban đầu là phải
snack_direction = "right"

# Tạo một đối tượng thức ăn có màu đỏ, kích thước 20x20 pixel và vị trí ngẫu nhiên
food = pygame.Rect(random.randint(0, 580), random.randint(0, 580), 20, 20)
food_color = (255, 0, 0)

# Tạo một biến để lưu trữ điểm số của người chơi, ban đầu là 0
score = 0

# Tạo một biến để lưu trữ tốc độ của snack, ban đầu là 20 pixel mỗi lần di chuyển
snack_speed = 20

# Tạo một đối tượng font để hiển thị điểm số
font = pygame.font.SysFont("Arial", 32)

# Tạo một vòng lặp chính để xử lý các sự kiện và cập nhật trạng thái của trò chơi
while True:
    # Xử lý các sự kiện từ bàn phím
    for event in pygame.event.get():
        # Nếu người chơi nhấn phím thoát, thoát khỏi vòng lặp
        if event.type == pygame.QUIT:
            sys.exit()
        # Nếu người chơi nhấn phím mũi tên, thay đổi hướng di chuyển của snack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snack_direction != "down":
                snack_direction = "up"
            if event.key == pygame.K_DOWN and snack_direction != "up":
                snack_direction = "down"
            if event.key == pygame.K_LEFT and snack_direction != "right":
                snack_direction = "left"
            if event.key == pygame.K_RIGHT and snack_direction != "left":
                snack_direction = "right"

    # Cập nhật vị trí của snack theo hướng di chuyển và tốc độ
    if snack_direction == "up":
        snack.y -= snack_speed
    if snack_direction == "down":
        snack.y += snack_speed
    if snack_direction == "left":
        snack.x -= snack_speed
    if snack_direction == "right":
        snack.x += snack_speed

    # Kiểm tra xem snack có va chạm với biên của màn hình hay không, nếu có thì kết thúc trò chơi
    if snack.x < 0 or snack.x > 580 or snack.y < 0 or snack.y > 580:
        print("Bạn đã thua!")
        break

    # Kiểm tra xem snack có ăn được thức ăn hay không, nếu có thì tăng điểm số, tăng kích thước của snack, tăng tốc độ của snack và tạo thức ăn mới
    if snack.colliderect(food):
        score += 1
        snack_body.append(snack.copy())
        food.x = random.randint(0, 580)
        food.y = random.randint(0, 580)
        snack_speed += 1

    # Kiểm tra xem snack có cắn vào thân của mình hay không, nếu có thì kết thúc trò chơi
    for body_part in snack_body[1:]:
        if snack.colliderect(body_part):
            print("Bạn đã thua!")
            break

    # Cập nhật vị trí của các phần thân của snack theo đầu snack
    for i in range(len(snack_body) - 1, 0, -1):
        snack_body[i].x = snack_body[i-1].x
        snack_body[i].y = snack_body[i-1].y

    # Vẽ nền màu trắng cho màn hình
    screen.fill((255, 255, 255))

    # Vẽ snack và thức ăn lên màn hình
    for body_part in snack_body:
        pygame.draw.rect(screen, snack_color, body_part)
    pygame.draw.rect(screen, food_color, food)

    # Tạo một đối tượng text để hiển thị điểm số
    text = font.render("Điểm: " + str(score), True, (0, 0, 0))

    # Vẽ text lên màn hình ở góc trên bên trái
    screen.blit(text, (0, 0))

    # Cập nhật màn hình
    pygame.display.flip()

    # Đợi 0.1 giây
    pygame.time.wait(100)
