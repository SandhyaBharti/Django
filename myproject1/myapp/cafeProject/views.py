from django.shortcuts import render


def home(request):

    cafe_name = "Brew & Bite Café"
    tagline = "Fresh Coffee • Delicious Food • Cozy Vibes"

    return render(request, "myapp/home.html", {
        "cafe_name": cafe_name,
        "tagline": tagline
    })