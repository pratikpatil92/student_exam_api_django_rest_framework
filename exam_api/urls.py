from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register('create_user', UserProfileView)

urlpatterns = [
                path('', include(router.urls)),
                path('token-auth/', obtain_jwt_token),
                path('all_user/', AllUser.as_view()),
                path('one_user/<int:pk>/', OneUserById.as_view()),
                path('post_questions/', PostQuestions.as_view()),
                path('update_questions/<int:pk>/', UpdateQuenstions.as_view()),
                path('all_questions/', AllQuenstions.as_view()),
                path('post_answer/', PostAnswer.as_view()),
                path('user_answer/', AnswerFilterByUser.as_view()),

]