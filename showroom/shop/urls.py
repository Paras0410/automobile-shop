from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('product_details/<pid>',views.product_details),
    path('register/', register, name='register'),
    path('user_login',views.user_login),
    path('user_logout',views.user_logout),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('placeorder',views.placeorder),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('remove/<cid>',views.remove),
    path('range',views.range),
    path('makepayment',views.makepayment),
    path('contact',views.contact),
    path('about',views.about)    
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
