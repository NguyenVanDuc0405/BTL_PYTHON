import pygame


def setIconApp():
    pygame.display.set_icon(pygame.image.load('./img/background/iconApp.png'))


def BACKGROUND():
    BGIMG = pygame.image.load('./img/background.png')
    BGIMG = pygame.transform.scale(BGIMG, (400, 700))
    return BGIMG    

def ONE_PLAYER():
    ONE_PLAYER = pygame.image.load('./img/button/1player.png')
    ONE_PLAYER = pygame.transform.scale(ONE_PLAYER, (150, 145))
    return ONE_PLAYER


def TWO_PLAYER():
    TWO_PLAYER = pygame.image.load('./img/button/2player.png')
    TWO_PLAYER = pygame.transform.scale(TWO_PLAYER, (120, 65))
    return TWO_PLAYER
#Background trước khi vào game
def POSTER():
    BGIMG = pygame.image.load('./img/background/background.jpg')
    BGIMG = pygame.transform.scale(BGIMG, (400, 700))
    return BGIMG


def PLAY_BUTTON():
    PLAY_BUTTON = pygame.image.load('./img/button/play.png')
    PLAY_BUTTON = pygame.transform.scale(PLAY_BUTTON, (180, 90))
    return PLAY_BUTTON

def HELP_BUTTON():
    HELP_BUTTON = pygame.image.load('./img/help/information.png')
    HELP_BUTTON = pygame.transform.scale(HELP_BUTTON, (60, 60))
    return HELP_BUTTON

def SOUND_BUTTON():
    SOUND_BUTTON = pygame.image.load('./img/help/sound.png')
    SOUND_BUTTON = pygame.transform.scale(SOUND_BUTTON, (60, 60))
    return SOUND_BUTTON

def MUTE_BUTTON():
    MUTE_BUTTON = pygame.image.load('./img/help/mute.jpg')
    MUTE_BUTTON = pygame.transform.scale(MUTE_BUTTON, (60, 60))
    return MUTE_BUTTON    

def RETURN_BUTTON():
    RETURN_BUTTON = pygame.image.load('./img/help/close.png')
    RETURN_BUTTON = pygame.transform.scale(RETURN_BUTTON, (40, 40))
    return RETURN_BUTTON


def RELOAD_BUTTON():
    RELOAD_BUTTON = pygame.image.load('./img/button/reload.png')
    RELOAD_BUTTON = pygame.transform.scale(RELOAD_BUTTON, (100, 100))
    return RELOAD_BUTTON

def BACK_BUTTON():
    BACK_BUTTON = pygame.image.load('./img/button/back.png')
    BACK_BUTTON = pygame.transform.scale(BACK_BUTTON, (100, 100))
    return BACK_BUTTON

def INSTRUCTION():
    INSTRUCTION = pygame.image.load('./img/help/instruction.png')
    INSTRUCTION = pygame.transform.scale(INSTRUCTION, (600, 600))
    return INSTRUCTION


def LEFT_BUTTON():
    LEFT_BUTTON = pygame.image.load('./img/button/left.png')
    LEFT_BUTTON = pygame.transform.scale(LEFT_BUTTON, (70, 70))
    return LEFT_BUTTON


def RIGHT_BUTTON():
    RIGHT_BUTTON = pygame.image.load('./img/button/right.png')
    RIGHT_BUTTON = pygame.transform.scale(RIGHT_BUTTON, (70, 70))
    return RIGHT_BUTTON


def FRAMES():
    FRAMES = pygame.image.load('./img/khung.png')
    FRAMES = pygame.transform.scale(FRAMES, (250, 300))
    return FRAMES


def GAME_OVER():
    GAME_OVER = pygame.image.load('./img/background/gameover.png')
    GAME_OVER = pygame.transform.scale(GAME_OVER, (350, 200))
    return GAME_OVER

def CHOOSE_CAR():
    CHOOSE_CAR = pygame.image.load('./img/button/chooseCar.png')
    CHOOSE_CAR = pygame.transform.scale(CHOOSE_CAR, (45, 70))
    return CHOOSE_CAR



class obstacle():
    def redCar():
        RED_CAR = pygame.image.load('img/obstacle/obstacleCarRed.png')
        RED_CAR = pygame.transform.scale(RED_CAR, (40, 60))
        return RED_CAR

    def whiteCar():
        WHITE_CAR = pygame.image.load('img/obstacle/obstacleCarWhite.png')
        WHITE_CAR = pygame.transform.scale(WHITE_CAR, (40, 60))
        return WHITE_CAR

    def blueCar():
        BLUE_CAR = pygame.image.load('img/obstacle/obstacleCarBlue.png')
        BLUE_CAR = pygame.transform.scale(BLUE_CAR, (40, 60))
        return BLUE_CAR

    def greenCar():
        BLUE_CAR = pygame.image.load('img/obstacle/obstacleCarGreen.png')
        BLUE_CAR = pygame.transform.scale(BLUE_CAR, (40, 60))
        return BLUE_CAR


class carUser():
    def car_1(x,y):
        CAR = pygame.image.load('img/car/1.png')
        CAR = pygame.transform.scale(CAR, (x, y))
        return CAR

    def car_2(x,y):
        CAR = pygame.image.load('img/car/2.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR

    def car_3(x,y):
        CAR = pygame.image.load('img/car/3.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR

    def car_4(x,y):
        CAR = pygame.image.load('img/car/4.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR


    def car_5(x,y):
        CAR = pygame.image.load('img/car/5.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR


    def car_6(x,y):
        CAR = pygame.image.load('img/car/6.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR

    def car_7(x,y):
        CAR = pygame.image.load('img/car/7.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR

    def car_8(x,y):
        CAR = pygame.image.load('img/car/8.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR



    def car_9(x,y):
        CAR = pygame.image.load('img/car/9.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR



    def car_10(x,y):
        CAR = pygame.image.load('img/car/10.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR



    def car_11(x,y):
        CAR = pygame.image.load('img/car/11.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR



    def car_12(x,y):
        CAR = pygame.image.load('img/car/12.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR


    def car_13(x,y):
        CAR = pygame.image.load('img/car/13.png')
        CAR = pygame.transform.scale(CAR, (x,y))
        return CAR


