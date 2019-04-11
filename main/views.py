from django.shortcuts import render_to_response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Base, Post,Speciality,User,UserEducation,UserProfile
from alchemlyProject import settings
import sqlalchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from rest_framework.decorators import api_view, renderer_classes
from main.serializers import *


# Create your views here.


engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

@api_view(['GET'])

def createUser(request):

        u1 = User(
            first_name= "nesreen",
            last_name = "massimi",
            email = "nmosimi@gmail.com",
            password="12345",)

        session.add(u1)
        session.new
        session.commit()
        return Response(status=status.HTTP_204_NO_CONTENT)

@renderer_classes((JSONRenderer,))
@api_view(['GET'])
def listUsers(request):
    data =session.query(User).all()
    serializer = UserSerializer(data=data,many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data,status=status.HTTP_200_OK)


