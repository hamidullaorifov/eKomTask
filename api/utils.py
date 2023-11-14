from datetime import datetime
import re
from tinydb import TinyDB,Query

db = TinyDB('db.json')



def get_input_type(text):
    if re.match('[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',text):
        return 'email'
    try:
        date = datetime.strptime(text,'%d.%m.%Y')
        if date:
            return 'date'
    except:
        pass
    try:
        date = datetime.strptime(text,'%Y-%m-%d')
        if date:
            return 'date'
    except:
        pass
    phone = text.replace(' ','')
    if len(phone)==12 and phone.startswith('+7') and phone[1:].isdigit():
        return 'phone'
    return 'text'

def get_form(query):
    Forms = Query()
    form = db.get(Forms.fragment(query))
    return form