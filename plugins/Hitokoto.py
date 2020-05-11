import requests
import config
import json
from nonebot import on_command, CommandSession

__plugin_name__ = '一言'
__plugin_usage__ = r"""一言
例：#一言
或者 #yy"""


@on_command('yy', aliases='一言', only_to_me=False)
async def Bind(session: CommandSession):
    SenderQQNumber = session.ctx['user_id']
    SenderGroupNumber = session.ctx['group_id']
    if str(SenderGroupNumber) not in config.SendGroup:
        pass
    else:
        Return = requests.get('https://v1.hitokoto.cn/?c=a')
        Json = json.loads(Return.text)
        await session.send('[CQ:at,qq=%s]\n%s\nFrom:%s' % (SenderQQNumber, Json['hitokoto'], Json['from']))
