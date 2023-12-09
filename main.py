import discord
from discord.ext import commands

intents = discord.Intents.all()  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='iklimdegisikligi')
async def iklim_degisikligi(ctx):
    response = """
    **İklim Değişikliği: Nedenler, Sebepler ve Önleme Yöntemleri**

    **Nedenler ve Sebepler:**
    1. Fosil Yakıtların Kullanımı: Kömür, petrol ve doğalgaz gibi fosil yakıtların yanması sera gazlarını arttırır.
    2. Orman Tahribatı: Ormanların kesilmesi ve yangınlar, atmosferdeki karbon miktarını artırır.
    3. Endüstriyel Faaliyetler: Sanayi tesislerinden salınan gazlar iklim değişikliğine katkıda bulunur.
    4. Tarım Uygulamaları: Tarım faaliyetleri metan ve azot oksit gibi gazların salınımına neden olabilir.

    Bu bilgiler genel bir bakış sunmaktadır. Daha fazla detay için bilimsel kaynaklara başvurun.
    """
    await ctx.send(response)
@bot.command(name='iklimdegisikligionle')
async def iklim_degisikligi_onle(ctx):  
    response = """
    **İklim Değişikliği: Önleme Yöntemleri**

    **Önleme Yöntemleri:**
    1. Yenilenebilir Enerji Kullanımı: Güneş, rüzgar, hidroelektrik gibi temiz enerji kaynaklarını teşvik edin.
    2. Orman Koruma ve Ağaçlandırma: Ormanları koruyun ve yeni ağaçlandırma projelerine destek verin.
    3. Enerji Verimliliği: Enerji tüketimini azaltan teknolojilere yatırım yapın.
    4. Sürdürülebilir Tarım: Çevre dostu tarım uygulamalarını teşvik edin.

    Bu bilgiler genel bir bakış sunmaktadır. Daha fazla detay için bilimsel kaynaklara başvurun.
    """

    await ctx.send(response)


bot.run("Your_Token")


