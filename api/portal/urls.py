from django.urls import path
from . import portal_views

urlpatterns = [
    # path('add', portal_views.AddPortal.as_view()),
    path('profile/karma', portal_views.GetKarma.as_view()),   

]
