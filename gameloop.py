# Nhập các thư viện cần thiết
import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Tạo một màn hình có kích thước 600x600 pixel
screen = pygame.display.set_mode((600, 600))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Trò chơi con rắn")

# Tạo một đối tượng con rắn có màu xanh lá cây, kích thước 20x20 pixel và vị trí ban đầu là (300, 300)
snake = pygame.Rect(300, 300, 20, 20)
snake_color = (0, 255, 0)

# Tạo một danh sách để lưu trữ các phần thân của con rắn
snake_body = [snake]

# Tạo một biến để lưu trữ hướng di chuyển của con rắn, ban đầu là phải
snake_direction = "right"

# Tạo một đối tượng thức ăn có màu đỏ, kích thước 20x20 pixel và vị trí ngẫu nhiên
food = pygame.Rect(random.randint(0, 580), random.randint(0, 580), 20, 20)
food_color = (255, 0, 0)

# Tạo một biến để lưu trữ điểm số của người chơi, ban đầu là 0
score = 0

# Tạo một đối tượng font để hiển thị điểm số
font = pygame.font.SysFont("Arial", 32)

# Tạo một vòng lặp chính để xử lý các sự kiện và cập nhật trạng thái của trò chơi
while True:
    # Xử lý các sự kiện từ bàn phím
    for event in pygame.event.get():
        # Nếu người chơi nhấn phím thoát, thoát khỏi vòng lặp
        if event.type == pygame.QUIT:
            sys.exit()
        # Nếu người chơi nhấn phím mũi tên, thay đổi hướng di chuyển của con rắn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            if event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            if event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Cập nhật vị trí của con rắn theo hướng di chuyển
    if snake_direction == "up":
        snake.y -= 20
    if snake_direction == "down":
        snake.y += 20
    if snake_direction == "left":
        snake.x -= 20
    if snake_direction == "right":
        snake.x += 20

    # Kiểm tra xem con rắn có va chạm với biên của màn hình hay không, nếu có thì kết thúc trò chơi
    if snake.x < 0 or snake.x > 580 or snake.y < 0 or snake.y > 580:
        print("Bạn đã thua!")
        break

    # Kiểm tra xem con rắn có ăn được thức ăn hay không, nếu có thì tăng điểm số, tăng kích thước của con rắn và tạo thức ăn mới
    if snake.colliderect(food):
        score += 1
        snake_body.append(snake.copy())
        food.x = random.randint(0, 580)
        food.y = random.randint(0, 580)

    # Kiểm tra xem con rắn có cắn vào thân của mình hay không, nếu có thì kết thúc trò chơi
    for body_part in snake_body[1:]:
        if snake.colliderect(body_part):
            print("Bạn đã thua!")
            break

    # Cập nhật vị trí của các phần thân của con rắn theo đầu con rắn
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i-1].x
        snake_body[i].y = snake_body[i-1].y

    # Vẽ nền màu trắng cho màn hình
    screen.fill((255, 255, 255))

    # Vẽ con rắn và thức ăn lên màn hình
    for body_part in snake_body:
        pygame.draw.rect(screen, snake_color, body_part)
    pygame.draw.rect(screen, food_color, food)

    # Tạo một đối tượng text để hiển thị điểm số
    text = font.render("Điểm: " + str(score), True, (0, 0, 0))

    # Vẽ text lên màn hình ở góc trên bên trái
    screen.blit(text, (0, 0))

    # Cập nhật màn hình
    pygame.display.flip()

    # Đợi 0.1 giây
    pygame.time.wait(100)
