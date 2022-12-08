from django.urls import path
from .views import SearchView



urlpatterns = [
    path(route="", view=SearchView.as_view(), name="search-page"),
]