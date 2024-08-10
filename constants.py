from pygame import *

init()
font.init()
mixer.init()

CONSTANT_W, CONSTANT_H = 800, 700

window = display.set_mode((CONSTANT_W, CONSTANT_H))
display.set_caption("RELIZNA GRA")

background_menu = transform.scale(image.load("../images/backgrounds/background.png"), (CONSTANT_W, CONSTANT_H))

button = "../images/ui/button.png"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = time.Clock()

FPS = 60

VOLUME_MUSIC_POWER = 0.5
VOLUME_SOUND_POWER = 0.5

CURRENT_LANG = "ukr"

class BaseSprite(sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = None
        self.rect = None

    def set_image(self, img, w, h, x, y):

        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, window):

        window.blit(self.image, (self.rect.x, self.rect.y))

global_localization = {

    "button_start": {
        "eng": ["Start", 25, 15, 25],
        "ukr": ["Старт", 25, 15, 25],
        "ru": ["Старт", 25, 15, 25]
    },
    "button_settings": {
        "eng": ["Settings", 25, 15, 22],
        "ukr": ["Налаштування", 25, 15, 22],
        "ru": ["Настройки", 25, 15, 22]
    },
    "button_exit": {
        "eng": ["Exit", 25, 15, 22],
        "ukr": ["Вихід", 25, 15, 22],
        "ru": ["Выход", 25, 15, 22]
    },
    "button_off": {
        "eng": ["off", 25, 15, 22],
        "ukr": ["вимк.", 25, 15, 22],
        "ru": ["выкл.", 25, 15, 22]
    },
    "button_on": {
        "eng": ["on", 25, 15, 22],
        "ukr": ["ввім.", 25, 15, 22],
        "ru": ["вкл.", 25, 15, 22]
    }
}

