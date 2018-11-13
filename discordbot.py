import discord # インストールした discord.py
import numpy as np
client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event

async def on_message(message):
    if message.content.startswith('/gobi'):
    	mem=[member.display_name for member in client.get_all_members()]
    	rand=np.random.randint(4)
    	rand2=np.random.randint(2)
    	if rand==0:
    		gobi='ごわす'
    	elif rand==1:
    		gobi='変更なし'
    	elif rand==2:
    		gobi='でんねんほっほーい'
    	else:
    		gobi='み'
    	reply = mem[rand2]+"あなたの語尾は"+gobi+"です"
    	await client.send_message(message.channel, reply)

    if message.content.startswith('/1ninsho'):
    	mem=[member.display_name for member in client.get_all_members()]
    	rand=np.random.randint(4)
    	rand2=np.random.randint(2)
    	if rand==0:
    		ninn='アチキ'
    	elif rand==1:
    		ninn='変更なし'
    	elif rand==2:
    		ninn='わし'
    	else:
    		ninn='ぼくちん'
    	reply = mem[rand2]+"あなたの一人称は"+ninn+"です"
    	await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTExNDk0NzM2OTEwMjIxMzM3.DsruVg.XdHqVVmeL4w6JApsjAOysps6Nqs')