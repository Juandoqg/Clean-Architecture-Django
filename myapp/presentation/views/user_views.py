from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework import serializers

from myapp.infrastructure.repositories.user_repository import UserRepository
from myapp.application.use_cases.create_user import CreateUser

# Serializer para validar los datos de entrada
class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

@extend_schema(
    summary="Crear un usuario",
    description="Este endpoint permite crear un nuevo usuario en la base de datos.",
    request=CreateUserSerializer,
    responses={201: {"message": "Usuario creado exitosamente"}, 400: {"error": "Datos inválidos"}}
)
@api_view(['POST'])
def create_user_view(request):
    serializer = CreateUserSerializer(data=request.data)
    
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']

        repository = UserRepository()
        use_case = CreateUser(repository)

        try:
            use_case.execute(name=name, email=email)
            return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista GET para renderizar el formulario (opcional, no aparecerá en Swagger)
def create_user_form_view(request):
    return render(request, "create_user.html")
