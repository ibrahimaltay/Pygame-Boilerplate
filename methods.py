import json
import pygame

def GetColors():
    COLORS = {
        "White": (255, 255, 255),
        "Black": (0, 0, 0)
    }
    return COLORS

def GetConfiguration():
    with open("config.json") as file:
        config = json.load(file)
        return config

#
# def PrintText(text):
#     pygame.font.init()
#     font = pygame.font.SysFont("ROBOTO", int(config["FONT_SIZE"]))
#     textsurface = font.render(text, True, colors["Black"])
#     text_rect = textsurface.get_rect(center=(200,200))
#     win.blit(textsurface, (text_rect))

