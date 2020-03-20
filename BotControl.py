import logging
from os import path

import nonebot

import config

if __name__ == '__main__':
    # init logging
    logger = logging.getLogger()
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(message)s')
    streamHandler.setFormatter(formatter)

    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run()