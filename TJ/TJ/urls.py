

from django.contrib import admin
from django.urls import path, include

# this is going to allow us to access all the variables in the main settings file
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
# the include command is used to link our urls file in TJ to the main django urls file in journal folder 
    path('', include('journal.urls')),

    
]

#creating a unique link to access our media files (configuring django to allow user uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



