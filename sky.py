###########################################################################################################
###################################################GAME####################################################
# $   $   $   $             ***************         @@@         **************              $   $   $   $ #
#PLAN

from pygame import mixer
import pygame
import random
import time
import sys
import os

def main_sky(event):

        pygame.quit()

        #red - камень (нужно уклонятся от камней -1 ХР)
        #green - мяч (нужно соберать мячики +1 бал)
        #blue - ХР (+1 ХР)
        pygame.init()


        infoObject = pygame.display.Info()

        #win = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

        win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #win=pygame.display.set_mode((1000,600))

        pygame.display.set_caption("Iok Jump")

        icon=pygame.image.load('media/game_icons/icon.png')
        pygame.display.set_icon(icon)
         
        bgraund = pygame.image.load("media/game_icons/bg.png")

        clock=pygame.time.Clock()

        hero = pygame.image.load('media/game_icons/characters/airplanes/1.png')

        meteor1 = pygame.image.load('media/meteors/1.png')
        meteor2 = pygame.image.load('media/meteors/2.png')
        meteor3 = pygame.image.load('media/meteors/3.png')

        ufo = pygame.image.load('media/game_icons/characters/airplanes/direshabel.png')
        
        coin = pygame.image.load('media/game_icons/coin.png')

        MUSIC = os.path.abspath('media/music/background_msc.mp3')

        heart_icon = pygame.image.load('media/game_icons/heart_icon.png')
        cup_icon = pygame.image.load('media/game_icons/cup_icon.png')

        trash1 = pygame.image.load('media/trash/1.png')
        trash2 = pygame.image.load('media/trash/2.png')
        trash3 = pygame.image.load('media/trash/3.png')

        explosion = [
            pygame.image.load("media/explosion/1.png"),
            pygame.image.load("media/explosion/2.png"),
            pygame.image.load("media/explosion/3.png"),
            pygame.image.load("media/explosion/4.png"),
            pygame.image.load("media/explosion/5.png")
        ]


        MUSIC = os.path.abspath('media/music/background_msc.mp3')
        music_file = open('configs/music_file.txt')
        for line in music_file:
            print(line)
        if line == 'True':
            mixer.init()
            mixer.music.load(MUSIC)
            mixer.music.play(-1, 0.0)
        else:
            pass

        schet = 0
        XP = 5

        my_coin = open("My_Coin.txt", "r")
        coins = my_coin.read()
        my_coin.close()

        #####################################################################################################################

        read_score = open("last_score.txt", "r")
        last_score = read_score.read()
        read_score.close()

        best_score = open("best_score.txt", "r")
        best_score_input = best_score.read()
        best_score.close()


        f2 = pygame.font.Font(None, 50)
        text2 = f2.render(str(XP), 10, (180, 0, 0))
        
        f = pygame.font.Font(None, 50)
        text = f.render(str(schet), 10, (0, 180, 0))

        f3 = pygame.font.Font(None, 40)
        text3 = f3.render("Last score: " + str(last_score), 10, (0, 180, 0))

        f4 = pygame.font.Font(None, 50)
        text4 = f4.render("Coin: " + str(coins), 10, (0, 180, 0))

        f5 = pygame.font.Font(None, 40)
        text5 = f5.render("Best score: " + str(best_score_input), 10, (0, 180, 0))

    #######################################################################################################################

        width=50
        height=140
        x=infoObject.current_w -width
        y= int(infoObject.current_h) - 150


        speed=23

    #################################################################################################################################3

        ball_width = 100
        ball_height = 100
        ball_x = random.randint(0, int(infoObject.current_w))
        ball_y = -ball_height

        ball2_width = 100
        ball2_height = 100
        ball2_x = random.randint(0, int(infoObject.current_w))
        ball2_y = -ball2_height

        ball3_width = 100
        ball3_height = 100
        ball3_x = random.randint(0, int(infoObject.current_w))
        ball3_y = -ball3_height


        ########################################################################################################################

        kamenyka1_width = 100
        kamenyka1_height = 120
        kamenyka1_x = random.randint(0, int(infoObject.current_w))
        kamenyka1_y = -kamenyka1_height


        kamenyka2_width = 100
        kamenyka2_height = 120
        kamenyka2_x = random.randint(0, int(infoObject.current_w))
        kamenyka2_y = -kamenyka2_height


        kamenyka3_width = 100
        kamenyka3_height = 120
        kamenyka3_x = random.randint(0, int(infoObject.current_w))
        kamenyka3_y = -kamenyka3_height


        #########################################################################################################################3


        ###############################################################################################################################

        turtle_width = 40
        turtle_height = 30
        turtle_x = -2 * turtle_width
        turtle_y = (int(infoObject.current_h) - 100)

        ###############################################################################################################################
        
        patron_x = x + 20
        patron_y = y
        patron_width = 10
        patron_height = 20

        patron = False

    ##################################################################################################################

        isjump=False
        jumpcount=12

        lastmove="right"

        run=True

        heart_x = 0
        heart_y = 0

        cup_x = 0
        cup_y = 55

        star_x = random.randint(0, infoObject.current_w)
        star_y = random.randint(0, infoObject.current_h)

        while run:

            pygame.time.delay(35)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False

            keys=pygame.key.get_pressed()

            ball_y += 16
            ball2_y += 18
            ball3_y += 20

            k = 14
            k1 = 16
            k2 = 18
            k3 = 20

            kamenyka1_y += 22
            kamenyka2_y += 24
            kamenyka3_y += 26

            tur = 30

            turtle_x += tur



            if turtle_x > int(infoObject.current_w):
                turtle_x = -turtle_width

                       
        #########################################################################################################################3

            if kamenyka1_y > int(infoObject.current_h):
                kamenyka1_y = -kamenyka1_height
                kamenyka1_x = random.randint(0, int(infoObject.current_w) - kamenyka1_width)


            if kamenyka2_y > int(infoObject.current_h):
                kamenyka2_y = -kamenyka1_height
                kamenyka2_x = random.randint(0, int(infoObject.current_w) - kamenyka2_width)


            if kamenyka3_y > int(infoObject.current_h):
                kamenyka3_y = -kamenyka1_height
                kamenyka3_x = random.randint(0, int(infoObject.current_w) - kamenyka3_width)
                

        ####################################################################################################################

            if ball_y > int(infoObject.current_h):
                ball_y = -ball_height
                ball_x = random.randint(0, int(infoObject.current_w) - ball_width)

            if ball2_y > int(infoObject.current_h):
                ball2_y = -ball2_height
                ball2_x = random.randint(0, int(infoObject.current_w) - ball2_width)

            if ball3_y > int(infoObject.current_h):
                ball3_y = -ball3_height
                ball3_x = random.randint(0, int(infoObject.current_w) - ball3_width)

        ##################################################################################################################################################

            #мяч

                #обработчик столкновения с ball
            if (x < (ball_x + ball_width) and (x + width) > ball_x and y < (ball_y + ball_height) and (height + y) > ball_y):
                schet += 1
                text = f.render(str(schet), 10, (0, 180, 0))
                ball_y = 0
                ball_x = random.randint(0, int(infoObject.current_w) - ball_width)


                #обработчик столкновения с ball2
            if (x < (ball2_x + ball2_width) and (x + width) > ball2_x and y < (ball2_y + ball2_height) and (height + y) > ball2_y):
                schet += 1
                text = f.render(str(schet), 10, (0, 180, 0))
                ball2_y = 0
                ball2_x = random.randint(0, int(infoObject.current_w) - ball2_width)


                #обработчик столкновения с ball3

            if (x < (ball3_x + ball3_width) and (x + width) > ball3_x and y < (ball3_y + ball3_height) and (height + y) > ball3_y):
                schet += 1
                text = f.render(str(schet), 10, (0, 180, 0))
                ball3_y = 0
                ball3_x = random.randint(0, int(infoObject.current_w) - ball3_width)

           # if (x + 39 >= turtle_x and x <= turtle_x + turtle_width - 1 and y + 40 == turtle_y):
        ###################################################################################################################################3

            #камни

                #обработка столкновения с kamenyka1
            if (x < (kamenyka1_x + kamenyka1_width) and (x + width) > kamenyka1_x and y < (kamenyka1_y + kamenyka1_height) and (height + y) > kamenyka1_y):
                XP -= 1
                text2 = f2.render(str(XP), 10, (180, 0, 0))
                kamenyka1_y = -kamenyka1_height
                kamenyka1_x = random.randint(0, int(infoObject.current_w) - kamenyka1_width)


                #обработка столкновения с kamenyka2
            if (x < (kamenyka2_x + kamenyka2_width) and (x + width) > kamenyka2_x and y < (kamenyka2_y + kamenyka2_height) and (height + y) > kamenyka2_y):
                XP -= 1
                text2 = f2.render(str(XP), 10, (180, 0, 0))
                kamenyka2_y = -kamenyka2_height
                kamenyka2_x = random.randint(0, int(infoObject.current_w) - kamenyka2_width)


                #обработка столкновения с kamenyka3
            if (x < (kamenyka3_x + kamenyka3_width) and (x + width) > kamenyka3_x and y < (kamenyka3_y + kamenyka3_height) and (height + y) > kamenyka3_y):
                XP -= 1
                text2 = f2.render(str(XP), 10, (180, 0, 0))
                kamenyka3_y = -kamenyka3_height
                kamenyka3_x = random.randint(0, int(infoObject.current_w) - kamenyka3_width)

        ###############################################################################################################################

        ######################################################################################################################################

        #turtle

            if (x < (turtle_x + turtle_width) and (x + width) > turtle_x and y < (turtle_y + turtle_height) and (height + y) > turtle_y):            
                XP -= 2
                text2 = f2.render(str(XP), 10, (180, 0, 0))
                turtle_x = -turtle_width
            else:
                pass


        ######################################################################################################################################

        #patron

            if (patron_x + 20 >= kamenyka1_x and patron_x <= kamenyka1_x + kamenyka1_width and patron_y >= kamenyka1_y and patron_y <= kamenyka1_y + 20):
                kamenyka1_y = -kamenyka1_height
                patron = False
                patron_y = y
                patron_x = x + 20
                win.blit(explosion[1], (patron_x, patron_y))

            if (patron_x + 20 >= kamenyka2_x and patron_x <= kamenyka2_x + kamenyka2_width and patron_y >= kamenyka2_y and patron_y <= kamenyka2_y + 20):
                kamenyka2_y = -kamenyka2_height
                patron = False
                patron_y = y
                patron_x = x + 20
                win.blit(explosion[1], (patron_x, patron_y))

            if (patron_x + 20 >= kamenyka3_x and patron_x <= kamenyka3_x + kamenyka3_width and patron_y >= kamenyka3_y and patron_y <= kamenyka3_y + 20):
                kamenyka3_y = -kamenyka3_height
                patron = False
                patron_y = y
                patron_x = x + 20
                win.blit(explosion[1], (patron_x, patron_y))


