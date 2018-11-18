import cocos
import pyglet
from cocos.director import director
from cocos.menu import Menu, CENTER, MenuItem
from pyglet.window import key
import random
from cocos.layer import *
from math import *
import time

global questions, arr_q, lives_c, begin, end

questions = [
    'Что такое HTML?',
    'Язык гипертекстовой разметки веб-страниц',
    'Шаблонизатор',
    'Интернет-протокол',
    '1',
    'Каким языком программирования является Python?',
    'Это не язык программирования, а язык гипертекстовой разметки',
    'Это высокоуровневый язык программирования',
    'Это низкоуровневый язык программирования',
    '2',
    'Что такое браузер?',
    'Программа для просмотра сайтов',
    'Удалённый сервер, на котором размещен сайт',
    'Программа для отправки электронной почты',
    '1',
    'В каком году был основан Facebook?',
    'В 2002 году',
    'В 2004 году',
    'В 2006 году',
    '2',
    'В какой стране впервые появился Интернет?',
    'США',
    'Франция',
    'Япония',
    '1',
    'Какая компьютерная сеть, созданная в 1969 году, стала прототипом сети Интернет?',
    'ARPANET',
    'Usenet',
    'BITNET',
    '1',
    'Кто спроектировал первую программируемую вычислительную машину?',
    'Илон Маск',
    'Альберт Эйнштейн',
    'Чарльз Беббидж',	
    '3',
    'Что из перечисленного не является единицей измерения информации?',
    'Микробайт',
    'Кибибит',
    'Пикабайт',
    '1',
    'Что из нижеперечисленного не относится к структурам данных в информатике?',
    'Куча',
    'Дерево',
    'Куст',
    '3',
    'Как назывался первый в мире язык программирования высокого уровня?',
    'Фортран',
    'Планкалкюль',
    'Бейсик',
    '2',
    ]



arr_q = [-1,-1,-1,-1,-1]



def q_numbers(arr_q):
    repetition = False
    for i in range(5):
        q = random.randint(0,9)
        for j in arr_q:
            if q == j:
                repetition = True  
            while repetition == True:
                q = random.randint(0,9)
                repetition = False
                for j in arr_q:
                    if q == j:
                        repetition = True
        arr_q[i] = q

lives_c = 0
vel_y_1 = 0
vel_y_2 = 0
vel_y_3 = 0
vel_y_4 = 0
vel_y_5 = 0
begin=0
end=0    
class rules(cocos.layer.Layer):
    
    def __init__(self):
        super().__init__()

        spr_r = cocos.sprite.Sprite('rules.jpg')
        spr_r.position = 480, 360
        spr_r.velocity = (0, 0)
        spr_r.do(Mover_rules())
        self.add(spr_r)


            
class main_menu(Menu):

    def __init__(self):
        super(main_menu, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem("Новая игра", self.start)),
            (MenuItem("Правила", self.rules)),
            (MenuItem("Выход", self.quit))
        ]
        self.create_menu(menu_items)

    def start(self):
        director.replace(question_scene_0)

    def rules(self):
        director.replace(rules_scene)

    def quit(self):
        director.window.close()



