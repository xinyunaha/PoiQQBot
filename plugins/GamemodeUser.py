import re
import time
import config
from helper.SQLiteHelper import Player
from websocket import create_connection
from nonebot import on_command, CommandSession, permission

__plugin_name__ = '修改游戏模式-user'
__plugin_usage__ = r"""修改游戏模式(仅群主及开发者可用)
例：#生存
或者#sur"""


@on_command('sur', aliases='生存', only_to_me=False, permission= permission.GROUP_MEMBER)
async def Bind(session: CommandSession):
    SenderQQNumber = session.ctx['user_id']  # 取发送者的qq号
    SenderGroupNumber = session.ctx['group_id']
    if str(SenderGroupNumber) not in config.SendGroup:
        pass
    else:
        # 联系数据库获取到玩家名称
        try:
            GamerName = Player('%s' % SenderQQNumber)  ##QQ取玩家ID
            if re.search('.*(\\\\n)',GamerName) or re.search('.*(\\n)',GamerName) or re.search('.*(\\r)',GamerName):
                await session.send('wdnmd,爪巴')
                return
            # 联系BedrockServer处理
            try:
                ws = create_connection("ws://127.0.0.1:30000")
            except:
                await session.send('[CQ:at,qq={0}] 服务器去火星了,等会儿再试试吧'.format(SenderQQNumber))
            ws.send('testfor \"%s\"' % GamerName)
            result = ws.recv()
            if result != 'No targets matched selector':
                ws.send(f'gamemode 0 \"{GamerName}\"')
                print("玩家%s -->生存" % GamerName)
                await session.send(f'[CQ:at,qq={SenderQQNumber}] 成功设置玩家{GamerName}为生存模式')
            else:
                await session.send('[CQ:at,qq={0}] 当前您不在线嗷,上线后再试试吧'.format(SenderQQNumber))
        except Player.PlayerNotFoundException:
            await session.send('[CQ:at,qq={0}]你没有绑定，请输入#bind 你的游戏ID，例：#addw username进行绑定'.format(SenderQQNumber))
