from django.urls import path
from app.views import HomePageTemplateView,PricePageTemplateView,SignUpView,ApointmentPageTemplateView,AboutPageTemplateView,ServivePageTemplateView,TestestimonalPageTemplateView,TeamPageTemplateView,ContactTemplateView
urlpatterns = [
    path('',HomePageTemplateView.as_view(),name='home_page'),
    path('price/',PricePageTemplateView.as_view(),name='price_page'),
    path('apintment/',ApointmentPageTemplateView.as_view(),name='apoinment_page'),
    path('service/',ServivePageTemplateView.as_view(),name='service_page'),
    path('about/',AboutPageTemplateView.as_view(),name='about_page'),
    path('team/',TeamPageTemplateView.as_view(),name='team_page'),
    path('contact/',ContactTemplateView.as_view(),name='contact_page'),
    path('testestimonal/',TestestimonalPageTemplateView.as_view(),name='testestimonal_page'),
    path('form/',SignUpView.as_view(), name='save')
]