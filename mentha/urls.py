from django.urls import path
from . import views


app_name = 'mentha'

urlpatterns = [
    path('',views.index_page_view, name='index'),
    path('home/',views.home_page_view, name='home'),
    path('noticias/',views.noticias_page_view, name='noticias'),
    path('projeto/', views.projeto_page_view, name='projeto'),

    path('aplicacoes/', views.aplicacoes_page_view, name='aplicacoes'),
    path('mentha-cog/', views.mentha_cog_page_view, name='mentha-cog'),
    path('mentha-care/', views.mentha_care_page_view, name='mentha-care'),
    path('protocolo-mentha/', views.protocolo_mentha_page_view, name='protocolo-mentha'),


    path('parceiros/', views.parceiros_page_view, name='parceiros'),
    path('equipa/', views.equipa_page_view, name='equipa'),

    path('contacto/', views.contacto_page_view, name='contacto'),
    path('videoconferencia/',views.videoconferencia_page_view, name='videoconferencia'),
    path('zoom-div/',views.zoom_div_page_view, name='zoom-div'),  
    path('login/',views.login_page_view, name='login'),
    path('logout/',views.logout_page_view, name='logout'),
]