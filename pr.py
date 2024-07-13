
import eel
import pyautogui #https://pypi.org/project/PyAutoGUI/
  
eel.init('views')
     
@eel.expose
def new_window(target: str):
   eel.show(f"html/{target}")
     
eel.start(
    'templates/base.html',mode='default',
    size=pyautogui.size(),
)
