
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_page),
    path("about", views.about_page),
    path("programs",views.program_page),
    path("program",views.program_page),
    path("curriculum", views.curriculum_page),
    path("gallery",views.gallery_page),
    path('contact', views.contact_page, name="contact"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
    path("dashboard", views.dashboard), 
    path("dashboard", views.dashboard),
    path("contacted/<int:id>", views.mark_contacted),
    path("delete/<int:id>", views.delete_enquiry),
    path("edit/<int:id>", views.edit_enquiry),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
]
