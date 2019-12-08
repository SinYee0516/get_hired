from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from app import models
from .models import User, Job, Company, Status, Saved, Message
from .serializers import UserSerializer, JobSerializer, CompanySerializer, StatusSerializer, SavedSerializer, \
    MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class UserList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    models_name = User

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



'''class SignUpView(TemplateView):
    template_name = "user/"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user/:user/')
        args = {'form': form}
        return render(request.POST, self.template_name, args)
'''
