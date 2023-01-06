from rest_framework.views import APIView
from rest_framework.response import Response
from tinydb import TinyDB,Query
import re
from datetime import datetime
db = TinyDB('db.json')


def define_input_type(text):
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
        return 'telephone'
    return 'text'
class GetFormView(APIView):
    def post(self,request,format=None):
        Forms = Query()
        data = request.data
        query = {}
        for field in data:
            field_type = define_input_type(data[field])
            query[field] = field_type
        forms = db.search(Forms.fragment(query))
        if forms:
            data = [f['name'] for f in forms]
            return Response(data)
        return Response(query)

# regex = {
#             'email':'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',
#             'date':'(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})',
#             'telephone':'/(^8|7|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))/',
#             'text':'(.*?)'
#         }