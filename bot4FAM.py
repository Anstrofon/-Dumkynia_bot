import os
import re
import random
import shelve
from local import getto

from copypasta import copypastas 
from googletrans import Translator
import bs4
import requests
import telebot
import wikipedia
from yt_dlp import YoutubeDL
from pyowm import OWM
from telebot import types

from genMemes import memes

bot = telebot.TeleBot('5672240426:AAEDnV3H5lWrYCkh6Ss7UNGblSQxefPt5vI')



'''    
    докуметація до коду в файлі README.md 
'''

@bot.message_handler(commands=['start'])
def start(message):
    greetings = f'True Turuu, {message.from_user.first_name}'
    
    #inline keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Останнє завантажене відео', callback_data= 'vid' )
    item2 = types.InlineKeyboardButton('Історія пошуку п\'ятьох сайтів', callback_data='siteres' )
    next_bottom = types.InlineKeyboardButton('Настууупне ->', callback_data= 'next1' )
    markup.add(item1, item2, next_bottom)

    bot.send_message(message.chat.id, greetings, reply_markup= markup)

@bot.message_handler(commands=['vid'])
def reading_messages(message):
    global pathname
    pathname = 'vidYT'
    task = message.text.split(maxsplit=1)[1]
    print(task)
    if task.startswith('https://www.youtube.com/watch') or task.startswith('https://youtu.be/'):
        saved_vid = []
        os.chdir(os.getcwd() + '\\' + pathname)
        bot.send_message(message.chat.id, 'Починаю завантаження')
        try:
            URLS = task
            with YoutubeDL() as ydl:
                ydl.download(URLS)               
        except:
            bot.send_message(message.chat.id, 'Відбулася помилка')
        
        if task.startswith('https://www.youtube.com/watch?v='):
            ch = re.compile(r'v=(.*)')
            ma = ch.search(task)
            name_vid = ma.group().strip('v=')  # працює 
            
            saved_vid.append(str(name_vid))
        elif task.startswith('https://youtu.be/'):
            ch = re.compile(r'e/(.*)')
            ma = ch.search(task)
            name_vid = ma.group().strip('e/')

            saved_vid.append(str(name_vid))
        os.chdir(os.path.abspath('..\\'))
        global shelfFile
        shelfFile = shelve.open(f'{message.chat.id}')
        shelfFile['name'] = saved_vid
        shelfFile.close()
    shelfFile = shelve.open(f'{message.chat.id}')
    shelfFile.close()

@bot.message_handler(commands=['search'])
def search(message):
    task = message.text.split('/search')[1:]
    if task[0] == '':
        bot.send_message(message.chat.id, 'А що збираєшься шукати, га?')
    else:
        bot.send_message(message.chat.id, 'Починаю гуглити...')
        params = {"q": " "}  # add "hl":"en" to get english results
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }
        res = requests.get('http://www.google.com/search?q=' + ''.join(task[0]), params=params, headers=headers)
        print(res.status_code == requests.codes.ok)

        # Знаходження перших знайденних лінков
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        print(soup.prettify())
        # Відкриття окремих вкладків для кожного з результатів.
        linkElems = soup.select('a:has(h3)')
        numOpen = min(5, len(linkElems))
        shelfFile = shelve.open(f'{message.chat.id}')
        list_sites = []
        for i in range(numOpen):
            ba = linkElems[i].get('href')
            list_sites.append(ba)
            bot.send_message(message.chat.id, f'{ba}')
        shelfFile['sites'] = list_sites
        shelfFile.close()

