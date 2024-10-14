from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from datetime import datetime


class ProductScreen(Screen):
    def build(self):
        root = FloatLayout()

        # Top container for the text
        top_container = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(0.5625, None), height=300, pos_hint={'center_x': 0.5, 'top': 1})

        # Title
        title_label = Label(text="[b]illumi Product Recommendation[/b]", font_size='24sp', size_hint=(1, None), height=50, halign='left', valign='middle', markup=True)
        title_label.bind(size=title_label.setter('text_size'))
        top_container.add_widget(title_label)

        # Product Name
        product_label = Label(text="La Roche-Posay Effaclar Duo Dual Action Acne Treatment Cream", font_size='20sp', size_hint=(1, None), height=50, halign='left', valign='middle')
        product_label.bind(size=product_label.setter('text_size'))
        top_container.add_widget(product_label)

        # Price
        price_label = Label(text="$29.99 for a 1.35 fl oz tube", font_size='18sp', size_hint=(1, None), height=30, halign='left', valign='middle')
        price_label.bind(size=price_label.setter('text_size'))
        top_container.add_widget(price_label)

        # Key Points
        key_points_label = Label(text=" Key Points:", font_size='20sp', size_hint=(1, None), height=30, halign='left', valign='middle')
        key_points_label.bind(size=key_points_label.setter('text_size'))
        top_container.add_widget(key_points_label)

        key_point1_label = Label(text="- Contains Benzoyl Peroxide", font_size='18sp', size_hint=(1, None), height=30, halign='left', valign='middle')
        key_point1_label.bind(size=key_point1_label.setter('text_size'))
        top_container.add_widget(key_point1_label)

        key_point2_label = Label(text="- Anti-Inflammatory", font_size='18sp', size_hint=(1, None), height=30, halign='left', valign='middle')
        key_point2_label.bind(size=key_point2_label.setter('text_size'))
        top_container.add_widget(key_point2_label)

        root.add_widget(top_container)

        # Product Image in the middle
        product_image = Image(source='C:\M&TSI\productd.jpg', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        root.add_widget(product_image)

        # Logo at the bottom
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint=(1, None), height=200, pos_hint={'center_x': 0.5, 'y': 0})
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(450, 450))
        logo_layout.add_widget(self.logo)
        root.add_widget(logo_layout)

        self.add_widget(root)


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        product_screen = ProductScreen(name='product_screen')
        product_screen.build()
        sm.add_widget(product_screen)

        sm.current = 'product_screen'

        self.sm = sm
        return sm


if __name__ == '__main__':
    MainApp().run()
