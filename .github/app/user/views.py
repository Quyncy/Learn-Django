from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, authentication, permissions

from .serializers import (
    UserSerializer, KursleiterSerializer, KursleiterProfileSerializer,
    DozentSerializer, TutorSerializer, TutorProfileSerializer
)
# DozentProfilSerializer

from rest_framework.authtoken.models import Token

from core.models import (
    User, Kursleiter, Dozent, Tutor, 
    KursleiterProfile, TutorProfile
    # DozentProfile, ,
)


@api_view(['GET',])
def apiOverView(request):
    api_urls = {
        'User erstellen': 'create-user/',
        'User Liste': 'list-user/',
        'User erhalten, updaten und löschen': 'detail-user/<pk>',

        'Kursleiter erstellen': 'create-kursleiter/',
        'Kursleiter Liste': 'list-kursleiter/',
        'Kursleiter erhalten, updaten und löschen': 'detail-kursleiter/<pk>',

        'Dozent erstellen': 'create-dozent/',
        'Dozent Liste': 'list-dozent/',
        'Dozent erhalten, updaten und löschen': 'detail-dozent/<pk>',
    }
    return Response(api_urls)


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

#####################################

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes=[]


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes=[]


class UserDetailView(APIView):

    def get(self, request, pk):
        user = get_user_model().objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_user_model().objects.get(pk=pk)
        serializer = UserSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk):
        user = get_user_model().objects.get(pk=pk)
        user.delete()
        return Response("User wurde erfolgreich gelöscht.")


###################################


# class TutorView(generics.ListAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         user = User.objects.filter(is_tutor=True)
#         print(user)
#         return user







class CreateKursleiterView(generics.CreateAPIView):
    # KursleiterProfile
    serializer_class = KursleiterSerializer
    permission_classes = []


class KursleiterListView(generics.ListAPIView):
    # KursleiterProfile
    queryset = Kursleiter.objects.all()
    serializer_class = KursleiterSerializer


class KursleiterDetailView(APIView):

    def get(self, request, pk):
        user = Kursleiter.objects.get(pk=pk)
        serializer = KursleiterSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = Kursleiter.objects.get(pk=pk)
        serializer = KursleiterSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk):
        user = Kursleiter.objects.get(pk=pk)
        user.delete()
        return Response("Kursleiter wurde erfolgreich gelöscht.")


########


class CreateKursleiterProfileView(generics.CreateAPIView):
    serializer_class = KursleiterProfileSerializer
    permission_classes=[]


class KursleiterProfileListView(generics.ListAPIView):
    queryset = KursleiterProfile.objects.all()
    serializer_class = KursleiterSerializer




#################################################




class CreateTutorView(generics.CreateAPIView):
    serializer_class = TutorSerializer
    permission_classes = []


class TutorListView(generics.ListAPIView):
    # TutorProfile
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = []


class TutorDetailView(APIView):

    def get(self, request, pk):
        user = Tutor.objects.get(pk=pk)
        serializer = TutorSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = Tutor.objects.get(pk=pk)
        serializer = TutorSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk):
        user = Tutor.objects.get(pk=pk)
        user.delete()
        return Response("Tutor wurde erfolgreich gelöscht.")


##############
class TutorProfileView(generics.CreateAPIView):
    serializer_class = TutorProfileSerializer
    permission_classes=[]


class TutorProfileListView(generics.ListAPIView):
    queryset = TutorProfile.objects.all()
    serializer_class = TutorProfileSerializer
    permission_classes = []





#################################################




class CreateDozentView(generics.CreateAPIView):
    serializer_class = DozentSerializer
    permission_classes = []


class DozentListView(generics.ListAPIView):
    queryset = Dozent.objects.all()
    serializer_class = DozentSerializer


class DozentDetailView(APIView):

    def get(self, request, pk):
        user = Dozent.objects.get(pk=pk)
        serializer = DozentSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = Dozent.objects.get(pk=pk)
        serializer = DozentSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk):
        user = Dozent.objects.get(pk=pk)
        user.delete()
        return Response("Dozent wurde erfolgreich gelöscht.")





##################################################


@api_view(['POST'])
# @permission_classes([AdminPerm]) # eigtl hätte ich hier die Recht haben müssen
def register_view(request):
    data = {}
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            data['response'] = "Registierung erfolgreich"
            data['email'] = user.email
            data['vorname'] = user.vorname
            data['nachname'] = user.nachname

            token = Token.objects.get(user=user).key

            data['token'] = token
            print(token)

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response("Token wurde nicht gelöscht.")