import telebot
from telebot import types


bot = telebot.TeleBot('8088561421:AAETwlXktS1mu-iG24GwivP6s5fM97ud_KA')

#Menu inicial
@bot.message_handler(['start'])
def start(msg:telebot.types.Message):
    markup = types.InlineKeyboardMarkup()

    botao_esc = types.InlineKeyboardButton('Escalação', callback_data='botao_esc')
    botao_hist = types.InlineKeyboardButton('Histórico', callback_data='botao_hist')
    botao_redes = types.InlineKeyboardButton('Redes sociais', callback_data='botao_redes')
    botao_jogos = types.InlineKeyboardButton('Próximos Jogos', callback_data='botao_jogos')

    markup.add(botao_jogos, botao_hist, botao_esc, botao_redes)

    bot.send_message(msg.chat.id, 'Bem vindo(a) a central de informações da Furia CS! \n Qual informação deseja?', reply_markup=markup)

#Retorno das funções



@bot.callback_query_handler()
def resp(call:types.CallbackQuery):
    match call.data:
        case 'botao_jogos':
            bot.send_message(call.message.chat.id, 'Os próximos desafios da Equipe da Furia são: \n PGL Astana 2025 - Entre 10/05 a 18/05 \n  IEM Dallas 2025 - Entre 19/05 a 25/05' \
            '\n BLAST.tv Austin Major 2025 - Entre 03/06 a 22/06 ')

        case 'botao_hist':
            bot.send_message(call.message.chat.id,'Os ultimos  resultados da Furia são: \n 0x2 vs The Mongolz pela PGL Bucharest 2025 \n 0x2 vs Virtus.pro pela PGL Bucharest 2025' \
            '\n 1x2 vs Complexity pela PGL Bucharest 2025')

        case 'botao_esc':
            bot.send_message(call.message.chat.id, 'A escalação da Furia hoje é:\n Yuri "yuurih" Boian  \n Kaike "KSCERATO" Cerato \n Gabriel "FalleN " Toledo(C) \n Danil "molodoy" Golubenko' \
            '\n Mareks "YEKINDAR" Gaļinskis \n Coach: Sidnei "sidde" Macedo ')

        case 'botao_redes':
            bot.send_message(call.message.chat.id, 'Siga a Furia nas redes Sociais: \n Twitter/X: https://x.com/FURIA \n Instagram: https://www.instagram.com/furiagg/' \
            '\n  TikTok: https://www.tiktok.com/@furiagg \n Linkedin: https://www.linkedin.com/company/furiagg/posts/?feedView=all' \
            '\n Também acesse o site da Furia em furia.gg')


bot.infinity_polling()