from django.views.generic import TemplateView
from vegetables.models import VegList, VegTitle
from about.models import About
from customers.models import Customers, Title
from footer.models import Footer1, Footer2
from home.models import HomeImage, HomeContent
from contact.models import Contact

class IndexPage(TemplateView):
     template_name = 'index.html'
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["veg_title"] = VegTitle.objects.last()
          context["veg_list"] = VegList.objects.all()
          context["about"] = About.objects.last()
          context["customers"] = Customers.objects.all()
          context["title"] = Title.objects.last()
          context["footer1"] = Footer1.objects.last()
          context["footer2"] = Footer2.objects.last() 
          context["homeimage"] = HomeImage.objects.last()
          context["homecontent"] = HomeContent.objects.all()
          context["contact"] = Contact()         
          return context