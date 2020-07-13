from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Animal, Lot, Bid
from .serializers import AnimalSerializer, LotSerializer, BidSerializer, UserSerializer, BidAcceptSerializer
from django.contrib.auth import get_user_model

class AnimalView(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class LotView(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class BidView(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer    

class UserView(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class BidAcceptView(APIView):
    serializer_class = BidAcceptSerializer

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Bid.bid_accept(self, pk=pk)
            return Response({'success': "deal successfully"})
        else:
            return Response(serializer.errors)
