import pygame
import sys
import pygame.freetype
import os
import cv2
import numpy as np


def process_image(file_path):
    image = cv2.imread(file_path)
    fill_image = np.zeros([1280, 1100, 3])
    fill_image.dtype = np.float64
    x = int((fill_image.shape[0] - image.shape[0]) / 2)
    y = int((fill_image.shape[1] - image.shape[1]) / 2)
    print(x, y)
    fill_image[x:x + image.shape[0], y:y + image.shape[1], :] = image[:, :, :]
    # cv2.imshow('a',fill_image)
    # cv2.waitKey(0)
    cv2.imwrite(file_path, fill_image)


class EnglishBigin:
    def __init__(self):
        pygame.init()
        self.image_list = None
        self.answer = None
        self.i = 0
        self.show_answer = False
        self.fclock = pygame.time.Clock()
        self.screen = self.__init_screen()
        self.loads()
        self.__draw_background()

    def loads(self):
        image_list = os.listdir('images')
        image_list = ['images/' + str(item) + '.png' for item in range(1, len(image_list) + 1)]
        with open('answer.txt', 'r') as f:
            answer = f.readlines()
        answer = [item[:-1] for item in answer]
        self.image_list = image_list
        self.answer = answer

    # create a screen and set the size of it
    def __init_screen(self):
        # set the size of the screen
        size = 1000, 1280
        # set the color of the background
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        # set the total of the screen
        pygame.display.set_caption('EnglishBigin')
        return screen

    def __draw_background(self):
        background = pygame.image.load(self.image_list[self.i])
        background_rect = background.get_rect()
        self.screen.blit(background, background_rect)

    def __draw_answer(self):
        font = pygame.font.Font('GB2312.ttf', 40)
        text_surface_obj = font.render(self.answer[self.i], True, (255, 255, 255), (0, 0, 0))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (500, 150)
        self.screen.blit(text_surface_obj, text_rect_obj)

    def __draw_index(self):
        font = pygame.font.Font('GB2312.ttf', 20)
        text_surface_obj = font.render(str(self.i + 1), True, (255, 255, 255), (0, 0, 0))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (50, 50)
        self.screen.blit(text_surface_obj, text_rect_obj)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.show_answer == False:
                            self.show_answer = True
                        else:
                            self.show_answer = False
                    elif event.key == pygame.K_RIGHT:
                        self.show_answer = False
                        if self.i < len(self.image_list) - 1:
                            self.i += 1
                    elif event.key == pygame.K_LEFT:
                        self.show_answer = False
                        if self.i > 0:
                            self.i -= 1
            self.__draw_background()
            if self.show_answer is True:
                self.__draw_answer()
            self.__draw_index()
            pygame.display.update()
            self.fclock.tick(300)


if __name__ == '__main__':
    post_man = EnglishBigin()
    post_man.main()
    # post_man.main()
    # post_man.__mode1()
    # a = os.listdir('images')
    # for item in a:
    #     print(item)
    #     process_image('images/' + item)
    # process_image('images/33.png')
    # process_image('images/34.png')
