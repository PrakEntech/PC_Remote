import os,requests,webbrowser,numpy,pyautogui,cv2,ctypes
from bs4 import BeautifulSoup
from random import randint
a,b='1',''
chrome_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
while True:
        with open('live.txt','r')as fil:b=fil.read()
        r = requests.get('https://YOUR-DOMAIN.pythonanywhere.com/lvecmdrunning')
        if r.status_code == 200:soup = BeautifulSoup(r.text,'html.parser')
        for A_Tag in soup.select('span[class*="livecmd"]'):a = A_Tag.get_text()
        if a == 'music':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                loc = "C:\\Users\\USER-NAME\\Music\\Playlists"
                music = os.listdir(loc)
                os.startfile(os.path.join("C:\\Users\\USER-NAME\\Music\\Playlists", music[randint(0,len(music)-1)]))
        if a == 'null':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:continue
        if a == 'shutdown':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:os.system("shutdown /s /t 1")
        if a == 'youtube':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:webbrowser.get(chrome_path).open("www.youtube.com")
        if a == 'zoom':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:os.system('C:\\Users\\USER-NAME\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        if a == 'whatsapp':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:webbrowser.get(chrome_path).open("web.whatsapp.com")
        if a == 'screenshot':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                image = pyautogui.screenshot()
                image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                with open('data.bin','r') as file1:
                    temp = file1.read()
                file1.close()
                q = eval(temp+'+1')
                cv2.imwrite("C:\\Users\\USER-NAME\\Desktop\\SS"+str(q)+".jpg", image)
                with open('data.bin','w+') as file1:
                    file1.write(str(q))
                file1.close()
        if a == 'wallpaper':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                files = os.listdir("C:\\Users\\USER-NAME\\Pictures\\poke wall")
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\USER-NAME\\Pictures\\poke wall\\"+files[randint(0,len(files)-1)], 0)
                del files
        if a == 'volup':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                for i in range(5):
                    pyautogui.keyDown('volumeup')
                    pyautogui.keyUp('volumeup')
        if a == 'voldown':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                for i in range(5):
                    pyautogui.keyDown('volumedown')
                    pyautogui.keyUp('volumedown')
        if a == 'word':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                os.startfile(os.environ["ProgramFiles"]+'\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        if a == 'pyfile':
            with open('live.txt','w')as fil:fil.write(a)
            if b!=a:
                    with open('data2.bin','r') as file1:temp = file1.read()
                    q = eval(temp+'+1')
                    with open("C:\\Users\\USER-NAME\\Desktop\\TestFile"+str(q)+".py",'w+') as file1:
                        file1.write('')
                    file1.close()
                    with open('data2.bin','w+') as file1:file1.write(str(q))
