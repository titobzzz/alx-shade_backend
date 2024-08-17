from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'',views.BallotViewSet,basename="Ballots"),


urlpatterns =[
    path('ballots/',views.BallotViewSet.as_view({"get":"list","post":"create"}),name="Ballots"),
    path('ballots/<str:pk>/',views.BallotViewSet.as_view({"get":"retrieve","patch":"update","delete":"delete"}),name="Ballots"),    
    path('ballots/<str:ballot_id>/comments/',views.CommentViewSet.as_view({"get":"list","post":"create"}),name="comments"),
    path('ballots/<str:ballot_id>/comments/<str:pk>/',views.CommentViewSet.as_view({"get":"retrieve","patch":"update","delete":"delete"}),name="retrive-comments"),
    path('ballots/<str:ballot_id>/polls/',views.PollsViewSet.as_view({"get":"list","post":"create"}), name="polls"),
    path('ballots/<str:ballot_id>/polls/<str:pk>/',views.PollsViewSet.as_view({"get":"retrieve","patch":"update","delete":"delete"}),name="polls")
]