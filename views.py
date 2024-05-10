from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app.forms import SignUpForm

# Create your views here.
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'


class PricePageTemplateView(TemplateView):
    template_name = 'price.html'


class ApointmentPageTemplateView(TemplateView):
    template_name = 'appointment.html'


class ServivePageTemplateView(TemplateView):
    template_name = 'service.html'


class AboutPageTemplateView(TemplateView):
    template_name = 'about.html'


class TeamPageTemplateView(TemplateView):
    template_name = 'team.html'


class TestestimonalPageTemplateView(TemplateView):
    template_name = 'testimonial.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class SignUpView(FormView):
    template_name = 'index.html'
    form_class = SignUpForm
    success_url = '/success/'  # Replace '/success/' with your actual success URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)