from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherListView(APIView):
    def get(self, request):
        try:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response("Teacher not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        try:
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response("Teacher not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id, format=None):
        try:
            teacher = Teacher.objects.get(id=id)
            teacher.delete()
            return Response("Teacher deleted", status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response("Teacher not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def teacher_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response("Login successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response("Invalid request method", status=status.HTTP_400_BAD_REQUEST)


def teacher_logout(request):
    logout(request)
    return Response("Logout successful", status=status.HTTP_200_OK)


class TeacherPasswordChangeView(APIView):
    def post(self, request, id, format=None):
        try:
            teacher = Teacher.objects.get(id=id)
            password = request.data.get('password')
            teacher.password = password
            teacher.save()
            return Response("Password changed successfully", status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response("Teacher not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)