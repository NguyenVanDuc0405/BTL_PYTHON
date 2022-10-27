import pygame

class Button:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = img
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isClicked = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked == False:
                self.isClicked = True

        # pygame.draw.rect(screen, (255,0,0), self.rect, 2)
        
        screen.blit(self.img, (self.x, self.y))