import telebot
from datetime import datetime
from telebot import types
import requests


bot = telebot.TeleBot('SEU TOKEN')

# /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao bot oficial da FURIA para você que assim como nós é muito fã do nosso time de CS:GO!\nUse os comandos abaixo para conhecer melhor nossa história, redes e muito mais.\n\nDigite /comandos para ver tudo que você pode fazer aqui.")

# /comandos
@bot.message_handler(commands=['comandos'])
def list_commands(message):
    bot.send_message(message.chat.id, 
        "📋 Comandos disponíveis:\n"
        "/quem_somos – Conheça a história da FURIA\n"
        "/nossas_redes – Veja onde nos encontrar\n"
        "/elenco – Saiba mais sobre nossos times e atletas\n"
        "/titulos – Veja nossas conquistas\n"
        "/loja – Confira nossos produtos oficiais\n"
        "/contato – Entre em contato com a FURIA\n"
        "/ultimo_jogo - Veja a última partida da FURIA\n"
        "/palpite - Dê seu palpite sobre o jogo"
    )

# /quem_somos
@bot.message_handler(commands=['quem_somos'])
def quem_somos(message):
    bot.send_photo(message.chat.id, 
    "https://media.licdn.com/dms/image/v2/D4D05AQHYsfbUjstOjA/videocover-low/B4DZXeLbqxHICU-/0/1743189332682?e=2147483647&v=beta&t=EmdTXPcDpRDMLe33kUdHlSecPprYYf5g32c4CAdWAvE"
    )
    
    bot.send_message(message.chat.id, 
        "🔥 Somos a FURIA!\n"
        "Mais que uma organização de esports — somos o orgulho brasileiro.\n"
        "Nascemos no CS:GO, conquistamos o mundo e hoje carregamos propósito, cultura e paixão. 🖤\n"
        "De fã pra fã, viva essa jornada com a gente."
    )

# /nossas_redes
@bot.message_handler(commands=['nossas_redes'])
def redes_sociais(message):
    bot.send_message(message.chat.id, 
        "🌐 Nossas redes oficiais:\n"
        "Instagram: https://www.instagram.com/furiagg\n"
        "Twitter (X): https://x.com/FURIA\n"
        "YouTube: https://www.youtube.com/@FURIAF.C.\n"
        "Site oficial: https://www.furia.gg/"
    )

# /elenco
@bot.message_handler(commands=['elenco'])
def elenco(message):
    bot.send_photo(message.chat.id, 
        "https://pbs.twimg.com/media/GpOqgqaW4AAw2-v?format=jpg&name=large"
        )
    
    bot.send_message(message.chat.id, 
        "👥 Conheça nossos atletas:\n"
        "- Gabriel 'FalleN' Toledo (Brasil) – Capitão e AWPer\n"
        "- Kaike 'KSCERATO' Cerato (Brasil) – Rifler\n"
        "- Yuri 'yuurih' Santos (Brasil) – Rifler\n"
        "- Danil 'molodoy' Golubenko (Cazaquistão) – Rifler\n"
        "- Mareks 'YEKINDAR' Gaļinskis (Letônia) – Stand-in"
    )

# /titulos
@bot.message_handler(commands=['titulos'])
def titulos(message):
    bot.send_photo(message.chat.id, 
    "https://i.ytimg.com/vi/B6Y3_OzBtjg/maxresdefault.jpg"
    )
    bot.send_message(message.chat.id, 
        "🏆 Nossas conquistas no CS:GO:\n"
        "- IEM New York North America – 2020\n"
        "- ESL Pro League Season 12 North America – 2020\n"
        "- DreamHack Masters Spring North America – 2020\n"
        "- DreamHack Open Summer North America – 2020\n"
        "- Elisa Invitational Summer  – 2021\n"
        "- IEM Fall North America  – 2021\n"
        "- BGS Esports  – 2023"
    )

# /loja
@bot.message_handler(commands=['loja'])
def loja(message):
    bot.send_photo(message.chat.id, 
    "https://medias.itatiaia.com.br/dims4/default/1969751/2147483647/strip/true/crop/735x414+0+0/resize/1000x563!/quality/90/?url=https%3A%2F%2Fk2-prod-radio-itatiaia.s3.us-east-1.amazonaws.com%2Fbrightspot%2F08%2Fa1%2F18cd273f43429a383d59437d24e8%2Fadidas-x-furia-banner-apoio-3.jpg"
    )
    bot.send_message(message.chat.id, 
        "🔥FURIA x Adidas\n"
        "\n"         
        "A FURIA e a Adidas uniram forças para redefinir o estilo no universo dos esports.\n"
        "\n"         
        "🛒 Explore a Coleção Completa\n"
        "\n"         
        "Visite-nos para conferir toda a linha de produtos oficiais da FURIA, incluindo camisetas, moletons, jaquetas e acessórios. Cada peça é pensada para quem vive o jogo com intensidade e estilo FURIA.\n"
        "Não perca a chance de vestir a revolução. Junte-se à FURIA nessa jornada de estilo e performance.\n"
        "\n"         
        "Confira nossos produtos oficiais:\n"
        "https://www.furia.gg/produtos"
    )

