from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def input_data():
    return render_template('zxc.html')

@app.route("/playmusic")
def input_data1():
    with open('live.txt','w')as fil:fil.write('music')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")

@app.route("/shutdown")
def input_data2():
    with open('live.txt','w')as fil:fil.write('shutdown')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")

@app.route("/openyt")
def input_data3():
    with open('live.txt','w')as fil:fil.write('youtube')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")

@app.route("/openzoom")
def input_data4():
    with open('live.txt','w')as fil:fil.write('zoom')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")

@app.route("/whatsapp")
def input_data5():
    with open('live.txt','w')as fil:fil.write('whatsapp')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/takess")
def input_data6():
    with open('live.txt','w')as fil:fil.write('screenshot')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/wallpaper")
def input_data7():
    with open('live.txt','w')as fil:fil.write('wallpaper')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")

@app.route("/volup")
def input_data9():
    with open('live.txt','w')as fil:fil.write('volup')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/voldown")
def input_data10():
    with open('live.txt','w')as fil:fil.write('voldown')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/null")
def input_data11():
    with open('live.txt','w')as fil:fil.write('null')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/word")
def input_data908():
    with open('live.txt','w')as fil:fil.write('word')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/pyfile")
def input_data12():
    with open('live.txt','w')as fil:fil.write('pyfile')
    return redirect("https://YOUR-DOMAIN.pythonanywhere.com/")
@app.route("/lvecmdrunning")
def input_data8():
    with open('live.txt','r')as fil:a=fil.read()
    return render_template('livecmd.html', cmdON=a)
if __name__=="__main__":
    app.run()
