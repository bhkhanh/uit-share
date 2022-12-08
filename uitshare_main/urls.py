from django.urls import path
from .views import (
    HomeView,
    AboutUsView,
    CategoryListView,
    CategoryDetailView,
    CourseListView,
    CourseDetailView,
)


urlpatterns = [
    path(route="", view=HomeView.as_view(), name="home-page"),
    path(route="about/", view=AboutUsView.as_view(), name="about-page"),
    path(route="category/", view=CategoryListView.as_view(), name="category-list-page"),
    path(route="category/<slug:category_codename>/", view=CategoryDetailView.as_view(), name="category-detail-page"),
    path(route="course/", view=CourseListView.as_view(), name="course-list-page"),
    path(route="course/<slug:course_codename>/", view=CourseDetailView.as_view(), name="course-detail-page"),
]