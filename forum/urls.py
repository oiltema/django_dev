from django.urls import path
import forum.views as v
app_name = 'forum'

urlpatterns = [
    path('main/', v.main_page, name='main_page' ),

]