#inline mode moment
@bot.callback_query_handler(func=lambda call: True)
def inline_func(call):
    if call.data == 'vid':
        bot.send_message(call.message.chat.id, 'Щоб завантажити нове відео, просто кинь джерело у чат, а зараз, я пошукаю останній відос')
        shelfFile = shelve.open(f'{call.message.chat.id}')
        
        print(list(shelfFile.keys()))
        print(list(shelfFile.values()))
        if 'name' not in list(shelfFile.keys()):
            bot.send_message(call.message.chat.id, 'Йой, з чого чату ніхто ще не завантажував відос. /vid [ютуб-джерело]')
            shelfFile.close()
        else:
            global markvid
            markvid = types.InlineKeyboardMarkup(row_width=2)
            vidnam = types.InlineKeyboardButton('{0}'.format(shelfFile['name'][-1]), callback_data= 'last_vid')
            markvid.add(vidnam)
            bot.send_message(call.message.chat.id, 'Осьо знайшла: ', reply_markup=markvid)
            pass
    
    if call.data == 'last_vid':
        pathname = 'vidYT'
        bot.send_message(call.message.chat.id, 'на')
        shelfFile = shelve.open(f'{call.message.chat.id}')
        print(shelfFile['name'][-1])
        for foldernme, subfolders, filenams in os.walk(pathname):
            for filename in filenams:
                print(filename)
                if filename.endswith('[{0}].mp4'.format(shelfFile['name'][-1])):
                    print(filename)
                    os.chdir(os.getcwd() + '\\' + pathname)
                    last_vid = open(filename, 'rb')
                    bot.send_video(call.message.chat.id, last_vid)
                    os.chdir(os.path.abspath('..\\'))
                else:
                    print('Не знайдено того відосу')
    
    if call.data == 'siteres':
        shelfFile = shelve.open(f'{call.message.chat.id}')
        if 'sites' not in list(shelfFile.keys()) == []:
            bot.send_message(call.message.chat.id, 'Йоой, ніхто в цьому чаті не користувався /search')
            shelfFile.close()
        else:
            for i in range(0, 5):
                bot.send_message(call.message.chat.id, shelfFile['sites'][-i])
            
    
    if call.data == 'next1':
        marknext = types.InlineKeyboardMarkup(row_width=2)
        item3 = types.InlineKeyboardButton('Дізнатись погоду в Дніпрі', callback_data='weather')
        item4 = types.InlineKeyboardButton('Як ти знайдеш локацію?', callback_data='local')
        next_bottom2 = types.InlineKeyboardButton('Настууупне ->', callback_data= 'next2' )
        marknext.add(item3, item4, next_bottom2)
        bot.send_message(call.message.chat.id, 'наступна сторінка:', reply_markup=marknext)
    
    if call.data == 'weather':
        owm = OWM('6cc68996da524266d0f52587b3f60b1d')
        mgr = owm.weather_manager()
        
        observation = mgr.weather_at_place('Dnipro')
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        feel_like = w.temperature('celsius')['feels_like']
        bot.send_message(call.message.chat.id, f'Температура в Дніпрі зараз {temp}°C. Відчувається як: {feel_like}°C')

    if call.data == 'local':
        bot.send_message(call.message.chat.id, 'Щоб отримати локаці пропиши /getlocal [місце]')

    if call.data == 'next2':
        marknext2 = types.InlineKeyboardMarkup(row_width=2)
        item5 = types.InlineKeyboardButton('Як отримати означення з вікіпедії?', callback_data='wiki')
        item6 = types.InlineKeyboardButton('Гра Камінь Ножниці Бумага', callback_data='game')
        next_bottom2 = types.InlineKeyboardButton('Настууупне ->', callback_data= 'next3' )
        marknext2.add(item5, item6, next_bottom2)
        bot.send_message(call.message.chat.id, 'ооо, ще сторінкаа..', reply_markup= marknext2)

    if call.data == 'wiki':
        bot.send_message(call.message.chat.id, 'Введи /wiki [твої збоченські запити] і я вілправлю те, що доступно в енциклопедії. Ну й звичайно це українська вікі')

    if call.data == 'game':
        games = types.InlineKeyboardMarkup(row_width=2)
        rock = types.InlineKeyboardButton('Камінь', callback_data='rock')
        noj = types.InlineKeyboardButton('Ножниці', callback_data='noj')
        paper = types.InlineKeyboardButton('Бумага', callback_data= 'paper' )
        games.add(rock, noj, paper)
        bot.send_message(call.message.chat.id, 'Ну поїхали, чічі-ко:', reply_markup=games)

    if call.data == 'rock':
        choics = ['камінь', "ножниці", "папір"]
        botchoice = random.choice(choics)
        print(botchoice)
        if botchoice == 'камінь':
            bot.send_message(call.message.chat.id, 'Нічия..')
        if botchoice == 'ножниці':
            bot.send_message(call.message.chat.id, f'лляяяя, програла тобі {call.message.from_user.first_name}')
        if botchoice == 'папір':
            bot.send_message(call.message.chat.id, f'Хаха, сасі бака {call.message.from_user.first_name}, у мене був {botchoice}')

    if call.data == 'noj':
        choics = ['камінь', "ножниці", "папір"]
        botchoice = random.choice(choics)
        print(botchoice)
        if botchoice == 'камінь':
            bot.send_message(call.message.chat.id, f'Хаха, сасі бака {call.message.from_user.first_name}, у мене був {botchoice}')
        if botchoice == 'ножниці':
            bot.send_message(call.message.chat.id, 'Нічия..')
        if botchoice == 'папір':
            bot.send_message(call.message.chat.id, f'лляяяя, програла тобі {call.message.from_user.first_name}')
    if call.data == 'paper':
        choics = ['камінь', "ножниці", "папір"]
        botchoice = random.choice(choics)
        print(botchoice)
        if botchoice == 'камінь':
            bot.send_message(call.message.chat.id, f'лляяяя, програла тобі')
        if botchoice == 'ножниці':
            bot.send_message(call.message.chat.id, f'Хаха, сасі бака, у мене був {botchoice}')
        if botchoice == 'папір':
            bot.send_message(call.message.chat.id, 'Нічия..')

    if call.data == 'next3':
        marknext3 = types.InlineKeyboardMarkup(row_width=2)
        item7 = types.InlineKeyboardButton('Вивчаємо http-коди разом з котиками', callback_data='http')
        item8 = types.InlineKeyboardButton('Йди з звідси!', callback_data='leave')
        next_bottom3 = types.InlineKeyboardButton('Настууупне ->', callback_data= 'next4' )
        marknext3.add(item7, item8, next_bottom3)
        bot.send_message(call.message.chat.id, 'ось щеееееееее', reply_markup=marknext3)
    
    if call.data == 'http':
        re = requests.get(f'https://http.cat/{random.randint(400, 425)}.jpg')
        playfile = open('random.jpg', 'wb')
        for chunk in re.iter_content(100000):
            playfile.write(chunk)
        playfile.close
        fot = open('random.jpg', 'rb')
        bot.send_photo(call.message.chat.id, fot)
    
    if call.data == 'leave':
        if call.message.chat.type == 'private':
            bot.send_message(call.message.chat.id, 'А куди? Ти сам проведеш за ручкою мене до виходу? Це не чат-група. Сам йди')
        else:
            bot.send_message(call.message.chat.id, 'Ну, ок(((')
            bot.leave_chat(call.message.chat.id)

    if call.data == 'next4':
        marknext4 = types.InlineKeyboardMarkup(row_width=2)
        item9 = types.InlineKeyboardButton('Отримати контакт', callback_data='contact')
        item10 = types.InlineKeyboardButton('Швидкий переклад з англ. на укр', callback_data='translate')
        marknext4.add(item9, item10)
        bot.send_message(call.message.chat.id, 'о', reply_markup=marknext4)

    if call.data == 'contact':
        bot.send_message(call.message.chat.id, '/contact { номер } { нейм } та спробувати відразу позвонити типу (якщо той є в телеграмі)')
    
    if call.data == 'translate':
        bot.send_message(call.message.chat.id, '/translate {ваше речення українською на англійську} /translate- {ваше речення будь-якою мовою для перекладу на українську}')

