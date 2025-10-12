from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('about/',views.about_view, name='about'),
    path('donate/', views.donate_view, name='donate'),
    path('volunteer/',views.volunteer_view, name='volunteer'),
    path('adopt/', views.adopt_view, name='adopt'),
    path('donate/form/', views.donate_form_view, name='donate_form'),
    path('volunteer/form/',views.volunteer_form_view, name='volunteer_form'),
    path('adopt/form/', views.postadoption_form_view, name='adopt_form'),
    path('adopt/preadoptform/', views.preadoption_form_view, name='preadoption_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)