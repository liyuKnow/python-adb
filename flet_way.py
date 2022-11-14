import flet
from flet import Page, Text, Slider, View, AppBar


# def main(page: Page):
#     page.add(Text("Hello, world!"))


def main(home_screen: View):
    home_screen.appbar = AppBar(leading=Text("Hello, world!"))
    home_screen.add(Slider(width=10, height=4))


if __name__ == "__main__":
    flet.app(target=main)
