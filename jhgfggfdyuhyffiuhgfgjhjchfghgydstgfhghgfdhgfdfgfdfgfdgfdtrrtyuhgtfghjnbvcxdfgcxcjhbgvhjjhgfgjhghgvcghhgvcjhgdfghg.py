def launch_app(app_name):
    apps = {
        "roblox": "launching boblox...",
        "blender": "epicly starting Blender...",
        "vscode": "opening epicly vscode...",
    }
    print(apps.get(app_name.lower(), "app not found lil bro try harder"))
a=input("put the name of your app here")
launch_app(a)