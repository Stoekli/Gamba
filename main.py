import json
import pygame as py
import numpy as np

odds = [0.7992, 0.1598, 0.032, 0.0064, 0.0026]
names = ["blue", "purple", "pink", "red", "gold"]

chosen_case = "Homeless case"

with open("cases.json", "r") as f:
    cases = json.load(f)


def gen_case():
    r = np.random.choice(names, 1, p=odds)[0]
    p: dict = cases["cases"][chosen_case][r]
    test = p.keys()
    d = np.random.choice(list(test), 1)[0]
    print(r + " " + d)

    return r, d

screen_width = 1200
screen_height =720

rec_width = screen_width/2
rec_height = screen_width/2

rec_pos_x = screen_width/2 - rec_width/2
rec_pos_y = screen_height/2 - rec_height/2

screen = py.display.set_mode((screen_width, screen_height))

running = True

py.display.set_caption('Gamba')

r, d = gen_case()

path = "C:\\Users\\perak\\PycharmProjects\\GambaCase\\images\\"

while running:


    imp = py.image.load(path + d + ".jpg").convert()
    imp = py.transform.scale(imp, (rec_width, rec_height))

    screen.blit(imp, (rec_pos_x, rec_pos_y))

    py.draw.rect(screen, py.Color(r), py.Rect(rec_pos_x - 10, rec_pos_y - 10, rec_width + 20, rec_height + 20), 10)

    for event in py.event.get():

        if event.type == py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                r, d = gen_case()
            if event.key == py.K_ESCAPE:
                running = False

    py.display.flip()
