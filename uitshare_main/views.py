from django.shortcuts import render
from .models import (
    Category,
    Course,
)
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from .helpers import (
    get_all_categories,
    get_image_slides,
    get_newest_course_list,
)


# ============================================================
# ============================================================

class HomeView(TemplateView):
    template_name = "main/index.html"
    extra_context = {
        "title": "UIT Share",
        "category_list": get_all_categories,
        "image_slides": get_image_slides,
        "newest_course_list": get_newest_course_list(0, 16),
    }

# ============================================================
# ============================================================

class CategoryListView(ListView):
    template_name = "main/category-list.html"
    extra_context = {
        "title": "Category / UIT Share",
    }
    model = Category
    context_object_name = "category_list"


class CategoryDetailView(DetailView):
    template_name = "main/category-detail.html"
    model = Category
    context_object_name = "category_detail"
    slug_url_kwarg = "category_codename"
    slug_field = "code_name"

    def get_context_data(self, **kwargs):
        context_arguments = super().get_context_data(**kwargs)
        context_arguments["title"] = self.get_object().name + " / UIT Share"
        context_arguments["category_list"] = get_all_categories
        context_arguments["course_list"] = self.get_object().courses.all()  # using related_name
        return context_arguments

# ============================================================
# ============================================================

class CourseListView(ListView):
    template_name = "main/course-list.html"
    extra_context = {
        "title": "Course / UIT Share",
        "category_list": get_all_categories,
    }
    model = Course
    context_object_name = "course_list"


class CourseDetailView(DetailView):
    template_name = "main/course-detail.html"
    model = Course
    context_object_name = "course_detail"
    slug_url_kwarg = "course_codename"
    slug_field = "code_name"

    def get_context_data(self, **kwargs):
        context_arguments = super().get_context_data(**kwargs)
        context_arguments["title"] = self.get_object().name + " / UIT Share"
        context_arguments["category_list"] = get_all_categories
        context_arguments["lecture_list"] = self.get_object().files.filter(file_type="Lecture")     # using related_name
        context_arguments["lab_list"] = self.get_object().files.filter(file_type="Lab")             # using related_name
        context_arguments["exercise_list"] = self.get_object().files.filter(file_type="Exercise")   # using related_name
        context_arguments["exam_list"] = self.get_object().files.filter(file_type="Exam")           # using related_name
        context_arguments["book_list"] = self.get_object().files.filter(file_type="Book")           # using related_name
        context_arguments["other_list"] = self.get_object().files.filter(file_type="Other")         # using related_name
        return context_arguments

# ============================================================
# ============================================================

class AboutUsView(TemplateView):
    template_name = "main/about.html"
    extra_context = {
        "title": "About / UIT Share",
        "category_list": get_all_categories,
    }