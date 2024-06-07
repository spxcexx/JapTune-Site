"""
URL configuration for japtune project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from japtuneapp.views import main
from partnersapp.views import partners
from registrationapp.views import registration, login_user, logout_user, show_successful_login
from markschoiceapp.views import *
from toyota.views import toyota_view
from subaru.views import subaru_view
from nissan.views import nissan_view
from mazda.views import mazda_view
from honda.views import honda_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('partners/', partners, name='partners'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout_user"),
    path('choice/', main_choice, name='choice'),
    path('successful_login/', show_successful_login, name='successful_login'),
    path('toyota/', toyota_view, name = "toyota"),
    path('subaru/', subaru_view, name = "subaru"),
    path('nissan/', nissan_view, name = "nissan"),
    path('mazda/', mazda_view, name = "mazda"),
    path('honda/', honda_view, name = "honda"),
]
