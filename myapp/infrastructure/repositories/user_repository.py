from myapp.infrastructure.models import User  # Asegúrate de importar el modelo correcto

class UserRepository:
    def save(self, user):
        # Asegúrate de que `user` sea una instancia del modelo User
        user_instance = User(name=user.name, email=user.email)
        user_instance.save()  # Guarda el objeto en la base de datos