class new_game(cocos.layer.Layer):

    def __init__(self):
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        menu = main_menu()
        self.add(menu)
        
        label = cocos.text.Label("Ньютоновские яблоки", font_name = "monospaced", font_size = 50,
                                 italic = True, color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label.position = 480, 690
        self.add(label)

class end_game(cocos.layer.Layer):
    global begin, end 
    def __init__(self):
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        label = cocos.text.Label("Вы продержались " + str (20) + " секунд",font_name = "monospaced", font_size = 50,
                                 italic = True, color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")
        label.position = 480,360
        background.do(Mover_end())
        self.add(label)
        
      
class answer_menu_0(Menu):

    global answer_1_0, answer_2_0, answer_3_0, code_0, arr_q
    q_numbers(arr_q)
    print(arr_q)

    q = arr_q[0]
    answer_1_0 = questions[q * 5 + 1]
    answer_2_0 = questions[q * 5 + 2]
    answer_3_0 = questions[q * 5 + 3]
    code_0 = questions[q * 5 + 4]

    def __init__(self):
        super(answer_menu_0, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem(answer_1_0, self.say_1)),
            (MenuItem(answer_2_0, self.say_2)),
            (MenuItem(answer_3_0, self.say_3))
        ]
        self.create_menu(menu_items)

    def say_1(self):
        global lives_c
        lives_c = 0
        if code_0 == '1':
            lives_c = lives_c + 1
        director.replace(question_scene_1)

    def say_2(self):
        global lives_c
        lives_c = 0
        if code_0 == '2':
            lives_c = lives_c + 1
        director.replace(question_scene_1)

    def say_3(self):
        global lives_c
        lives_c = 0
        if code_0 == '3':
            lives_c = lives_c + 1
        director.replace(question_scene_1)
        


class answer_menu_1(Menu):

    global answer_1_1, answer_2_1, answer_3_1, code_1, arr_q, questions

    q = arr_q[1]
    answer_1_1 = questions[q * 5 + 1]
    answer_2_1 = questions[q * 5 + 2]
    answer_3_1 = questions[q * 5 + 3]
    code_1 = questions[q * 5 + 4]

    def __init__(self):
        super(answer_menu_1, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem(answer_1_1, self.say_1)),
            (MenuItem(answer_2_1, self.say_2)),
            (MenuItem(answer_3_1, self.say_3))
        ]
        self.create_menu(menu_items)

    def say_1(self):
        global lives_c
        if code_1 == '1':
            lives_c = lives_c + 1
        director.replace(question_scene_2)

    def say_2(self):
        global lives_c
        if code_1 == '2':
            lives_c = lives_c + 1
        director.replace(question_scene_2)

    def say_3(self):
        global lives_c
        if code_1 == '3':
            lives_c = lives_c + 1
        director.replace(question_scene_2)



class answer_menu_2(Menu):

    global answer_1_2, answer_2_2, answer_3_2, code_2, arr_q, questions

    q = arr_q[2]
    answer_1_2 = questions[q * 5 + 1]
    answer_2_2 = questions[q * 5 + 2]
    answer_3_2 = questions[q * 5 + 3]
    code_2 = questions[q * 5 + 4]

    def __init__(self):
        super(answer_menu_2, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem(answer_1_2, self.say_1)),
            (MenuItem(answer_2_2, self.say_2)),
            (MenuItem(answer_3_2, self.say_3))
        ]
        self.create_menu(menu_items)

    def say_1(self):
        global lives_c
        if code_2 == '1':
            lives_c = lives_c + 1
        director.replace(question_scene_3)

    def say_2(self):
        global lives_c
        if code_2 == '2':
            lives_c = lives_c + 1
        director.replace(question_scene_3)

    def say_3(self):
        global lives_c
        if code_2 == '3':
            lives_c = lives_c + 1
        director.replace(question_scene_3)



class answer_menu_3(Menu):

    global answer_1_3, answer_2_3, answer_3_3, code_3, arr_q, questions

    q = arr_q[3]
    answer_1_3 = questions[q * 5 + 1]
    answer_2_3 = questions[q * 5 + 2]
    answer_3_3 = questions[q * 5 + 3]
    code_3 = questions[q * 5 + 4]

    def __init__(self):
        super(answer_menu_3, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem(answer_1_3, self.say_1)),
            (MenuItem(answer_2_3, self.say_2)),
            (MenuItem(answer_3_3, self.say_3))
        ]
        self.create_menu(menu_items)

    def say_1(self):
        global lives_c
        if code_3 == '1':
            lives_c = lives_c + 1
        director.replace(question_scene_4)

    def say_2(self):
        global lives_c
        if code_3 == '2':
            lives_c = lives_c + 1
        director.replace(question_scene_4)

    def say_3(self):
        global lives_c
        if code_3 == '3':
            lives_c = lives_c + 1
        director.replace(question_scene_4)



