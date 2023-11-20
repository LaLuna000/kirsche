from kivy.app import App
import sys
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from functools import partial
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.stacklayout import StackLayout


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # установка фона формы
        with layout.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            self.rect = Rectangle(size=(10000, 10000), pos=layout.pos)

        # добавление названия "запомни одинаковые"
        title = Label(text='запомни одинаковые', pos_hint={'x': 0, 'top': 1}, size_hint=(1, 0.1), color=(0.1, 0.1, 0.1, 0.8))
        layout.add_widget(title)

        # добавление кнопки "играть"
        play_button = Button(text='играть', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(0.3, 0.5, 0.4, 0.8))
        play_button.bind(on_press=self.switch_to_difficulty)
        layout.add_widget(play_button)

        # добавление кнопки "правила"
        menu_button = Button(text='правила', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.4}, background_color=(0.3, 0.5, 0.4, 0.8))
        menu_button.bind(on_press=self.switch_to_rules)
        layout.add_widget(menu_button)

        # добавление кнопки "выход"
        exit_button = Button(text='выход', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8))
        exit_button.bind(on_press=self.exit_app)
        layout.add_widget(exit_button)

        self.add_widget(layout)

    def switch_to_rules(self, *args):
        self.parent.current = 'rules_screen'

    def switch_to_difficulty(self, *args):
        self.parent.current = 'difficulty_screen'

    def exit_app(self, *args):
        App.get_running_app().stop()


class RulesScreen(Screen):
    def __init__(self, **kwargs):
        super(RulesScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        with self.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            Rectangle(size=(10000, 10000))

        title_label = Label(text='Правила', size_hint=(1, 1.5))
        title_label.color = (0, 0, 0, 1)  # черные буквы

        rule_label1 = Label(text='На игровом поле находится четное количество карточек, повернутых лицевой стороной вниз.', size_hint=(1, 1.1))
        rule_label1.color = (0, 0, 0, 1)  # черные буквы
        rule_label2 = Label(text='В игре «Запомни одинаковые» пользователь должен поочередно открывать любые две картинки,', size_hint=(1, 1))
        rule_label2.color = (0, 0, 0, 1)  # черные буквы
        rule_label3 = Label(text='находя среди них одинаковые. Если игрок открывает разные, они кладутся обратно,', size_hint=(1, 0.9))
        rule_label3.color = (0, 0, 0, 1)  # черные буквы
        rule_label4 = Label(text='если одинаковые – они убираются с поля. Цель игры – убрать с поля все карточки. ', size_hint=(1, 0.8))
        rule_label4.color = (0, 0, 0, 1)  # черные буквы
        rule_label5 = Label(text='Игра заканчивается, когда на поле не остается карточек.', size_hint=(1, 0.7))
        rule_label5.color = (0, 0, 0, 1)  # черные буквы

        ok_button = Button(text='понятно', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2}, background_color=(0.3, 0.5, 0.4, 0.8))
        ok_button.bind(on_press=self.switch_to_main)
        ok_button.color = (1, 1, 1, 1)  # белые буквы

        self.add_widget(title_label)
        self.add_widget(rule_label1)
        self.add_widget(rule_label2)
        self.add_widget(rule_label3)
        self.add_widget(rule_label4)
        self.add_widget(rule_label5)
        self.add_widget(ok_button)

    def switch_to_main(self, *args):
        self.parent.current = 'main_screen'


