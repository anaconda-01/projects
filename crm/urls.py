
from django.contrib import admin
from django.urls import path,include
from leads.views import home,lead_list,lead_create,alter_lead,delete_lead
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", home,name="home"),
    path("<int:pk>",lead_list),
    path("create/",lead_create,name="lead_create"),
    path("<int:pk>/alter/",alter_lead,name="alter_lead"),
    path("<int:pk>/delete/",delete_lead,name="delete_lead"),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
