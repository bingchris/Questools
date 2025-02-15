from sys import version as sysdotversion, platform as sysdotplatform
from shutil import which
from subprocess import check_output
from os import system, path
from time import time
try: from yaml import safe_load as yamlload, YAMLError
except ImportError: print("Install pyyaml from pip to use qtt"); exit(1)
endl = "\n"
class qtt: 
    contributors = ["Tarvey"]
    def get_devices(): return check_output("adb devices", shell=True).decode("utf-8").strip()
    def set_oculus_property(key, value): system(f"adb shell setprop debug.oculus.{key} {value}")
    def set_app_property(app, key, value): system(f"adb shell setprop {app}.{key} {value}")
    def get_oculus_property(key): return check_output(f"adb shell getprop debug.oculus.{key}", shell=True).decode("utf-8").strip()
    def get_app_property(app, key): return check_output(f"adb shell getprop {app}.{key}", shell=True).decode("utf-8").strip()
    def search_packages(search): return check_output("adb shell pm list packages", shell=True).decode("utf-8").strip().find(search)
    def show_app_location(app): return check_output(f"adb shell pm path {app}", shell=True).decode("utf-8").strip()
    def save_apk(location): return check_output(f"adb pull {location} ", shell=True).decode("utf-8").strip()
    def auto_apk(app):
        apkpath = check_output(f"adb shell pm path {app}", shell=True).decode("utf-8").strip()
        apkpath = apkpath.split(":")[1]
        check_output(f"adb pull {apkpath} {app}{round(time())}.apk", shell=True).decode("utf-8").strip()
    version = "Release 2.0"
    def __init__(self):
        print(f"Questools {self.version}", endl,
              "This project wouldn't be possible without:")
        for i in qtt.contributors: print(f"- {i}")
        print(qtt.get_devices())
        

if which("adb") is None: print("Install adb from the Android SDK/your package manager to use qtt"); exit(1)
qtt()