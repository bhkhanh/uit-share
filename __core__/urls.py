"""__core__ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path(route="administration/", view=admin.site.urls),
    path(route="", view=include("uitshare_main.urls")),
    path(route="", view=include("uitshare_user.urls")),
    path(route="search/", view=include("uitshare_search.urls")),
]


# Customize Admin page:
admin.AdminSite.site_header = "UIT Share"
admin.AdminSite.site_title = "UIT Share"
admin.AdminSite.index_title = "Administration"

# Error Handlers
handler400 = "uitshare_main.helpers.handler400_bad_request"
handler403 = "uitshare_main.helpers.handler403_forbidden"
handler404 = "uitshare_main.helpers.handler404_page_not_found"
handler500 = "uitshare_main.helpers.handler500_server_error"