class DifficultyScreen(Screen):
    def __init__(self, **kwargs):
        super(DifficultyScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        layout = FloatLayout()

        # установка фона формы
        with layout.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            self.rect = Rectangle(size=(10000, 10000), pos=layout.pos)

        # добавление названия "сложность"
        title = Label(text='сложность', pos_hint={'x': 0, 'top': 1}, size_hint=(1, 0.1), color=(0.1, 0.1, 0.1, 1))
        layout.add_widget(title)

        # добавление кнопки "Легко"
        easy_button = Button(text='Легко', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.6}, background_color=(0.3, 0.5, 0.4, 0.8))
        easy_button.bind(on_press=self.switch_to_easy)
        layout.add_widget(easy_button)

        # добавление кнопки "Средне"
        medium_button = Button(text='Средне', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(0.3, 0.5, 0.4, 0.8))
        medium_button.bind(on_press=self.switch_to_medium)
        layout.add_widget(medium_button)

        # добавление кнопки "Сложно"
        hard_button = Button(text='Сложно', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.4}, background_color=(0.3, 0.5, 0.4, 0.8))
        hard_button.bind(on_press=self.switch_to_hard)
        layout.add_widget(hard_button)

        # добавление кнопки "назад"
        back_button = Button(text='назад', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8))
        back_button.bind(on_press=self.switch_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def switch_to_main(self, *args):
        self.parent.current = 'main_screen'

    def switch_to_easy(self, *args):
        self.parent.current = 'easy_screen'

    def switch_to_medium(self, *args):
        self.parent.current = 'medium_screen'

    def switch_to_hard(self, *args):
        self.parent.current = 'hard_screen'


class EasyLevelScreen(Screen):
    def __init__(self, **kwargs):
        super(EasyLevelScreen, self).__init__(**kwargs)
        self.selected_button = None
        self.orientation = 'vertical'
        self.layout = FloatLayout()

        # установка фона формы
        with self.layout.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            self.rect = Rectangle(size=(10000, 10000), pos=self.layout.pos)

        # добавление названия
        title = Label(text='Легкий уровень', pos_hint={'x': 0, 'top': 1}, size_hint=(1, 0.1), color=(0, 0, 0, 1))
        self.layout.add_widget(title)

        # добавление поля 3x2 из кнопок с картинками
        for i in range(1, 4):
            for j in range(1, 3):
                if ((i == 1) and (j == 1)) or ((i == 2) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.25, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='сатурн.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 1) and (j == 2)) or ((i == 3) and (j == 1)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.25, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='венера.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 2) and (j == 1)) or ((i == 3) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.25, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='земля.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

        # добавление кнопки "правила"
        rules_button = Button(text='правила', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8), halign='center')
        rules_button.bind(on_press=self.switch_to_rules)
        self.layout.add_widget(rules_button)

        # добавление кнопки "назад"
        back_button = Button(text='назад', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8))
        back_button.bind(on_press=self.switch_to_difficulty)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def switch_to_difficulty(self, *args):
        self.parent.current = 'difficulty_screen'

    def switch_to_rules(self, *args):
        self.parent.current = 'rules_screen'

    def on_button_press(self, button):
        if not self.selected_button:
            self.selected_button = button
        else:
            if (self.selected_button.background_down == button.background_down) and (self.selected_button != button):
                self.layout.remove_widget(self.selected_button)
                self.layout.remove_widget(button)
            else:
                # перевернуть кнопки обратно
                Clock.schedule_once(
                    partial(self.reset_buttons, button, self.selected_button), 2)
            self.selected_button = None

    def reset_buttons(self, button1, button2, dt):
        button1.background_normal = 'фон.jpg'
        button2.background_normal = 'фон.jpg'


class MediumLevelScreen(Screen):
    def __init__(self, **kwargs):
        super(MediumLevelScreen, self).__init__(**kwargs)
        self.selected_button = None
        self.orientation = 'vertical'
        self.layout = FloatLayout()

        # установка фона формы
        with self.layout.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            self.rect = Rectangle(size=(10000, 10000), pos=self.layout.pos)

        # добавление названия
        title = Label(text='Средний уровень', pos_hint={'x': 0, 'top': 1}, size_hint=(1, 0.1), color=(0, 0, 0, 1))
        self.layout.add_widget(title)

        # добавление поля 4x2 из кнопок с картинками
        for i in range(1, 5):
            for j in range(1, 3):
                if ((i == 1) and (j == 1)) or ((i == 4) and (j == 1)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='сатурн.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 3) and (j == 2)) or ((i == 4) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='венера.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 2) and (j == 1)) or ((i == 1) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='земля.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 3) and (j == 1)) or ((i == 2) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 0.9 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='марс.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

        # добавление кнопки "правила"
        rules_button = Button(text='правила', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8), halign='center')
        rules_button.bind(on_press=self.switch_to_rules)
        self.layout.add_widget(rules_button)

        # добавление кнопки "назад"
        back_button = Button(text='назад', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8))
        back_button.bind(on_press=self.switch_to_difficulty)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def switch_to_difficulty(self, *args):
        self.parent.current = 'difficulty_screen'

    def switch_to_rules(self, *args):
        self.parent.current = 'rules_screen'

    def on_button_press(self, button):
        if not self.selected_button:
            self.selected_button = button
        else:
            if (self.selected_button.background_down == button.background_down) and (self.selected_button != button):
                self.layout.remove_widget(self.selected_button)
                self.layout.remove_widget(button)
            else:
                # перевернуть кнопки обратно
                Clock.schedule_once(
                    partial(self.reset_buttons, button, self.selected_button), 2)
            self.selected_button = None

    def reset_buttons(self, button1, button2, dt):
        button1.background_normal = 'фон.jpg'
        button2.background_normal = 'фон.jpg'