@bot.message_handler(commands=['contact'])
def contact(message):
    task = message.text.split('/contact')
    print(task)
    t = task[1]
    numero = t.split(maxsplit=2)[0]
    name = t.split(maxsplit=2)[1]
    try:
        bot.send_contact(message.chat.id, numero, name)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ти як взагалі написав?')

@bot.message_handler(commands=['getlocal'])
def getlocal(message):
    adress = message.text.split('/getlocal')[1:]
    try:
        coordinates = getto(addres= adress )
        coordinates = coordinates.split(" ")
        bot.send_location(message.chat.id, coordinates[0], coordinates[1])
    except Exception as e:
        bot.send_message(message.chat.id, f'{e}')
        
   

@bot.message_handler(commands=['translate'])
def trnslate(message):
    text = message.text.split('/translate')[1:]
    textik = text[0]
    translator = Translator()
    translation = translator.translate(text=textik, src='uk', dest='en')
    bot.send_message(message.chat.id, translation.text)

@bot.message_handler(commands=['translate-'])
def trnslate2(message):
    text = message.text.split('/translate-')[1:]
    textik = text[0]
    translator = Translator()
    translation = translator.translate(text=textik, src='auto', dest='uk')
    bot.send_message(message.chat.id, translation.text)



def getwiki(s):
    wikipedia.set_lang("uk")
    try:
        ny = wikipedia.page(s)

        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub(r'\([^()]*\)', '', wikitext2)
        wikitext2=re.sub(r'\([^()]*\)', '', wikitext2)
        wikitext2=re.sub(r'\{[^\{\}]*\}', '', wikitext2)

        return wikitext2
    except Exception as e:
        return 'Йоойоойоййй, нічого не знаййдено..'

