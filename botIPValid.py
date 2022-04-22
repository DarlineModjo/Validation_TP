from discord.ext import commands

from shodan import Shodan

TOKEN = 'OTY2OTc5ODkwOTM3MjIxMTQx.YmJoMw.34YNAvntbzRaQWVbsuhTj2X_VDs'
SHODAN_API_KEY = '7TpTAnFpX18i4OFquJ2ZMSNA2uuyKbkf'

bot = commands.Bot(command_prefix='!')

shodan_api = Shodan(SHODAN_API_KEY)

@bot.command(name='range', help='count valid ip')
async def count(ctx, ip_start, nb):
    ip = ip_start.split(".")

    _count = 0
    for i in range(int(ip_start.split(".")[-1]), int(nb)+1):
        ip[-1] = str(i)
        ".".join(ip)
        print(ip)
        try:
            res = shodan_api.host(ip)
            _count += 1
        except Exception as e:
            print(e)

    response = '%d Valid Adress' % _count
    await ctx.send(response)

bot.run(TOKEN)