class HardLevelScreen(Screen):
    def __init__(self, **kwargs):
        super(HardLevelScreen, self).__init__(**kwargs)

        self.selected_button = None

        self.orientation = 'vertical'
        self.layout = FloatLayout()

        # установка фона формы
        with self.layout.canvas.before:
            Color(0.8, 1, 0.7, 0.6)  # салатовый цвет
            self.rect = Rectangle(size=(10000, 10000), pos=self.layout.pos)

        # добавление названия
        title = Label(text='Сложный уровень', pos_hint={'x': 0, 'top': 1}, size_hint=(1, 0.1), color=(0, 0, 0, 1))
        self.layout.add_widget(title)

        # добавление поля 4x3 из кнопок с картинками
        for i in range(1, 5):
            for j in range(1, 4):
                if ((i == 1) and (j == 3)) or ((i == 4) and (j == 1)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='сатурн.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 4) and (j == 2)) or ((i == 3) and (j == 1)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='венера.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 1) and (j == 1)) or ((i == 3) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='земля.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 4) and (j == 3)) or ((i == 2) and (j == 2)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='марс.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 1) and (j == 2)) or ((i == 2) and (j == 1)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='юпитер.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

                if ((i == 2) and (j == 3)) or ((i == 3) and (j == 3)):
                    button = Button(size_hint=(0.2, 0.2), pos_hint={'center_x': i*0.205, 'center_y': 1 - j*0.25}, 
                                    background_normal='фон.jpg', background_down='Меркурий.jpg')
                    button.bind(on_press=self.on_button_press)
                    self.layout.add_widget(button)

        # добавление кнопки "правила"
        rules_button = Button(text='правила', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8), halign='center')
        rules_button.bind(on_press=self.switch_to_rules)
        self.layout.add_widget(rules_button)

        # добавление кнопки "назад"
        back_button = Button(text='назад', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0}, background_color=(0.3, 0.5, 0.4, 0.8))
        back_button.bind(on_press=self.switch_to_difficulty)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def switch_to_difficulty(self, *args):
        self.parent.current = 'difficulty_screen'

    def switch_to_rules(self, *args):
        self.parent.current = 'rules_screen'

    def on_button_press(self, button):
        if not self.selected_button:
            self.selected_button = button
        else:
            if (self.selected_button.background_down == button.background_down) and (self.selected_button != button):
                self.layout.remove_widget(self.selected_button)
                self.layout.remove_widget(button)
            else:
                # перевернуть кнопки обратно
                Clock.schedule_once(
                    partial(self.reset_buttons, button, self.selected_button), 1)
            self.selected_button = None

    def reset_buttons(self, button1, button2, dt):
        button1.background_normal = 'фон.jpg'
        button2.background_normal = 'фон.jpg'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(EasyLevelScreen(name='easy_screen'))
        sm.add_widget(MediumLevelScreen(name='medium_screen'))
        sm.add_widget(HardLevelScreen(name='hard_screen'))
        sm.add_widget(RulesScreen(name='rules_screen'))
        sm.add_widget(DifficultyScreen(name='difficulty_screen'))

        return sm


if __name__ == '__main__':
    MyApp().run()
