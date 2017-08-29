from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic

import mezzanine

from common.views import contact


admin.autodiscover()


urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^api/', include('sample_base.urls')),
    url(r'^$', mezzanine.pages.views.page, {'slug': '/'}, name='home'),
    url('^', include('mezzanine.urls')),

]


if settings.TEMPLATE_DEBUG:
    urlpatterns += [
        url
        (
            r'^404.html$',
            generic.TemplateView.as_view(template_name='404.html')
        ),
        url
        (
            r'^500.html$',
            generic.TemplateView.as_view(template_name='500.html')
        ),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
