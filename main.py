#Підключаєм модулі
import play
import pygame
#Опрацьовуєм функції
pygame.init()
#Додаєм змогу додавати звук
pygame.mixer.init()
#Робив ігровий екран 
play.set_backdrop('purple')
#Написи для розуміння що це за гра 
text1 = play.new_text(words="Це класне піаніно для гри!", x=0, y=200) 
text2 = play.new_text(words="Створи свою мелодію натискаючи на клавіші", x=0, y=150)
#Создаєм кнопку для включення записаной мелодії
play_melody = play.new_box(color='light green', border_color='aquamarine', border_width=4, x=-100, y=-170, width=160, height=50) #Сама кнопка
play_melody_txt = play.new_text(words="грати мелодію", x=-100, y=-170, font_size=23) # Текст в ній
#Создаєм кнопку для удаління мелодії
clear_melody = play.new_box(color='light green', border_color='aquamarine', border_width=4, x=100, y=-170, width=160, height=50) #Сама кнопка
clear_melody_txt = play.new_text(words="очистити мелодію", x=100, y=-170, font_size=23) # Текст в ній
#Робим інструменти
piano_btn = play.new_circle(color = "black", border_color = "light green", border_width = 2, radius = 12, x = -160, y = -100) #Кнопка піаніно
piano_txt = play.new_text(words = "piano", font_size = 25, x = -120, y = -100) #Текст піаніно

flute_btn = play.new_circle(color = "white", border_color = "light green", border_width = 2, radius = 12, x = -70, y = -100) # Кнопка флейта
flute_txt = play.new_text(words = "flute", font_size = 25, x = -30, y = -100) # Текст флейта 

guitar_btn = play.new_circle(color = "white", border_color = "light green", border_width = 2, radius = 12, x = 20, y = -100) # Кнопка гитара
guitar_txt = play.new_text(words = "guitar", font_size = 25, x = 60, y = -100) # Текст гитара

violin_btn = play.new_circle(color = "white", border_color = "light green", border_width = 2, radius = 12, x = 110, y = -100) # Кнопка скрипка
violin_txt = play.new_text(words = "violin", font_size = 25, x = 150, y = -100) # Текст скрипка

#Змінна для перемикання інструментів
get_instrument = 1
#Списки інструментів
keys = [] # Список для клавіш
piano = [] # Піаніно
flute = [] # Флейта
guitar = [] # Гитара 
violin = [] # Скрипка
#Список для мелодії
melody = []
#Цикл який виконується 8 разів для створення клавіш
for i in range(8):
    key_x = -180 + i * 50 # Зміна координат
    key = play.new_box(color='white', border_color='black', border_width=4, width=40, height=100, x=key_x, y=0) # Сама клавіша
    keys.append(key) # Додавання клавіши до списку
    piano_snd = pygame.mixer.Sound(f"{i+1}.ogg") #Додавання звук піаніно
    piano.append(piano_snd) # Додавання звука до списку
    flute_snd = pygame.mixer.Sound(f"f{i + 1}.ogg") #Додавання звук флейти
    flute.append(flute_snd) # Додавання звука до списку
    guitar_snd = pygame.mixer.Sound(f"g{i + 1}.ogg") #Додавання звук гитари
    guitar.append(guitar_snd) # Додавання звука до списку
    violin_snd = pygame.mixer.Sound(f"v{i + 1}.ogg") #Додавання звук скрипка
    violin.append(violin_snd) # Додавання звука до списку
#Запуск Гри
@play.when_program_starts
def start():
    pass
#Перевірка чи нажата клавіша грати мелодію
@play_melody.when_clicked
async def play_mel(): # Функція для роботи кнопки 
    for mel in melody: # цикл для перевірки на входження в список
        mel.play() # програвання звуку 
        play_melody.color = "aquamarine" #Зміна кольру
        await play.timer(0.4) # Таймер
        play_melody.color = "light green" # Зміна кольору
#Перевірка чи нажата клавіша очистити мелодію
@clear_melody.when_clicked
async def clear_mel(): # Функція для роботи кнопки 
    melody.clear() 
    clear_snd = pygame.mixer.Sound('clear_melody.wav')
    clear_snd.play() 
    clear_melody.color = "aquamarine"
    await play.timer(0.4) 
    clear_melody.color = "light green"
#Перевірка чи нажата кнопка інструмент піаніно
@piano_btn.when_clicked # Функція для роботи кнопки 
def piano_b():
    global get_instrument
    piano_btn.color = "black"
    flute_btn.color = "white"
    guitar_btn.color = "white"
    violin_btn.color = "white"
    get_instrument = 1
#Перевірка чи нажата кнопка інструмент флейта
@flute_btn.when_clicked
def flute_b(): # Функція для роботи кнопки 
    global get_instrument
    piano_btn.color = "white"
    flute_btn.color = "black"
    guitar_btn.color = "white"
    violin_btn.color = "white"
    get_instrument = 2
#Перевірка чи нажата кнопка інструмент гитара
@guitar_btn.when_clicked
def guitar_b(): # Функція для роботи кнопки 
    global get_instrument
    piano_btn.color = "white"
    flute_btn.color = "white"
    guitar_btn.color = "black"
    violin_btn.color = "white"
    get_instrument = 3
#Перевірка чи нажата кнопка інструмент скрипка
@violin_btn.when_clicked
def violin_b(): # Функція для роботи кнопки 
    global get_instrument
    piano_btn.color = "white"
    flute_btn.color = "white"
    guitar_btn.color = "white"
    violin_btn.color = "black"
    get_instrument = 4
#Бескінечний цикл
@play.repeat_forever
async def play_piano():
    for j in range(len(keys)): #Цикл для перевірки клавіш
        #Перевірка якщо нажата клавиша і інструмент піаніно
        if keys[j].is_clicked and get_instrument == 1:
            keys[j].color = 'light green'
            piano[j].play()
            melody.append(piano[j])
            await play.timer(0.3)
            keys[j].color = 'white'
        #Перевірка якщо нажата клавиша і інструмент флейта
        if keys[j].is_clicked and get_instrument == 2:
            keys[j].color = 'light green'
            flute[j].play()
            melody.append(flute[j])
            await play.timer(0.3)
            keys[j].color = 'white'
        #Перевірка якщо нажата клавиша і інструмент гитара
        if keys[j].is_clicked and get_instrument == 3:
            keys[j].color = 'light green'
            guitar[j].play()
            melody.append(guitar[j])
            await play.timer(0.3)
            keys[j].color = 'white'
        #Перевірка якщо нажата клавиша і інструмент скрипка
        if keys[j].is_clicked and get_instrument == 4:
            keys[j].color = 'light green'
            violin[j].play()
            melody.append(violin[j])
            await play.timer(0.3)
            keys[j].color = 'white'
#Старт Програми
play.start_program()