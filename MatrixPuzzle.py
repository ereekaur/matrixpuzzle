import pygame
import random

"""
File: MatrixPuzzle.py
Author: Erno Kauranen
Date: 2023-11-07
Description: Quiz game

"""
temp_variable = 1
temp_variable2 = 1
temp_variable3 = 1
temp_variable4 = 1
temp_variable6 = 1
pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Puzzle")

font = pygame.font.Font(None, 36)
input_text = ''
input_rect = pygame.Rect(300, 300, 340, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
active = False
player_name = None
name_entered = False


while not name_entered:
   
    text1 = "To start the game click the field below, type your name and press Enter"
    text2 = "WARNING! The game starts immediately!"

    text_surface1 = font.render(text1, True, (255,0,0)) 
    text_surface2 = font.render(text2, True, (255,0,0))   

    window.blit(text_surface1, (120, 150))
    window.blit(text_surface2, (220, 450))
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_passive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    player_name = input_text
                    input_text = ''
                    name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

  
    pygame.draw.rect(window, color, input_rect)
    text_surface = font.render(input_text, True, (0, 0, 0))
    window.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.flip()


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix puzzle")
logics = []
start_time = pygame.time.get_ticks()

def grate_bnry_matrix_with_red_sq(position):
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

def moredifff(position):
    
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if position == 0:
        matrix = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif position == 1:
        matrix =[[1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif position == 2:
        matrix = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0]]
    elif position == 3:
        matrix = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
    return matrix

def morediffff(position):
    
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if position == 0:
        matrix = [[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1]]
    elif position == 1:
        matrix =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    elif position == 2:
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
    elif position == 3:
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
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

def movingsq(position):
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

def mirror(position):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    if position == 0:
        matrix =[[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
    elif position == 1:
        matrix =[[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]]
    elif position == 2:
        matrix =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
    elif position == 3:
        matrix =[[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
    return matrix

def diagonal(position):
    
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    if position == 0:
        matrix =[[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]] 
    elif position == 1:
        matrix =[[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif position == 2:
        matrix =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    elif position == 3:
        matrix =[[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]

    return matrix

def randomsquare(monesko,tmp,question_number):
    
    matrix = tmp
    while tmp == matrix:
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        random_row = random.randint(0, 3)
        random_col = random.randint(0, 3)
        matrix[random_row][random_col] = 1
   
    if monesko == 2:

        global temp_variable3
        for i in range(2):
                
                if temp_variable3 == 1:
                
                    temp_variable3 +=1
                    return [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
                    
                else: 
                
                    return [[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0]]
    
    if monesko == 3:
        global temp_variable4
        for i in range(2):
             
             if temp_variable4 == 1:
             
                 temp_variable4 +=1
                 return [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
                 
             else: 
              
              matrix =[[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
        
       
    if monesko == 4:
            global temp_variable
            for i in range(2):
             
             if temp_variable == 1:
             
                 temp_variable +=1
                 return [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
                 
             else: 
              
              return [[0, 0, 0,0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1]]
    
    if monesko == 5:
            global temp_variable2
            for i in range(2):
             
             if temp_variable2 == 1:
             
                 temp_variable2 +=1
                 return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                 
             else: 
              
              return [[0, 0, 0,0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
             

    if monesko == 6:
        return logics[monesko][question_number]
    
    if monesko == 7:
        global temp_variable6
        
        for i in range(2):
             
             if temp_variable6 == 1:
             
                 temp_variable6 +=1
                 return [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                 
             else: 
              
              return [[0, 0, 0,0 ], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]   
    return matrix


logics = []
functions = [grate_bnry_matrix_with_red_sq, movingsq, morediff,mirror, moredifff, morediffff,difficult,diagonal]

for func in functions:
    questions = [func(i) for i in range(4)]
    logics.append(questions)

def display_matrix(matrix, x, y, square_size = 50, grid_color=(0, 0, 0)):
    for i in range(4):
        for j in range(4):
            color = (255, 0, 0) if matrix[i][j] == 1 else (255, 255, 255) 
            pygame.draw.rect(WINDOW, color, (x + j * square_size, y + i * square_size, square_size, square_size))
            pygame.draw.rect(WINDOW, grid_color, (x + j * square_size, y + i * square_size, square_size, square_size), 1)

def create_button(x, y, width, height, color, text, text_color, font_size, action=None):

    return (x, y, width, height, action, color, text)

def check_answer(selected_option, correct_option):
    
    return selected_option == correct_option

def format_time(milliseconds):
    total_seconds = milliseconds // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"Time: {minutes:02d}:{seconds:02d}"

running = True
score = 0
buttons = []

for question_number in range(len(logics)):

    
    options = [logics[question_number][3]]
    tmp = logics[question_number][3]
    options += [randomsquare(question_number, tmp,_) for _ in range(2)]

    random.shuffle(options)
    
    correct_option = options.index(logics[question_number][3])

    buttons.append(create_button(155, 600, 150, 50, (0, 255, 0), "Option 1", (255, 0, 0), 24, action=0))
    buttons.append(create_button(405, 600, 150, 50, (0, 255, 0), "Option 2", (255, 0, 0), 24, action=1))
    buttons.append(create_button(655, 600, 150, 50, (0, 255, 0), "Option 3", (255, 0, 0), 24, action=2))

    question_answered = False
    time_limit = 60000
    elapsed_time = pygame.time.get_ticks() - start_time
    
    remaining_time = max(time_limit - elapsed_time, 0)
    if elapsed_time >= time_limit:
            running =  question_answered  
            
    while not question_answered and running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in buttons:
                    x, y, width, height, action, color, text= button
                    if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                        if check_answer(action, correct_option):
                            score += 1
                        question_answered = True
                    
        WINDOW.fill((0, 0, 0))  

        elapsed_time = pygame.time.get_ticks() - start_time
        time_limit = 60000
        remaining_time = max(time_limit - elapsed_time, 0)
        WINDOW.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        timer_text = font.render(format_time(remaining_time), True, (255, 255, 255))
        timer_rect = timer_text.get_rect()
        timer_rect.topleft = (10, 10)
        WINDOW.blit(timer_text, timer_rect)
        if remaining_time <= 0:
            running = False
        for i in range(3):
            display_matrix(logics[question_number][i], 50 + i * 250, 100, square_size=40)

        # Display the answer matrices
        for i, matrix in enumerate(options):
            x = 150 + i * 250  
            y = 400  
            display_matrix(matrix, x, y, square_size = 40)  

        # Display the buttons
        for button in buttons:
            x, y, width, height, action, color, text = button
            pygame.draw.rect(WINDOW, (0, 0, 255), (x, y, width, height))
            text_surface = font.render(text, True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x + width / 2, y + height / 2)  
            WINDOW.blit(text_surface, text_rect)
            
        display_question_mark(50 + (i + 1) * 250, 100, size=150, color=(0, 0, 255))

        pygame.display.update()

    buttons.clear()

def display_iq_score(score, x, y, font_size=66, color=(255, 255, 255)):
    
    font = pygame.font.Font(None, font_size)

    text = "Your estimated IQ is: ~ "
    if score == 0:
        text += "50"
    elif score == 1:
        text += "80"
    elif score == 2:
        text += "90"
    elif score == 3:
        text += "100"
    elif score == 4:
        text += "105"
    elif score == 5:
        text += "110"
    elif score == 6:
        text += "120"
    elif score == 7:
        text += "128"
    else:
        text = "Your estimated IQ is over 135"

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)

    WINDOW.blit(text_surface, text_rect)

running_iq_screen = True

while running_iq_screen:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_iq_screen = False

    WINDOW.fill((0, 0, 0))

    
    display_iq_score(score, 150, 250)

    pygame.display.update()


if player_name is not None:
    with open('player_scores.txt', 'a') as file:
        file.write(f"Name: {player_name}, Score: {score}, IQ: {text}\n")

pygame.quit()
