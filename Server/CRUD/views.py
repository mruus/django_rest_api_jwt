from rest_framework.response import Response
from rest_framework.decorators import api_view
from CRUD import models
from . import serializers
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST', 'GET'])
def CRUD_NOID(request):

    # Public variable
    resposne = ''

    if request.method == "POST":

        # Fetch the data from the request
        namePost = request.POST.get('Name')
        emailPost = request.POST.get('Email')
        phonePost = request.POST.get('Phone')
        usernamePost = request.POST.get('Username')
        passwordPost = request.POST.get('Password')

        # Check If There Is Account With This Fields

        try:
            userEmail = models.Accounts.objects.get(Email=emailPost)
            # Instance of resposne
            response = Response()

            data = {
                'isError': True,
                'Message': "Email Already Exists"
            }

            response.data = data

        except ObjectDoesNotExist:

            try:
                userUsername = models.Accounts.objects.get(
                    Username=usernamePost)
                # Instance of resposne
                response = Response()

                data = {
                    'isError': True,
                    'Message': "Username Already Exists"
                }

                response.data = data

            except ObjectDoesNotExist:
                # Add the data to the database
                serializeData = serializers.AccountSerializer(
                    data=request.data)

                if serializeData.is_valid():
                    serializeData.save()

                    # Instance of resposne
                    response = Response()

                    data = {
                        'isError': False,
                        'Message': "Account Has Been Created"
                    }

                    response.data = data

    elif request.method == 'GET':
        users = models.Accounts.objects.all()
        serializeData = serializers.AccountSerializer(users, many=True)

        response = Response()

        data = {
            'isError': False,
            'Message': serializeData.data
        }

        response.data = data

    return response


@api_view(['GET', 'PUT', 'DELETE'])
def CRUD_ID(request, pk):

    # Get Request
    if request.method == 'GET':
        try:
            user = models.Accounts.objects.get(id=pk)
            serializeData = serializers.AccountSerializer(user)

            response = Response()

            data = {
                'isError': False,
                'Message': serializeData.data
            }

            response.data = data

        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': False,
                'Message': "This Username Does Not Exist"
            }

            response.data = data

    if request.method == 'DELETE':
        try:
            user = models.Accounts.objects.get(id=pk)
            user.delete()

            response = Response()

            data = {
                'isError': False,
                'Message': "User Has Been Deleted"
            }

            response.data = data

        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': False,
                'Message': "This Username Does Not Exist"
            }

            response.data = data

    if request.method == 'PUT':
        try:
            user = models.Accounts.objects.get(id=pk)
            serializeData = serializers.AccountSerializer(user, request.data)

            if serializeData.is_valid():
                serializeData.save()

                # Instance of resposne
                response = Response()

                data = {
                    'isError': False,
                    'Message': "Account Has Been Updated"
                }

                response.data = data
        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': False,
                'Message': "This Username Does Not Exist"
            }

            response.data = data


    return response
