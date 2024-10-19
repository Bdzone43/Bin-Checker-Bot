from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23306415"))
    API_HASH = getenv("API_HASH", "fecb61dcfee0e426cf6ef96cc6f32cbc")
    BOT_TOKEN = getenv("BOT_TOKEN", "7351510273:AAGF6qx3Ac8Vkwyv_vB6zCC2WVfNNJI6kdA")

config = Config()
