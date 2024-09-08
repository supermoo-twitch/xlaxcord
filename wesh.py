wesh="WESH CHANME C'EST XLAPS" 
print(wesh)
import discord
from discord.ext import commands
import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
XLAXIEN = os.getenv('XLAXIEN')
# Remplacez 'USER_ID_SPECIFIQUE' par l'ID de l'utilisateur auquel vous souhaitez que le bot réponde
USER_ID_SPECIFIQUE = "1280421470987878410"
USER_DYNO = "1282242159080243286" # Exemple : "123456789012345678"
mymessage=[]
mymessage.append({"role": "system","content": XLAXIEN})
intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f'Wesh c est {bot.user}')

@bot.event
async def on_message(message):
    print("in new message")
    print(str(message.author.id))
    if message.author == bot.user:
        return
    
    # Vérifier si l'auteur du message n'est pas Xlax XLAXON
    if str(message.author.id) != USER_ID_SPECIFIQUE and str(message.author.id) != USER_DYNO:
        try:
                prompt = message.content.strip()
                print(f"Prompt: {prompt}")
                mymessage.append({"role": "user","content": prompt})
                print("j'ai envie d'aller o chiotte, signe Jacquo")
                response = openai.chat.completions.create(
                    messages=mymessage,
                    model="gpt-4o"
                )
                print(response.choices[0].message.content)
                reply = response.choices[0].message.content.strip()
                # lui demander de poster en moins de 2000 caractere puis ecrire la suite puis la suite etc; dans plusieurs messages
                # Diviser le texte en segments de 2000 caractères ou moins
                mymessage.append({"role": "assistant","content": reply})
                if len(reply) > 2000:
                    for i in range(0, len(reply), 2000):
                        await message.channel.send(reply[i:i+2000])
                else:
                    await message.channel.send(reply)
        except Exception as e:
            await message.channel.send("Wesh ! C'est Xlaps, y'a eu un bugch réessaye plus tard gro !")
            print("waaaaaaaaaillle")


# Ne pas oublier de traiter les commandes normalement
    await bot.process_commands(message)
print("wesh c'est Jacquo y'a un truc qui me gratte ")
bot.run(DISCORD_TOKEN)
