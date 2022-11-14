import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

# ^ APPLICATION
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Report app")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_top = customtkinter.CTkFrame(
            master=self, corner_radius=10, height=300, width=400
        )

        self.frame_top.grid(row=1, column=0, sticky="nswe")

        self.frame_bottom = customtkinter.CTkFrame(
            master=self, corner_radius=10, height=300, width=400, bg_color="green"
        )
        self.frame_bottom.grid(row=2, column=0, sticky="nswe")

        # ============ frame_top ============

        # configure grid layout (1x11)
        self.frame_top.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing

        self.frame_top.grid_rowconfigure(3, weight=1)  # empty row as spacing
        self.frame_top.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_top.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_top,
            text="CustomTkinter",
            text_font=("Roboto Medium", -16),
        )  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(
            master=self.frame_top, text="Export File", command=self.push_button_event
        )
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

    def pull_button_event(self):
        pull_command = "adb pull /storage/emulated/0/Download/usersDownload.xlsx C:/Users/Liyu/Desktop"
        subprocess.call(pull_command, shell=True)
        print("Success")

    def push_button_event(self):
        pull_command = (
            "adb push C:/Users/Liyu/Desktop/VeryNew.xlsx /storage/emulated/0/Download/"
        )
        subprocess.call(pull_command, shell=True)
        print("Success")

    #     def change_appearance_mode(self, new_appearance_mode):
    #         customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
