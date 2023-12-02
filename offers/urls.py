# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = "offers"

urlpatterns = [
    # Create a task
    path("create/", views.offer_create, name="offer_create"),
    # Retrieve task list
    # path("", views.OfferListView.as_view(), name="task_list"),
    path("", views.homepage, name="homepage"),
    path("list/", views.offer_list, name="offer_list"),
    # Retrieve single task object
    re_path(r"^offers/list/(?P<pk>\d+)/$", views.offer_detail, name="offer_detail"),
    # Update a task
    re_path(
        r"^offers/list/(?P<pk>\d+)/update/$",
        views.offer_update,
        name="offer_update",
    ),
    # Delete a task
    re_path(
        r"^offers/list/(?P<pk>\d+)/delete/$",
        views.offer_delete,
        name="offer_delete",
    )




    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]

