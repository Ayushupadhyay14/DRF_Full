from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from .models import Account
from rest_framework.response import Response

# Create your views here.


class AccountList(APIView):
    def get(self, request):
        Accounts = Account.objects.all()
        serializer = AccountSerializer(Accounts, many=True)
        return Response(serializer.data, 'rest_framework/api.html')
