from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from Auth.models import AuthUsers
import jwt
import datetime


@api_view(['POST'])
def AuthLogin(request):
    if request.method == 'POST':
        emailPost = request.POST.get('email')
        passwordPost = request.POST.get('password')

        user = AuthUsers.objects.get(
            email=emailPost, password=passwordPost)

        if user is not None:
            serializeData = serializers.AuthUsersSerializer(user)

            # init token
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            # instance of Response
            response = Response()

            # set cookie for the token
            response.set_cookie(key='TokenKey', value=token)

            response.data = {
                'Error': False,
                'Data': serializeData.data,
                'Token': token
            }
            return response

        data = {
            'Error': True,
            'Data': "User Does Not Exist"
        }
        return Response(data)


@api_view(['POST'])
def AuthRegister(request):
    if request.method == 'POST':
        serializeData = serializers.AuthUsersSerializer(data=request.data)

        if serializeData.is_valid():
            serializeData.save()
            data = {
                'Error': False,
                'Data': serializeData.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = {
            'Error': True,
            'Data': serializeData.errors['email'][0],
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetToken(request):
    if request.method == "GET":
        # fetch cookie
        tokenCookie = request.COOKIES.get('TokenKey')
    
        if tokenCookie is not None:
            tokenDecode = jwt.decode(
                tokenCookie, "secret", algorithms=["HS256"])

            return Response({
                'Error': False,
                'Token': tokenCookie,
                'Data': tokenDecode
            })
        else:
            return Response({
                'Error': True,
                'Token': '',
                'Data': ''
            })


@api_view(['GET'])
def AuthLogout(request):
    response = Response()

    response.delete_cookie('TokenKey')

    response.data = {
        'Error': False,
        'Data':  'Cookie Has Been Destroyed'
    }

    return response

# @api_view(['GET', 'POST'])
# def AuthUser_(request):
#     if request.method == 'GET':
#         users = AuthUsers.objects.all()
#         serializeData = serializers.AuthUsersSerializer(users, many=True)
#         data = {
#             'Error': False,
#             'Data': serializeData.data
#         }
#         return Response(data)

#     elif request.method == 'POST':
#         serializeData = serializers.AuthUsersSerializer(data=request.data)

#         if serializeData.is_valid():
#             serializeData.save()
#             data = {
#                 'Error': False,
#                 'Data': serializeData.data
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         data = {
#             'Error': True,
#             'Data': [],
#         }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def AuthUser__(request, pk):
#     try:
#         user = AuthUsers.objects.get(id=pk)
#     except AuthUsers.DoesNotExist:
#         data = {
#             'Error': True,
#             'Data': []
#         }
#         return Response(data, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializeData = serializers.AuthUsersSerializer(user, many=False)
#         data = {
#             'Error': False,
#             'Data': serializeData.data
#         }
#         return Response(data)

#     elif request.method == 'PUT':
#         serializeData = serializers.AuthUsersSerializer(
#             user, data=request.data)

#         if serializeData.is_valid():
#             serializeData.save()
#             data = {
#                 'Error': False,
#                 'Data': serializeData.data
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         data = {
#             'Error': True,
#             'Data': [],
#         }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         data = {
#             'Error': False,
#             'Data': "User Deleted",
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)
