from datetime import date

from django.shortcuts import render_to_response
from django.utils.timezone import now
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Base, Post,Speciality,User,UserEducation,UserProfile
from UsingAlchemly import settings
import sqlalchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from rest_framework.decorators import api_view, renderer_classes
from main.serializers import *


# Create your views here.


engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

def createProfile(data,id):
    profile = UserProfile()
    profile.users =id
    profile.updated = date.today()
    profile.created = date.today()
    profile.license_number = data['license_number']
    profile.about = data['about']
    profile.weight = data['weight']
    profile.height=data['height']
    try:
      session.add(profile)
      session.new
      session.commit()

    except:
        session.rollback()
        raise

    finally:
        session.close()

@renderer_classes((JSONRenderer,))
@api_view(['POST'])
def createUser(request):
    profile_data = request.data.get('profile')
    print(profile_data)
    user = User()
    user.email = request.data.get('email')
    user.first_name = request.data.get('first_name')
    user.last_name = request.data.get('last_name')
    user.password = request.data.get('password')
    user.user_type = request.data.get('user_type')
    user.created = date.today()
    user.updated = date.today()
    user.last_login = now()

    try:
        session.add(user)
        session.new
        session.commit()
        profile=createProfile(profile_data, user.id)

    except:
        session.rollback()
        raise

    finally:
        session.close()

    return Response(status=status.HTTP_204_NO_CONTENT)

@renderer_classes((JSONRenderer,))
@api_view(['GET'])
def listUsers(request):

    data =session.query(User).all()
    serializer = UserSerializer(data=data,many=True)
    if serializer.is_valid():
        serializer.save()
    session.close()


def listProfs(request):

    data = session.query(UserProfile).all()
