import discord
import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count: int = 100):
    await ctx.send("he" * count)

# @bot.command()
# async def mem(ctx):
#     #NOTA: AL COMPILAR DEBE ESTAR EN LA MISMA CARPETA QUE EL ARCHIVO .py, click derecho abrir en terminal
#     with open('Images/mem1.jpeg', 'rb') as f:
#         # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
#         picture = discord.File(f)
#     # A continuación, podemos enviar este archivo como parámetro.
#     await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    # Obtenemos la lista de archivos dentro de la carpeta Images
    images = os.listdir('Images')
    # Elegimos un archivo al azar
    img_name = random.choice(images)
    # Abrimos la imagen seleccionada
    with open(f'Images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    # Enviamos la imagen al canal
    await ctx.send(file=picture)

# def get_duck_image_url():    
#     url = 'https://random-d.uk/api/random' 
#     res = requests.get(url) 
#     data = res.json() 
#     return data['url'] 

# @bot.command('duck')
# async def duck(ctx):
#     '''
#     Cuando alguien escribe $duck en Discord:
#     1. Se ejecuta este comando
#     2. Se llama a la función get_duck_image_url
#     '''
#     image_url = get_duck_image_url() 
#     await ctx.send(image_url)
manualidad1 = "Portalápices con lata o botella   Materiales: lata o botella de plástico, tijeras, papel, pegamento.   Pasos:  Lava y seca la lata o botella.  Si es botella, córtala a la altura deseada.  Decórala con papel, colores o recortes.  Deja secar y úsala para lápices."
manualidad2 = "Maceta con botella de plástico     Materiales: botella, tijeras, clavo o lápiz, tierra, planta.  Pasos:   1 Corta la botella por la mitad.   2  Haz pequeños agujeros abajo para el agua.    3  Agrega tierra y planta la flor.   4  Riega un poco."
manualidad3 = "Maceta con llanta reciclada  Materiales:  Llanta vieja,   Pintura,   Tierra,    Planta o flores,    Cómo se hace:  1  Lava la llanta.   2    Píntala y deja secar.    3   Colócala en el suelo.     4   Llénala con tierra y planta flores."
manualidades = [manualidad1, manualidad2, manualidad3]
@bot.command()
async def manu(ctx):
    manu_aleatoria = random.choice(manualidades)
    await ctx.send(manu_aleatoria)
bot.run("MTQ1NzA1MzYzMjQ1NjU1NjU1Ng.Gr1Z-N.tTa8mVkduGfyVSmRoIHGX1hQxuTOyGi1YCa20k")
