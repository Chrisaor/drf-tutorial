from django.urls import path, include

app_name = 'snippets'
urlpatterns = [
    path('django_view/', include('snippets.urls.django_veiw'))
]