# /contato
@bot.message_handler(commands=['contato'])
def contato(message):
    bot.send_photo(message.chat.id, 
    "https://yt3.googleusercontent.com/_QDHD8FYiV_Xhk4pdtzme9OOtbg6LMCOcSz3-Sv0AVUbSccWbtQJlIbk2sIEiBbQsIgwn64onQ=s900-c-k-c0x00ffffff-no-rj"
    )
    bot.send_message(message.chat.id, 
        "📩 Precisa falar com a gente?\n"
        "Envie um e-mail para: sac@furia.gg\n"
        "Ou entre em contato pelo nosso whatsapp: https://wa.me/5511993404466"
    )

# Função para obter os dados da última partida da FURIA no HLTV
def obter_ultima_partida_furia_json():
    try:
        url = "https://hltv-api.vercel.app/api/matches.json"
        response = requests.get(url)

        if response.status_code != 200:
            return "Erro ao acessar a API."

        dados = response.json()
        nome_time = "FURIA"

        # Procurar partidas que envolvem FURIA
        partidas_furia = []
        for partida in dados:
            teams = partida.get('teams', [])
            for team in teams:
                if team.get('name', '').upper() == nome_time:
                    partidas_furia.append(partida)
                    break  

        if not partidas_furia:
            return "Nenhuma partida da FURIA encontrada."

        ultima_partida = partidas_furia[0]

        # Extrair dados
        evento = ultima_partida.get('event', {}).get('name', 'Evento desconhecido')
        data_iso = ultima_partida.get('time', None)
        match_id = ultima_partida.get('matchId', None)

        # Formatar a data
        if data_iso:
            data = datetime.fromisoformat(data_iso.replace('Z', '')).strftime('%d/%m/%Y %H:%M')
        else:
            data = 'Data desconhecida'

        # Recupera os times
        team1, team2 = ultima_partida.get('teams', [])[0], ultima_partida.get('teams', [])[1]
        
        # Recupera os resultados numéricos
        team1_result = team1.get('result', 1)
        team2_result = team2.get('result', 2)

        # Determina o placar e o oponente com base na FURIA
        if team1.get('name', '').upper() == nome_time:
            oponente = team2.get('name', 'Oponente desconhecido')
            placar = f"{team1_result} - {team2_result}"
        else:
            oponente = team1.get('name', 'Oponente desconhecido')
            placar = f"{team2_result} - {team1_result}"

        return {
            "data": data,
            "evento": evento,
            "oponente": oponente,
            "resultado": placar
        }

    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
        return "Erro ao acessar os dados."

# /ultimo_jogo
@bot.message_handler(commands=['ultimo_jogo'])
def status_jogo(message):
    ultima_partida = obter_ultima_partida_furia_json()

    if isinstance(ultima_partida, dict):
        texto = (
            f"📊 Última Partida da FURIA\n"
            f"🏟 Evento: {ultima_partida['evento']}\n"
            f"🗓 Data: {ultima_partida['data']}\n"
            f"🎮 Contra: {ultima_partida['oponente']}\n"
            f"📈 Resultado: {ultima_partida['resultado']}"
        )
    else:
        texto = ultima_partida  

    bot.send_message(message.chat.id, texto)

# /palpite
@bot.message_handler(commands=['palpite'])
def status_interativo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔥", callback_data='reacao_fogo'),
        types.InlineKeyboardButton("😱", callback_data='reacao_susto'),
        types.InlineKeyboardButton("🖤", callback_data='reacao_coracao')
    )
    texto = "Vai ser uma partida emocionante! Qual seu palpite?"
    bot.send_message(message.chat.id, texto, reply_markup=markup)

# 🤖 Reações às jogadas
@bot.callback_query_handler(func=lambda call: call.data.startswith('reacao_'))
def reacoes(call):
    reacao = call.data.split('_')[1]
    respostas = {
        'fogo': "🔥 2 a 0 com direito a jogadas impressionantes!",
        'susto': "😱 2 a 1! Aquele jogo suado mas insano!",
        'coracao': "🖤 Isso é FURIA, pra cima deles!"
    }

    markup = types.InlineKeyboardMarkup()  # Cria um novo markup vazio
    texto = respostas[reacao]

    bot.answer_callback_query(call.id)
    bot.edit_message_text(texto, chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)


# Iniciar o bot
if __name__ == "__main__":
    bot.polling()