############################################################################################################

        

    ######################################################################################################################################################


            if keys[pygame.K_LEFT] and x>5 :
                x-=speed
                patron_x -= 23
                lastmove="left"
            if keys[pygame.K_RIGHT] and x < int(infoObject.current_w)-width-5:
                x+=speed
                patron_x += 23
                lastmove="right"
            if not(isjump):
                if keys[pygame.K_SPACE]:
                    isjump=True
            else:
                if jumpcount >=-12:
                    if jumpcount < 0:
                        y+=(jumpcount**2)/2
                        patron_y += (jumpcount**2)/2
                    else:
                        y-=(jumpcount**2)/2
                        patron_y -= (jumpcount**2)/2
                    jumpcount-=1
                else:
                    isjump=False
                    jumpcount=12


    #################################################################################################################


            if XP <= 0:
                pygame.quit()

    #################################################################################################################

            win.fill((0,0,0))

          #  win.blit(hero,(x-30,y-25))
          #  win.blit(bgraund, (0, 0))

            for i in range(10):
                a = random.randint(1, 20)
                if a % 2 == 0:
                   pygame.draw.circle(win, (255, 255, 255), (star_x, star_y), 1)
                   star_x = random.randint(0, infoObject.current_w)
                   star_y = random.randint(0, infoObject.current_h)
                    
                else:
                    pygame.draw.circle(win, (255, 255, 255), (star_x, star_y), 3)
                    star_x = random.randint(0, infoObject.current_w)
                    star_y = random.randint(0, infoObject.current_h)


            win.blit(trash1, (kamenyka1_x,kamenyka1_y))
            win.blit(trash2,(kamenyka2_x,kamenyka2_y))
            win.blit(trash3,(kamenyka3_x,kamenyka3_y))

            pygame.draw.rect(win, (0, 0, 255), (patron_x, patron_y, patron_width, patron_height))

            win.blit(hero, (x - 25, y))


            win.blit(text, (55, 60))
            win.blit(text2, (55, 10))
            win.blit(text3, (infoObject.current_w - 200, 0))
            win.blit(text5, (infoObject.current_w - 200, 30))

            win.blit(heart_icon,(heart_x,heart_y))
            win.blit(cup_icon,(cup_x,cup_y))

            win.blit(text4, (infoObject.current_w / 2, 0)) 
            
            #meteors


            #win.blit(meteor1,(kamenyka1_x,kamenyka1_y))
            #win.blit(meteor2,(kamenyka2_x,kamenyka2_y))
            #win.blit(meteor3,(kamenyka3_x,kamenyka3_y))

            #UFO
            win.blit(ufo,(turtle_x - 15, turtle_y - 10))
            
            #game coin
            win.blit(coin,(ball_x,ball_y))
            win.blit(coin,(ball2_x,ball2_y))
            win.blit(coin,(ball3_x,ball3_y))




            if keys[pygame.K_UP] and patron_y == int(infoObject.current_h) - 150:
                patron = True

            if patron == True:
                patron_y -= 30

            if patron_y <= -patron_height:
                patron = False
                patron_y = y
                patron_x = x + 20



           # win.blit(ball, (ball_x, ball_y))
          #  win.blit(ball2, (ball2_x, ball2_y))
           # win.blit(ball3, (ball3_x, ball3_y))

            #pygame.draw.rect(win,(0,0,255),(x,y,width,height))

            #pygame.draw.rect(win, (0, 255, 0), (ball_x, ball_y, ball_width, ball_height))
            #pygame.draw.rect(win, (0, 255, 0), (ball2_x, ball2_y, ball2_width, ball2_height))
            #pygame.draw.rect(win, (0, 255, 0), (ball3_x, ball3_y, ball3_width, ball3_height))

          #  pygame.draw.rect(win, (255, 0, 0), (kamenyka1_x, kamenyka1_y, kamenyka1_width, kamenyka1_height))
           # pygame.draw.rect(win, (255, 0, 0), (kamenyka2_x, kamenyka2_y, kamenyka2_width, kamenyka2_height))
            #pygame.draw.rect(win, (255, 0, 0), (kamenyka3_x, kamenyka3_y, kamenyka3_width, kamenyka3_height))

        #    pygame.draw.circle(win, (100, 100, 255), (XP_x, XP_y), 10)

            #pygame.draw.rect(win, (255, 0, 0), (turtle_x, turtle_y, turtle_width, turtle_height))

            #pygame.draw.rect(win, (0, 0, 255), (patron_x, patron_y, patron_width, patron_height))       

            up_coins = (int(coins) + schet)


            if schet > int(best_score_input):

                best_score_output = open("best_score.txt", "w")
                best_score_output.write(str(schet))
                best_score_output.close()



            save_score = open("last_score.txt", "w")
            save_score.write(str(schet))
            save_score.close()

            save_my_coins = open("My_Coin.txt", "w")
            save_my_coins.write(str(up_coins))
            save_my_coins.close()

        ###########################################################################################################################

            

            pygame.display.flip()
            pygame.display.update()
            clock.tick(35)
