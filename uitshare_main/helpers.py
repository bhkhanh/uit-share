from django.shortcuts import render
from .models import (
    Category,
    Course,
)


# Get all objects in Category table
def get_all_categories():
    return Category.objects.all()


# Get image list for carousel slide in front-end
def get_image_slides():
    image_slides = [
        "images/image-01.jpeg",
        "images/image-02.jpeg",
    ]
    return image_slides


# Get latest/newest course list
def get_newest_course_list(start_from, end_at):
    return Course.objects.order_by("-date_modified")[start_from:end_at]


# Error handling for error code 400
def handler400_bad_request(request, exception):
    context_arguments = {
        "title": "400 | Bad Request",
    }
    template_name = "errors/400.html"
    return render(request=request, template_name=template_name, context=context_arguments, status=400)


# Error handling for error code 403
def handler403_forbidden(request, exception):
    context_arguments = {
        "title": "403 | Forbidden",
    }
    template_name = "errors/403.html"
    return render(request=request, template_name=template_name, context=context_arguments, status=403)


# Error handling for error code 404
def handler404_page_not_found(request, exception):
    context_arguments = {
        "title": "404 | Not Found",
    }
    template_name = "errors/404.html"
    return render(request=request, template_name=template_name, context=context_arguments, status=404)


# Error handling for error code 500
def handler500_server_error(request):
    context_arguments = {
        "title": "500 | Server Error",
    }
    return render(request=request, template_name="errors/500.html", context=context_arguments ,status=500)