class answer_menu_4(Menu):

    global answer_1_4, answer_2_4, answer_3_4, code_4, arr_q, questions

    q = arr_q[4]
    answer_1_4 = questions[q * 5 + 1]
    answer_2_4 = questions[q * 5 + 2]
    answer_3_4 = questions[q * 5 + 3]
    code_4 = questions[q * 5 + 4]

    def __init__(self):
        super(answer_menu_4, self).__init__()
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        menu_items = [
            (MenuItem(answer_1_4, self.say_1)),
            (MenuItem(answer_2_4, self.say_2)),
            (MenuItem(answer_3_4, self.say_3))
        ]
        self.create_menu(menu_items)

    def say_1(self):
        global lives_c
        if code_4 == '1':
            lives_c = lives_c + 1
        if (lives_c == 0):    
            director.replace(menu_scene)
        else:
            begin=time.time()
            director.replace(game_scene)
            print(lives_c)

    def say_2(self):
        global lives_c
        if code_4 == '2':
            lives_c = lives_c + 1
        if (lives_c == 0):    
            director.replace(menu_scene)
        else:
            begin=time.time()
            director.replace(game_scene)
            print(lives_c)


    def say_3(self):
        global lives_c
        if code_4 == '3':
            lives_c = lives_c + 1
        if (lives_c == 0):    
            director.replace(menu_scene)
        else:
            begin=time.time()
            director.replace(game_scene)
            print(lives_c)

                        
