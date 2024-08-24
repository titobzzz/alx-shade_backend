from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'',views.TabViewSet,basename="Tabs"),


urlpatterns =[
    path('tabs/',views.TabViewSet.as_view({"get":"list","post":"perform_create"}),name="Tabs"),
    path('tabs/<str:pk>/', views.TabViewSet.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"}), name="Tab"),  
    path('tabs/<str:tab_id>/comments/',views.CommentViewSet.as_view({"get":"list","post":"create"}),name="comments"),
    path('tabs/<str:tab_id>/comments/<str:pk>/',views.CommentViewSet.as_view({"get":"retrieve","patch":"update","delete":"delete"}),name="retrive-comments"),
    path('tabs/<str:tab_id>/polls/',views.PollsViewSet.as_view({"get":"list","post":"create"}), name="polls"),
    path('tabs/<str:tab_id>/polls/<str:pk>/',views.PollsViewSet.as_view({"get":"retrieve","patch":"update","delete":"delete"}),name="poll")
]