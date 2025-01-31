from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class SaveFolder:
    path: str


@dataclass
class Config:
    tg_bot: TgBot
    folder: SaveFolder


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    bot_token = env("BOT_TOKEN")
    folder_path = env("FOLDER_PATH")

    return Config(TgBot(token=bot_token), SaveFolder(path=folder_path))
