import os


base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class Development(Config):
    DEBUG = True


class Testing(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


config_map = {
    "dev": Development,
    "test": Testing,
    "prod": Production,
}
