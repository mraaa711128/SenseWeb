from django.conf.urls import url
from SenseWeb.views import webviews, apiviews

urlpatterns = [
    url(r'^movies/', webviews.movies),
    url(r'^movie/(?P<movieid>\d+)',webviews.movie),
    url(r'^movie/delete/(?P<movieid>\d+)',webviews.delete_movie),

    url(r'^quizzes/', webviews.quizzes),

    url(r'^quiz/(?P<quizid>\d+)', webviews.quiz),
    url(r'^quiz/delete/(?P<quizid>\d+)', webviews.delete_quiz),
    
    
    url(r'^quizset/(?P<quizid>\d+)', webviews.quizset),
    url(r'^quizanswer/(?P<quizid>\d+)', webviews.quizanswer),
    
    url(r'^message/', webviews.msgpage),
    url(r'^sendmessage/(?P<phonenum>[+]\d+)', apiviews.sendmessage),
    
    # url(r'^movie/',webviews.movie),
]