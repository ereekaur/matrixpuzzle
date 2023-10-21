import pygame
import random

## ----------------
## MATRIX PUZZLE
## (c) Erno Kauranen
## ---------------

pygame.init()
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix puzzle")
logics = []

def generate_binary_matrix_with_red_square(position):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matrix[0][position] = 1
    return matrix

def difficult(position):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if position == 0:
        matrix = [[1, 0, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
    elif position == 1:
        matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
    elif position == 2:
        matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    elif position == 3:
        matrix = [[1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    return matrix


def morediff(position):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if position == 0:
        matrix = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif position == 1:
        matrix =[[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif position == 2:
        matrix =[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]]
    elif position == 3:
        matrix = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1 ,1]]
    return matrix

def display_question_mark(x, y, size=50, color=(0, 0, 255)):
    pygame.draw.rect(WINDOW, color, (x, y, size, size))
    font = pygame.font.Font(None, 100)
    text = font.render("?", True, (255, 255, 255))
    text2 = font.render("->", True, (255, 155, 0))
    text3 = font.render("->", True, (255, 155, 0))
    text4 = font.render("->", True, (255, 155, 0))

    text_rect = text.get_rect(center=(x + size / 2, y + size / 2))
    text_rect2 = text.get_rect(center=(500,170))
    text_rect3 = text.get_rect(center=(250,170))
    text_rect4 = text.get_rect(center=(750,170))
    WINDOW.blit(text, text_rect)
    WINDOW.blit(text2, text_rect2)
    WINDOW.blit(text3, text_rect3)
    WINDOW.blit(text4, text_rect4)

def moving_red_square(position):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    if position == 0:
        matrix[0][0] = 1  
    elif position == 1:
        matrix[0][3] = 1  
    elif position == 2:
        matrix[3][3] = 1  
    elif position == 3:
        matrix[3][0] = 1  
    return matrix

def randomsquare(monesko,tmp,question_number):
    
    matrix = tmp
    while tmp == matrix:
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        random_row = random.randint(0, 3)
        random_col = random.randint(0, 3)
        matrix[random_row][random_col] = 1
   
    if monesko == 2:

        return logics[2][question_number]
    
    if monesko == 3:
        return [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1]]
    
    
    return matrix


# --- Questions and the answer is stored to list --------------------


question1 =        [generate_binary_matrix_with_red_square(0),
                   generate_binary_matrix_with_red_square(1),
                   generate_binary_matrix_with_red_square(2),
                   generate_binary_matrix_with_red_square(3)]


question2 = [      moving_red_square(0),
                   moving_red_square(1),
                   moving_red_square(2),
                   moving_red_square(3)]

question4 =         [difficult(0),
                   difficult(1),
                   difficult(2),
                   difficult(3)]

question3 =        [morediff(0),
                   morediff(1),
                   morediff(2),
                   morediff(3)]


# ------ Add questions to list --------------

logics.append(question1)
logics.append(question2)
logics.append(question3)
logics.append(question4)

#------------------------------------------

def display_matrix(matrix, x, y, square_size=50, grid_color=(0, 0, 0)):
    for i in range(4):
        for j in range(4):
            color = (255, 0, 0) if matrix[i][j] == 1 else (255, 255, 255) 
            pygame.draw.rect(WINDOW, color, (x + j * square_size, y + i * square_size, square_size, square_size))
            pygame.draw.rect(WINDOW, grid_color, (x + j * square_size, y + i * square_size, square_size, square_size), 1)

def create_button(x, y, width, height, color, text, text_color, font_size, action=None):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    pygame.draw.rect(WINDOW, color, (x, y, width, height))
    WINDOW.blit(text_surface, text_rect)
    return (x, y, width, height, action)

def check_answer(selected_option, correct_option):
    return selected_option == correct_option

running = True
score = 0

buttons = []

for question_number in range(4):
    
    options = [logics[question_number][3]]
    tmp= logics[question_number][3]
    options += [randomsquare(question_number, tmp,_) for _ in range(2)]

   
    random.shuffle(options)
    
    
    correct_option = options.index(logics[question_number][3])


    buttons.append(create_button(160, 600, 150, 50, (0, 255, 0), "Option 1", (0, 0, 0), 24, action=0))
    buttons.append(create_button(405, 600, 150, 50, (0, 255, 0), "Option 2", (0, 0, 0), 24, action=1))
    buttons.append(create_button(650, 600, 150, 50, (0, 255, 0), "Option 3", (0, 0, 0), 24, action=2))

    question_answered = False

    while not question_answered and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in buttons:
                    x, y, width, height, action = button
                    if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                        if check_answer(action, correct_option):
                            score += 1
                        question_answered = True

        WINDOW.fill((0, 0, 0))  
        
        
        for i in range(3):
            display_matrix(logics[question_number][i], 50 + i * 250, 100, square_size=40)

        # Display the answer matrices
        for i, matrix in enumerate(options):
            x = 150 + i * 250  
            y = 400  
            display_matrix(matrix, x, y, square_size=40)  

        # Display the buttons
        for button in buttons:
            x, y, width, height, _ = button
            pygame.draw.rect(WINDOW, (0, 255, 0), (x, y, width, height))

       
        display_question_mark(50 + (i + 1) * 250, 100, size=150, color=(0, 0, 255))

        pygame.display.update()

    buttons.clear()


def display_iq_score(score, x, y, font_size=136, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text = "Score: "
    if score == 0:
        text += "50 IQ"
    elif score == 1:
        text += "80 IQ"
    elif score == 2:
        text += "100 IQ"
    elif score == 3:
        text += "150 IQ"
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    WINDOW.blit(text_surface, text_rect)

# points display

running_iq_screen = True

while running_iq_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_iq_screen = False

    WINDOW.fill((0, 0, 0))

    
    display_iq_score(score, 150, 250)

    pygame.display.update()

pygame.quit()
