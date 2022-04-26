from django.views.generic import TemplateView

# home page view is exstending TemplateView 
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'    