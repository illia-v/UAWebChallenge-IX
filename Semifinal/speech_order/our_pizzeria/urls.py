from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^orders/(?P<slug>[\w]{8})/$',
        views.OrderDetailView.as_view(),
        name='order'
    )
]
