from django.views.generic import TemplateView

'''
Also known as class based views in django.
there are basic classes that can take advantage of these views inherited from TemplateView
which can be called in urls.py

'''
class HOMEPAGE(TemplateView):
    template_name = 'index.html'