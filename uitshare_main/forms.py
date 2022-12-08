from django import forms
from .models import (
    Category,
    Course,
    File,
)


# ============================================================
# ============================================================

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        help_texts = {
            "name": "Human-readable title for Category.",
            "code_name": "This field is generally used for URLs (such as \"hello-world\" in www.example.com/hello-world/).",
            "date_created": "Date and time this category is being created.",
            "date_modified": "Automatically this field will be set to NOW every time the object is saved.",
            "thumbnail_img": "Background cover image for Category object.",
        }
        error_messages = {
            "name": {
                "required": "Category title is required, please enter a title for it.",
            },
            "codename": {
                "required": "Category code-name is required, this cannot be blank.",
            },
        }

# ============================================================

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        help_texts = {
            "name": "Human-readable title for Course.",
            "code_name": "This field is generally used for URLs (such as \"hello-world\" in www.example.com/hello-world/).",
            "date_created": "Date and time this course is being created.",
            "date_modified": "Automatically this field will be set to NOW every time the object is saved.",
            "category_id": "Category that this course will belong to.",
            "by_user": "This category is created/modified by which user.",
            "thumbnail_img": "Background cover image for Course object.",
        }
        error_messages = {
            "name": {
                "required": "Course title is required, please enter a title for it.",
            },
            "code_name": {
                "required": "Course code-name is required, this cannot be blank."
            },
            "category_id": {
                "required": "Category is required, please choose which category this course belong to.",
            },
        }

# ============================================================

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"
        help_texts = {
            "name": "Human-readable title for File.",
            "date_created": "Date and time this file is being created.",
            "date_modified": "Automatically this field will be set to NOW every time the object is saved.",
            "course_id": "Course that this file will belong to.",
            "uploaded_by": "This file is uploaded by which user.",
            "file_uploaded": "Choose file or document that you want to upload.",
            "file_type": "File type such as Lectures, Labs, Exercises, Exams, Books,...",
        }
        error_messages = {
            "course_id": {
                "required": "Course is required, please choose which course this file belong to.",
            },
            "file_uploaded": {
                "required": "You have to upload file, this is required.",
            },
        }
