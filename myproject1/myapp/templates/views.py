from django.shortcuts import render

def home(request):

    students = [
        {
            "name": "Sandhya",
            "roll": 101,
            "course": "CSE",
            "cgpa": 8.9
        },
        {
            "name": "Rahul",
            "roll": 102,
            "course": "IT",
            "cgpa": 8.2
        },
        {
            "name": "Priya",
            "roll": 103,
            "course": "CSE",
            "cgpa": 9.1
        },
        {
            "name": "Aman",
            "roll": 104,
            "course": "ECE",
            "cgpa": 7.8
        }
    ]

    return render(request, "myapp/home.html", {"students": students})