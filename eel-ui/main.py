import eel

eel.init('web')


@eel.expose
def greet_html():
    return "Hello Js"


eel.start("index.html")
