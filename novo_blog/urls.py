"""novo_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projetos import views
#Importando módulo para configuração do django (arq. settings.py) arquivos estáticos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Rota raiz e projetos
    path('', views.index),
    path('addProjetoForm/', views.addProjetoForm),
    path('addProjetoForm/addProjeto/', views.addProjeto),
    path('editProjetoForm/<int:projeto_id>', views.editProjetoForm),
    path('editProjetoForm/editProjeto/<int:projeto_id>', views.editProjeto),
    #Rotas para blog
    path('', include('blog.urls'))
]
#Concatenando com as rotas o caminho da pasta media para salver arquivos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
