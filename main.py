#* ***********************************************************************
# Dip Khadka and Harsit Baral
# Assignment 3 - Medieval Battle
# Block 8
# Completed: June 12, 2024

#This program is my own work - DIP KHADKA and HARSIT BARAL */
#images and sounds downloaded from google

import pygame
import sys
from Button import Button
from Warrior import Warrior
from Knight import Knight
from Defender import Defender
from Vampire import Vampire
from Lancer import Lancer
from Healer import Healer

#initialize pygame
pygame.init()

#setup display
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Medieval Battle - Harsit + Dip")

#load assets
BACKGROUND = pygame.image.load("assets/background.png")
ATTACK_SOUND = r"assets\swoosh-sound-effect-for-fight-scenes-or-transitions-1-149889.mp3"
GAME_OVER_SOUND = r"assets\game-over-39-199830.mp3"
GAME_LOOP_SOUND = r"assets\game-music-loop-3-144252.mp3"
HEAL_SOUND = r"assets\heal-up-39285.mp3"
#play main game sound
pygame.mixer.Channel(0).play(pygame.mixer.Sound(GAME_LOOP_SOUND), loops=-1)

#load and scale sprites
WARRIOR_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/warrior_idle.png"))
WARRIOR_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/warrior_punch.png"))
KNIGHT_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/knight_idle.png"))
KNIGHT_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/knight_punch.png"))
DEFENDER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/defender_idle.png"))
DEFENDER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/defender_punch.png"))
VAMPIRE_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/vampire_idle.png"))
VAMPIRE_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/vampire_punch.png"))
LANCER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/lancer_idle.png"))
LANCER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/lancer_punch.png"))
HEALER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/healer_idle.png"))
HEALER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/healer_punch.png"))
HEALER_BEHIND_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/healer_idle.png"))

#initialize warriors with attributes
initial_warriors = {
    "warrior" : Warrior("warrior", 50, 5, WARRIOR_IDLE_SPRITE, 0, 0),
    "knight" : Knight("knight", 50, 7, KNIGHT_IDLE_SPRITE, 0, 0),
    "defender" : Defender("defender", 60, 3, 2, DEFENDER_IDLE_SPRITE, 0, 0),
    "vampire" : Vampire("vampire", 40, 4, 0.5, VAMPIRE_IDLE_SPRITE, 0, 0),
    "lancer" : Lancer("lancer", 50, 6, LANCER_IDLE_SPRITE, 0, 0),
    "healer" : Healer("healer", 60, 0, HEALER_IDLE_SPRITE, 0, 0)
}

def return_font(size): #returns font object for rendering text
    return pygame.font.SysFont("Roboto", size)

def fight(warrior_1, warrior_2, healer = None): #handles fight logic between warriors and healers
    #change warrior 1 to punching stance
    warrior_1.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{warrior_1.name}_punch.png"))
    
    #move warriors back and forth for attack animations
    if warrior_1.x == 840:
        warrior_1.sprite = pygame.transform.flip(warrior_1.sprite, True, False)
        warrior_1.x = 480
    elif warrior_1.x == 440:
        warrior_1.x = 800
    
    #calculate damage and adjust health and defense
    if warrior_2.defense >= warrior_1.get_attack():
        warrior_2.health -= warrior_1.get_attack()
    elif warrior_2.defense > 0 and warrior_2.defense < warrior_1.get_attack():
        warrior_2.set_health((warrior_2.get_health() + warrior_2.defense) - warrior_1.get_attack())
        warrior_2.defense -= warrior_1.get_attack()
    else:
        warrior_2.set_health(warrior_2.get_health() - warrior_1.get_attack())

    #heal warrior if healer present
    if healer and warrior_1.name == "warrior":
        warrior_1.set_health(min(warrior_1.get_health() + healer.heal_amount, warrior_1.max_health))

    #check if health drops to or below 0
    if warrior_2.get_health() <= 0:
        return True
    elif warrior_1.get_health() <= 0:
        return False
    
    #fight loop to display health and sprites
    while True:
        warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.health}", True, "white")
        warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.health}", True, "white")
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(warrior_1.sprite, warrior_1.sprite.get_rect(center=(warrior_1.x, 500)))
        SCREEN.blit(warrior_2.sprite, warrior_2.sprite.get_rect(center=(warrior_2.x, 500)))
        if healer:
            SCREEN.blit(HEALER_BEHIND_SPRITE, (300, 445))
        SCREEN.blit(warrior_1_health_text, warrior_1_health_text.get_rect(center=(400, 200)))
        SCREEN.blit(warrior_2_health_text, warrior_2_health_text.get_rect(center=(800, 200)))
        SCREEN.blit(return_font(32).render(f"{chosen_warrior1.name}", True, "white"), (350, 100))
        SCREEN.blit(return_font(32).render(f"{chosen_warrior2.name}", True, "white"), (800, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if warrior_1.x == 480:
                    warrior_1.x = 840
                elif warrior_1.x == 800:
                    warrior_1.x = 440
                
                if warrior_1.get_health() > 0 and warrior_2.get_health() <= 0:
                    return True
                #play attack sounds between hits
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(ATTACK_SOUND))
                return False
            
        pygame.display.update()

def choose_warriors(): #handles UI for choosing warriors
    choose_warriors_text = return_font(36).render("Please choose your warriors:", True, "black")
    choose_warriors_text_rect = choose_warriors_text.get_rect(center=(640, 100))
    
    #create buttons for each warrior type
    choose_warrior_button = Button(WARRIOR_IDLE_SPRITE, (120, 200), None, return_font(40), "white", "white", "warrior")
    choose_knight_button = Button(KNIGHT_IDLE_SPRITE, (320, 200), None, return_font(40), "white", "white", "knight")
    choose_defender_button = Button(DEFENDER_IDLE_SPRITE, (520, 200), None, return_font(40), "white", "white", "defender")
    choose_vampire_button = Button(VAMPIRE_IDLE_SPRITE, (720, 200), None, return_font(40), "white", "white", "vampire")
    choose_lancer_button = Button(LANCER_IDLE_SPRITE, (920, 200), None, return_font(40), "white", "white", "lancer")
    choose_healer_button = Button(HEALER_IDLE_SPRITE, (1120, 200), None, return_font(40), "white", "white", "healer")
    
    warriors_chosen = 0
    chosen_healer = None

    choose_warriors_buttons = [choose_warrior_button, choose_knight_button, 
                               choose_defender_button, choose_vampire_button,
                               choose_lancer_button, choose_healer_button]
    
    #main loop to handle user inputs for choosing warriors
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in choose_warriors_buttons:
                    if button.checkForInput(pygame.mouse.get_pos()):
                        if warriors_chosen == 0:
                            warrior_1 = initial_warriors[button.warrior]
                            if warrior_1.name == "warrior":
                                chosen_healer = initial_warriors["healer"]
                            warriors_chosen += 1
                        elif warriors_chosen == 1:
                            warrior2 = initial_warriors[button.warrior]
                            warriors_chosen += 1
                        if warriors_chosen == 2:
                            return warrior_1, warrior2, chosen_healer
                        
        SCREEN.fill("white")
        SCREEN.blit(choose_warriors_text, choose_warriors_text_rect)
        SCREEN.blit(return_font(32).render("Warrior", True, "black"), (80, 250))
        SCREEN.blit(return_font(32).render("Knight", True, "black"), (280, 250))
        SCREEN.blit(return_font(32).render("Defender", True, "black"), (480, 250))
        SCREEN.blit(return_font(32).render("Vampire", True, "black"), (680, 250))
        SCREEN.blit(return_font(32).render("Lancer", True, "black"), (860, 250))
        SCREEN.blit(return_font(32).render("Healer", True, "black"), (1060, 250))
        for button in choose_warriors_buttons:
            button.update(SCREEN)
        
        pygame.display.update()
    
def resset_warriors(): #resets warriors for new game session
    #make variables global
    global chosen_warrior1, chosen_warrior2, chosen_healer, warrior_1_health_text, warrior_2_health_text, current_turn
    chosen_warrior1, chosen_warrior2, chosen_healer = choose_warriors()
    
    chosen_warrior1.reset_health()
    chosen_warrior2.reset_health()

    chosen_warrior1.x = 440
    chosen_warrior2.x = 840

    warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.get_health()}", True, "white")
    warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.get_health()}", True, "white")

    current_turn = 1

