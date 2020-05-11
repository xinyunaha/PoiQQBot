if not SenderGamerName:
    #     await session.send('[CQ:at,qq={0}]#rmw后面必须跟上游戏ID嗷，例：#addw HelloWorld'.format(SenderQQNumber))
    # else:
    #     try:
    #         ws = create_connection("ws://127.0.0.1:30000")
    #     except:
    #         await session.send('[CQ:at,qq={0}] 服务器去火星了,等会儿再试试吧'.format(SenderQQNumber))
    #     ws.send(f'whitelist add \"{SenderGamerName}\"')
    #     time.sleep(0.3)
    #     result = ws.recv()
    #     if result == 'Success':
    #         result == ws.recv()
    #     print(result)
    #     time.sleep(0.2)
    #     if result == "Player added to whitelist":
    #         await session.send('[CQ:at,qq=%s] 已经把%s添加到Poicraft的白名单中了呢!' % (SenderQQNumber, SenderGamerName))
    #     elif result == 'Player already in whitelist':
    #         await session.send('[CQ:at,qq=%s] %s已经在Poicraft的白名单中了呢!' % (SenderQQNumber, SenderGamerName))
    #     else:
    #         await session.send('[CQ:at,qq=%s] 出了点问题?试试提个issues???' % SenderQQNumber)