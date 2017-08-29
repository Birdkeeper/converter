from django.conf.urls import url


from sample_1.views import request_to_html as view_sample_1
from sample_2.views import request_to_html as view_sample_2
from sample_3.views import request_to_html as view_sample_3


urlpatterns = [
    url(r'^sample_1$', view_sample_1, name="request_to_html_task_1"),
    url(r'^sample_2$', view_sample_2, name="request_to_html_task_2"),
    url(r'^sample_3$', view_sample_3, name="request_to_html_task_3"),
]
