from django.urls import path
from App import views

urlpatterns = [
    path("total/",views.TotalAmt.as_view()),
    path("data/",views.Productget.as_view()),
    path("getcart/",views.ApiStatus.as_view()),
    path("task/",views.CartAdd.as_view()),
    path("update/",views.Update.as_view()),
    path("remove/",views.Remove.as_view())

]