@bot.message_handler(commands=['wiki'])
def wiki(message):
    value = message.text.split('/wiki')[1:]
    if value[0] == '':
        bot.send_message(message.chat.id, 'А що збираєшься шукати, га?')
    else:
        bot.send_message(message.chat.id, getwiki(value[0]))


@bot.message_handler(content_types=["photo"])
def pics(message):
    try:  
        if '/oilpic' in message.caption:
            bot.send_message(message.chat.id, 'Зараз буде обробка твоєї світлині у размазню')
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)

            os.chdir("C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik");
            with open("pic\\image.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            print('yesss')
            files = {'image': open("pic\\image.jpg", "rb")}
            r = requests.post("https://face.bubble.ru/_api/face", files=files)

            with open('pic\\result.jpg', 'wb') as f:
                f.write(r.content)

            fot = open('pic\\result.jpg', 'rb')
            
            bot.send_photo(message.chat.id, fot, 'ось що я зробило:')
        elif '/meme' in message.caption:
            bot.send_message(message.chat.id, 'Генерую мемас 😘')
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)

            os.chdir("C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik");
            NAMEFILE = "imageforMeme.jpg"
            with open("Memes\\imageforMeme.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            
            memes(NAMEFILE)
            os.chdir("C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik");
            fot = open('Memes\\memed\\imageforMeme.jpg', 'rb')
            
            bot.send_photo(message.chat.id, fot)
    except TypeError:
        pass

    
@bot.message_handler(commands=['randnum'])
def randnum(message):
    try:
        if ',' in message.text.split(maxsplit=2)[1]: 
            arg = message.text.split(maxsplit=2)[1].split(',')[0]
            arg2 = message.text.split(maxsplit=2)[2]
            res = random.randint(int(arg2), int(arg))

            bot.send_message(message.chat.id, f'Випадкове число з {arg2} до {arg}: {res}')
        elif message.text.split(maxsplit=2)[1].isdecimal():
            arg = message.text.split(maxsplit=2)[1]
            res = random.randint(1, int(arg))
            bot.send_message(message.chat.id, f'Випадкове число до {arg} : {res}')
        else:
            bot.send_message(message.chat.id, f'ТИ ЛЕДЬ НЕ ЗЛОМАВ БОТА, ЛОЛЯ')
    except IndexError:
        res = random.randint(0, 100)
        bot.send_message(message.chat.id, f'Випадкове число: {res}') 

@bot.message_handler(commands=['go'])
def go_poll(message):
    task = message.text.split(maxsplit=1)[1]
    bot.send_poll(message.chat.id, f'Go {task.lower()}', ['Так','Ні'])


@bot.message_handler(commands=['randforward'])
def randforward(message):
    try:
        bot.forward_message(message.chat.id, -1001688903092, random.randint(11, 39) ) #-1001688903092
    except ValueError as e:
        bot.send_message(message.chat.id, f'{e}')

@bot.message_handler(commands=['copypasta'])
def copypasta(message):
    bot.send_message(message.chat.id, random.choice(copypastas))



bot.polling(none_stop=True)