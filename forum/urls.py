from django.urls import path
import forum.views as v
app_name = 'forum'

urlpatterns = [
    path('main/', v.cats_articles, name='main_page'),
    path('new-post/', v.new_post, name='new_post'),
    path('login/', v.login_user, name='login'),
    path('logout/', v.logout_user, name='logout'),
    path('register/', v.register_user, name='register'),
    path('category/<slug:slug_for_cats>/', v.cats_articles, name='art_to_cat'),
    path('article/<slug:slug_for_art>/', v.page_to_article, name='page_to_article'),

]
