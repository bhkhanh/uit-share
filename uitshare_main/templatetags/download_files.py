from django import template

register = template.Library()

@register.filter(name="download_url")
def download_url(url_path):
    return url_path.upper()