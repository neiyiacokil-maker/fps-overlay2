
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.035, 0.04, 0.05, 1)


class Kart(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 14
        self.spacing = 10

        with self.canvas.before:
            Color(0.10, 0.11, 0.12, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[18]
            )

        self.bind(pos=self.guncelle, size=self.guncelle)

    def guncelle(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class FPSApp(App):
    def build(self):
        ana = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=14
        )

        baslik = Label(
            text="[b]PUBG FPS PANEL[/b]",
            markup=True,
            font_size=27,
            color=(1, 0.78, 0.05, 1),
            size_hint_y=None,
            height=65
        )
        ana.add_widget(baslik)

        kart = Kart()
        ana.add_widget(kart)

        kart.add_widget(Label(
            text="FPS",
            font_size=20,
            color=(0.8, 0.8, 0.8, 1),
            size_hint_y=None,
            height=35
        ))

        self.fps_yazi = Label(
            text="--",
            font_size=58,
            bold=True,
            color=(1, 0.78, 0.05, 1)
        )
        kart.add_widget(self.fps_yazi)

        self.durum = Label(
            text="DURUM: HAZIR",
            font_size=16,
            color=(0.3, 1, 0.45, 1),
            size_hint_y=None,
            height=40
        )
        ana.add_widget(self.durum)

        buton = Button(
            text="ÖLÇÜMÜ BAŞLAT",
            font_size=18,
            bold=True,
            color=(0.05, 0.05, 0.05, 1),
            background_normal="",
            background_color=(1, 0.78, 0.05, 1),
            size_hint_y=None,
            height=58
        )
        buton.bind(on_press=self.baslat)
        ana.add_widget(buton)

        self.sayac = 0
        self.baslangic = 0
        return ana

    def baslat(self, *args):
        self.sayac = 0
        self.durum.text = "DURUM: PANEL ÇALIŞIYOR"
        Clock.schedule_interval(self.olc, 1)

    def olc(self, dt):
        self.sayac += 1
        self.fps_yazi.text = str(self.sayac)
        return True


if __name__ == "__main__":
    FPSApp().run()
      
