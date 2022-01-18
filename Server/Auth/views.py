from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from Auth.models import AuthUsers


@api_view(['POST'])
def AuthLogin(request):
    if request.method == 'POST':
        emailPost = request.POST.get('email')
        passwordPost = request.POST.get('password')

        try:
            user = AuthUsers.objects.get(
                email=emailPost, password=passwordPost)
            serializeData = serializers.AuthUsersSerializer(user)
            data = {
                'Error': False,
                'Data': serializeData.data
            }
            return Response(data)

        except AuthUsers.DoesNotExist:
            data = {
                'Error': True,
                'Data': "User Does Not Exist"
            }
            return Response(data)


@api_view(['POST'])
def AuthRegister(request):
    if request.method == 'POST':
        namePost = request.POST.get('name')
        emailPost = request.POST.get('email')
        passwordPost = request.POST.get('password')

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
