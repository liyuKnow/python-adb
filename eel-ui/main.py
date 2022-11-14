import eel

# Set web files folder
eel.init('web')


@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('hello.html', size=(300, 200))  # Start


# import eel
# import subprocess

# # name of folder where the html, css, js, image files are located
# eel.init('templates')


# # Exposing the random_python function to javascript
# @eel.expose
# def pull_file():
#     pull_command = "adb devices"
#     print("WOW Pulling")
#     return subprocess.call(pull_command, shell=True)


# @eel.expose
# def push_file():
#     pull_command = "adb devices"
#     print("WOW Pushing")
#     return subprocess.call(pull_command, shell=True)


# # 1000 is width of window and 600 is the height
# eel.start('index.html', size=(1000, 600))
