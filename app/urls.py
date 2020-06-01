# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('users', views.AuthUserView)

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),



]

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include("authentication.urls")),  # add this
#     path("", include("app.urls"))  # add this
# ]