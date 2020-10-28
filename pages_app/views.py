from django.shortcuts import render
from pages_app.models import Page

# Create your views here.
def page(request, slug):
    page = Page.objects.get(slug = slug, visible = True)
    return render(request, 'pages_app/page.html', {'page': page})