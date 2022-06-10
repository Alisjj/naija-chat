from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from n_chat.users.api.views import UserViewSet
from n_chat.chats.api.views import Conversation, ConversationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("conversation", ConversationViewSet)



app_name = "api"
urlpatterns = router.urls
