from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from classroom.forms import ContactForm
from django.urls import reverse_lazy
from classroom.models import Teacher

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html' 

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html' 

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    
    # for template name django will auto matically look for
    # model_form.html in template folder 

    success_url =reverse_lazy("classroom:thank_you") 



class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL not a template.html
    success_url = reverse_lazy("classroom:thank_you")

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)