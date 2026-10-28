# from django.urls import path
# from . import views

# urlpatterns=[
#     path("", views.home, name="home"),
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns=[
#     path("admin/", admin.site.urls),
#     path("", include("main.urls")),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.home),
# ]









from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
]

