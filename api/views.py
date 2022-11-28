from rest_framework.response import Response
from rest_framework.views import APIView
from .transposer import transposer
from .serializers import MatSerializer
from Matapp.funcs import transpose as tr
#from drf_spectacular.utils import extend_schema

class transposerView(APIView):
#    @extend_schema(command=MatSerializer, responses=MatSerializer)
    def get(self, command, cols, rows, args):
        transpose = transposer(cols, rows, args, tr(cols, rows, args))
        ser = MatSerializer(instance=transpose)
        return Response(ser.data)