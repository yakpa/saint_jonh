from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^commanderie/', include('commanderie.urls')),
    url(r'^districte/', include('districte.urls')),
    url(r'^admin/', admin.site.urls),
]
