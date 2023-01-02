from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    # path('', views.product),
    path('', views.index, name='index'),  # 'pybo/' 에 해당되는 path
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

]
