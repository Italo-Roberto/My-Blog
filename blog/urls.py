from django.urls import path
from . import views

urlpatterns = [
    #Rotas de autenticação
    path('loginForm/', views.loginForm),
    path('loginForm/loginUser/', views.loginUser),
    path('logoutUser/', views.logoutUser),
    #Blog
    path('blog/', views.blog, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('save_post/', views.save_post, name='save_post'),
    path('post_edit/<int:post_id>', views.post_edit, name='post_edit'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('blog/post/<int:post_id>', views.post, name='post'),
    path('remove_post/<int:post_id>', views.remove_post, name='remove_post'),
]