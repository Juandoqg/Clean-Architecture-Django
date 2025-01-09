from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.infrastructure.repositories.user_repository import UserRepository
from myapp.application.use_cases.create_user import CreateUser

def create_user_view(request):
    if request.method == "GET":
        # Renderizar el formulario HTML
        return render(request, "create_user.html")

    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if not name or not email:
            return JsonResponse({"error": "Name and email are required"}, status=400)

        repository = UserRepository()
        use_case = CreateUser(repository)

        try:
            use_case.execute(name=name, email=email)
            return redirect('success_page')  # Redirige a una página de éxito
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)
