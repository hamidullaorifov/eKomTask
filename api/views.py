from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_form,get_input_type




class GetFormView(APIView):
    def post(self,request,format=None):
        data = request.data
        query = {}
        for field in data:
            field_type = get_input_type(data[field])
            query[field] = field_type
        form = get_form(query)
        if form:
            return Response(form['name'])
        return Response(query)