class Question_0(cocos.layer.Layer):
    
    global questions, arr_q, question0

    q = arr_q[0]
    question0 = questions[q * 5]
        
    def __init__(self):
        super().__init__()  
        label = cocos.text.Label(question0, font_name = "monospaced", font_size = 15,
                                 color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label.position = 480, 500
        self.add(label)



class Question_1(cocos.layer.Layer):
    
    global questions, arr_q, question1

    q = arr_q[1]
    question1 = questions[q * 5]
        
    def __init__(self):
        super().__init__()  
        label_q = cocos.text.Label(question1, font_name = "monospaced", font_size = 15,
                                 color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label_q.position = 480, 500
        self.add(label_q)


        
class Question_2(cocos.layer.Layer):
    
    global questions, arr_q, question2

    q = arr_q[2]
    question2 = questions[q * 5]
        
    def __init__(self):
        super().__init__()  
        label = cocos.text.Label(question2, font_name = "monospaced", font_size = 15,
                                 color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label.position = 480, 500
        self.add(label)


        
class Question_3(cocos.layer.Layer):
    
    global questions, arr_q, question3

    q = arr_q[3]
    question3 = questions[q * 5]
        
    def __init__(self):
        super().__init__()  
        label = cocos.text.Label(question3, font_name = "monospaced", font_size = 15,
                                 color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label.position = 480, 500
        self.add(label)


        
class Question_4(cocos.layer.Layer):
    
    global questions, arr_q, question4

    q = arr_q[4]
    question4 = questions[q * 5]
        
    def __init__(self):
        super().__init__()  
        label = cocos.text.Label(question4, font_name = "monospaced", font_size = 15,
                                 color = (255, 0, 0, 255), anchor_x = "center", anchor_y = "center")

        label.position = 480, 500
        self.add(label)


class Exam_Layer_0(cocos.layer.Layer):
    global lives_c
    def __init__(self):
        global lives_c
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        a_menu_0 = answer_menu_0()
        self.add(a_menu_0)
        spr_q_0= Question_0()
        self.add(spr_q_0)


class Exam_Layer_1(cocos.layer.Layer):
    global lives_c
    def __init__(self):
        global lives_c
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        a_menu_1 = answer_menu_1()
        self.add(a_menu_1)
        spr_q_1 = Question_1()
        self.add(spr_q_1)



class Exam_Layer_2(cocos.layer.Layer):
    global lives_c
    def __init__(self):
        global lives_c
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        a_menu_2 = answer_menu_2()
        self.add(a_menu_2)
        spr_q_2 = Question_2()
        self.add(spr_q_2)





class Exam_Layer_3(cocos.layer.Layer):
    global lives_c
    def __init__(self):
        global lives_c
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        a_menu_3 = answer_menu_3()
        self.add(a_menu_3)
        spr_q_3 = Question_3()
        self.add(spr_q_3)



class Exam_Layer_4(cocos.layer.Layer):
    global lives_c
    def __init__(self):
        global lives_c
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        a_menu_4 = answer_menu_4()
        self.add(a_menu_4)
        spr_q_4 = Question_4()
        self.add(spr_q_4)


class Mover_rules(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        
        if keyboard[key.TAB]:
            director.replace(menu_scene)


class Mover_end(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        
        if keyboard[key.TAB]:
            director.replace(menu_scene)

class Mover_newton(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT])*500
        vel_y = 0;
        
        self.target.velocity = (vel_x, vel_y)

        if keyboard[key.RIGHT] and self.target.position[0] > 825 \
                or keyboard[key.LEFT] and self.target.position[0] < 115:
            self.target.velocity = (0, 0)
   
        if keyboard[key.TAB]:
            director.replace(menu_scene)



class Mover_apple1(cocos.actions.Move):
    def step(self,dt):
        global newton, apple, lives_c, begin, end, vel_y_1
        super().step(dt)
        vel_x = 0
        vel_y_1 = vel_y_1 - 5.6
        
        self.target.velocity = (vel_x,vel_y_1)
        if (self.target.position[1] < -36 ):
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_1 = 0
            self.target.position = (pos_x, pos_y)
            
        if (self.target.position[1] < 300 and (abs(self.target.position[0] - newton.position[0])<100)):
            pos_x = random.randint(30, 930)
            pos_y = 800
            self.target.position = (pos_x, pos_y)
            vel_y_1 = 0
            lives_c=lives_c-1
            
        if (lives_c==0):
            end=time.time()
            print(end-begin)
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_1 = 0
            director.replace(menu_scene)

class Mover_apple2(cocos.actions.Move):
    def step(self,dt):
        global newton, apple, lives_c, begin, end, vel_y_2
        super().step(dt)
        vel_x = 0
        vel_y_2 = vel_y_2 - 5.6
        
        self.target.velocity = (vel_x,vel_y_2)
        if (self.target.position[1] < -36 ):
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_2 = 0
            self.target.position = (pos_x, pos_y)
            
        if (self.target.position[1] < 300 and (abs(self.target.position[0] - newton.position[0])<100)):
            pos_x = random.randint(30, 930)
            pos_y = 800
            self.target.position = (pos_x, pos_y)
            vel_y_2 = 0
            lives_c=lives_c-1
            
        if (lives_c==0):
            end=time.time()
            print(end-begin)
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_2 = 0
            director.replace(menu_scene)

class Mover_apple3(cocos.actions.Move):
    def step(self,dt):
        global newton, apple, lives_c, begin, end, vel_y_3
        super().step(dt)
        vel_x = 0
        vel_y_3 = vel_y_3 - 5.6
        
        self.target.velocity = (vel_x,vel_y_3)
        if (self.target.position[1] < -36 ):
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_3 = 0
            self.target.position = (pos_x, pos_y)
            
        if (self.target.position[1] < 300 and (abs(self.target.position[0] - newton.position[0])<100)):
            pos_x = random.randint(30, 930)
            pos_y = 800
            self.target.position = (pos_x, pos_y)
            vel_y_3 = 0
            lives_c=lives_c-1
            
        if (lives_c==0):
            end=time.time()
            print(end-begin)
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_3 = 0
            director.replace(menu_scene)
            

class Mover_apple4(cocos.actions.Move):
    def step(self,dt):
        global newton, apple, lives_c, begin, end, vel_y_4
        super().step(dt)
        vel_x = 0
        vel_y_4 = vel_y_4 - 5.6
        
        self.target.velocity = (vel_x,vel_y_4)
        if (self.target.position[1] < -36 ):
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_4 = 0
            self.target.position = (pos_x, pos_y)
            
        if (self.target.position[1] < 300 and (abs(self.target.position[0] - newton.position[0])<100)):
            pos_x = random.randint(30, 930)
            pos_y = 800
            self.target.position = (pos_x, pos_y)
            vel_y_4 = 0
            lives_c=lives_c-1
            
        if (lives_c==0):
            end=time.time()
            print(end-begin)
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_4 = 0
            director.replace(menu_scene)

class Mover_apple5(cocos.actions.Move):
    def step(self,dt):
        global newton, apple, lives_c, begin, end, vel_y_5
        super().step(dt)
        vel_x = 0
        vel_y_5 = vel_y_5 - 5.6
        
        self.target.velocity = (vel_x,vel_y_5)
        if (self.target.position[1] < -36 ):
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_5 = 0
            self.target.position = (pos_x, pos_y)
            
        if (self.target.position[1] < 300 and (abs(self.target.position[0] - newton.position[0])<100)):
            pos_x = random.randint(30, 930)
            pos_y = 800
            self.target.position = (pos_x, pos_y)
            vel_y_5 = 0
            lives_c=lives_c-1
            
        if (lives_c==0):
            end=time.time()
            print(end-begin)
            pos_x = random.randint(30, 930)
            pos_y = 800
            vel_y_5 = 0
            director.replace(menu_scene)            
        
class game(cocos.layer.Layer):
    def __init__(self):
        global lives_c, newton, begin
        super().__init__()
        background = cocos.sprite.Sprite('apple_garden.jpg')
        self.add(background)
        background.position = (480, 360)
        background.velocity = (0, 0)
        newton.position = 480, 159
        newton.velocity = (0, 0)
        newton.do(Mover_newton())
        self.add(newton)
        begin=time.time()
        apple1.position = random.randint(30,930),800
        apple1.velocity=(0,0)
        apple1.do(Mover_apple1())
        self.add(apple1)
        apple2.position = random.randint(30,930),900
        apple2.velocity=(0,0)
        apple2.do(Mover_apple2())
        self.add(apple2)
        apple3.position = random.randint(30,930),1000
        apple3.velocity=(0,0)
        apple3.do(Mover_apple3())
        self.add(apple3)
        apple4.position = random.randint(30,930),1100
        apple4.velocity=(0,0)
        apple4.do(Mover_apple4())
        self.add(apple4)
        apple5.position = random.randint(30,930),1200
        apple5.velocity=(0,0)
        apple5.do(Mover_apple5())
        self.add(apple5)
       
              
if __name__ == "__main__":
    director.init(width = 960, height = 720, caption = "Newton's apples")
    director.window.pop_handlers()
    
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    newton = cocos.sprite.Sprite("newton.png")
    apple1 = cocos.sprite.Sprite("apple.png")
    apple2 = cocos.sprite.Sprite("apple.png")
    apple3 = cocos.sprite.Sprite("apple.png")
    apple4 = cocos.sprite.Sprite("apple.png")
    apple5 = cocos.sprite.Sprite("apple.png")
    life = cocos.sprite.Sprite("life.png")

    menu_scene = cocos.scene.Scene(new_game())
    
    rules_scene = cocos.scene.Scene(rules())
    end_scene = cocos.scene.Scene(end_game())
    question_scene_0 = cocos.scene.Scene(Exam_Layer_0())
    question_scene_1 = cocos.scene.Scene(Exam_Layer_1())
    question_scene_2 = cocos.scene.Scene(Exam_Layer_2())
    question_scene_3 = cocos.scene.Scene(Exam_Layer_3())
    question_scene_4 = cocos.scene.Scene(Exam_Layer_4())
    
    game_scene = cocos.scene.Scene(game())
    
    director.run(menu_scene)
