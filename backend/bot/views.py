from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient


class VerificationView(GenericAPIView):
    model = TgUser
    permission_classes = [IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        s: TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data["tg_user"]
        tg_user.user = self.request.user
        tg_user.save(update_fields=("user",))

        instance_s: TgUserSerializer = self.get_serializer(tg_user)
        TgClient(settings.BOT_TOKEN).send_message(tg_user.chat_id, "[verification_has_been_completed]")

        return Response(instance_s.data)
