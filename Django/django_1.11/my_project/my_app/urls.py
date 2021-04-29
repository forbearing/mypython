#!/usr/bin/env python3
from django.urls import path
import views

urlpatterns = [
    path('^$', views.index)
]