def winner_screen(winner): #displays winner screen
    #play game over sound
    pygame.mixer.music.load(GAME_OVER_SOUND)
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                resset_warriors()
                return
        
        winner_text = return_font(36).render(f"{winner.name} WON!", True, "black")
        play_again_text = return_font(36).render("Click Anywhere to Play Again", True, "black")
        SCREEN.fill("white")
        SCREEN.blit(winner_text, (525, 300))
        SCREEN.blit(play_again_text, (450, 600))
        pygame.display.update()

    
def main_game(): #main game loop
    #make variables global 
    global current_turn, warrior_1_health_text, warrior_2_health_text

    information_text = return_font(30).render("Click anywhere to start a round", True, "white")
    information_text_rect = information_text.get_rect(center=(640, 50))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #start fights on mouse clicks
                if current_turn == 1:
                    if fight(chosen_warrior1, chosen_warrior2, chosen_healer): #start fight between warriors
                        winner_screen(chosen_warrior1)
                    if chosen_healer: #play healing sounds if healer present
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(HEAL_SOUND))
                    current_turn = 2
                elif current_turn == 2:
                    if fight(chosen_warrior2, chosen_warrior1, chosen_healer):
                        winner_screen(chosen_warrior2)
                    current_turn = 1
                    
        SCREEN.blit(BACKGROUND, (0, 0))
        #display sprites for fights
        chosen_warrior1.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{chosen_warrior1.name}_idle.png"))
        chosen_warrior2.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{chosen_warrior2.name}_idle.png"))
        chosen_warrior2.sprite = pygame.transform.flip(chosen_warrior2.sprite, True, False)
        if chosen_healer:
            SCREEN.blit(HEALER_BEHIND_SPRITE, (300, 445))
        chosen_warrior1.x = 440
        chosen_warrior2.x = 840
        SCREEN.blit(warrior_1_health_text, warrior_1_health_text.get_rect(center=(400, 200)))
        SCREEN.blit(warrior_2_health_text, warrior_2_health_text.get_rect(center=(800, 200)))
        warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.health}", True, "white")
        warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.health}", True, "white")
        SCREEN.blit(return_font(32).render(f"{chosen_warrior1.name}", True, "white"), (350, 100))
        SCREEN.blit(return_font(32).render(f"{chosen_warrior2.name}", True, "white"), (800, 100))
        SCREEN.blit(chosen_warrior1.sprite, chosen_warrior1.sprite.get_rect(center=(chosen_warrior1.x, 500)))
        SCREEN.blit(chosen_warrior2.sprite, chosen_warrior2.sprite.get_rect(center=(chosen_warrior2.x, 500)))
        SCREEN.blit(information_text, information_text_rect)
        
        pygame.display.update()

resset_warriors() 
main_game()