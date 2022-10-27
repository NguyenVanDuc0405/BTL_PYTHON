import pygame
import controller.img as IMAGE

SOUND_BUTTON = IMAGE.SOUND_BUTTON()
MUTE_BUTTON = IMAGE.MUTE_BUTTON()

class soundButton:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = img
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isClicked = False
        self.mute = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked == False:
                self.isClicked = True
                if self.mute == False:
                    self.mute = True
                    self.img = MUTE_BUTTON
                    pygame.mixer.music.stop()
                else:
                    self.mute = False
                    self.img = SOUND_BUTTON
                    pygame.mixer.music.play(-1)

        if pygame.mouse.get_pressed()[0] == 0:
            self.isClicked = False
        # pygame.draw.rect(screen, (255,0,0), self.rect, 2)
        
        screen.blit(self.img, (self.x, self.y))