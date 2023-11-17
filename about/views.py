from django.views.generic.base import TemplateView

# code template from Bootstrap documentation 

class AboutView(TemplateView):
	template_name = 'about.html'