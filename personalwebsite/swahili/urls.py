from django.urls import path

from . import views

app_name = 'swahili'
urlpatterns = [
    path('swahili/', views.swahili_overview, name='mambo_dunia'),
    path('swahili_test/', views.view_test, name='view_test'),
    path('swahili/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('swahili/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('swahili/<int:question_id>/vote/', views.vote, name='vote'),
]
