
import cgi
from botendine import make_reply

form = cgi.FieldStorage()

def main():
    m = form.getvalue("m", default="")
    if m == "" : show_form()
    elif m == "say" : api_say()

def api_say():
    print("Content-Type: text/plain; charset=utf-8")
    print("")
    txt= form.getvalue("txt", default="")
    if txt =="": return
    res = make_reply(txt)
    print(res)

def show_form():
    print("Content-Type: text/html; charset=utf-8")
