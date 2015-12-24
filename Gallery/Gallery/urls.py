from django.conf.urls import include, url
from django.contrib import admin
from Paintings.views import paintings_data

urlpatterns = [
    # Examples:
    # url(r'^$', 'Gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', paintings_data, name = 'paintings_data'),
    
]
