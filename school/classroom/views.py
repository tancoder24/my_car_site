from django.shortcuts import render
from classroom.forms import ContactForm
from django.urls import reverse_lazy
from classroom.models import Teacher

from django.views.generic import (TemplateView, 
                                  FormView, 
                                  CreateView, 
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)


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

class TeacherListView(ListView):
    model = Teacher

    # qeuryset = Teacher.objects.all() # default
    qeuryset = Teacher.objects.order_by('first_name')

    # default template django look for is model_list.html
    context_object_name = "teacher_list"

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL not a template.html
    success_url = reverse_lazy("classroom:thank_you")

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherDetailView(DetailView):
    # template = model_detail.html
    model=Teacher

class TeacherUpdateView(UpdateView):
    # share model_form.html, same as createView
    model = Teacher
    fields = "__all__"

    success_url =reverse_lazy("classroom:list_teacher") 

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url =reverse_lazy("classroom:list_teacher") 

    # default template name
    # model_confirm_delete.html
