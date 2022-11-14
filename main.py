import tkinter as tk
import subprocess

from ppadb.client import Client as AdbClient


def main():
    window = tk.Tk()

    def testPurePyADB():
        pass
        # apk_path = "example.apk"

        # Default is "127.0.0.1" and 5037
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()

        for device in devices:
            print(device)
        # device.install(apk_path)
        # # Check apk is installed
        # for device in devices:
        #     print(device.is_installed("example.package"))

        # Uninstall
        # for device in devices:
        #     device.uninstall("example.package")

    def sendCallBack():
        # ADB COMMANDS HERE
        pull_command = "adb devices"
        subprocess.call(pull_command, shell=True)
        print("Success")

    def getCallBack():
        # ADB COMMANDS HERE
        pull_command = "adb devices"
        subprocess.call(pull_command, shell=True)
        print("WOW")

    sendBTN = tk.Button(window, text="Send File", command=sendCallBack)
    ImportBTN = tk.Button(window, text="Import File", command=testPurePyADB)

    sendBTN.pack()
    ImportBTN.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
