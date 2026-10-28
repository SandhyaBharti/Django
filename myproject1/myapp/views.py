# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello! Welcome to Django")



from django.shortcuts import render


def home(request):

    name = "Sandhya"
    age = 21
    course = "B.Tech CSE"
    college = "LPU"
    cgpa = 8.9

    return render(request, "myapp/home.html", {
        "name": name,
        "age": age,
        "course": course,
        "college": college,
        "cgpa": cgpa
    })