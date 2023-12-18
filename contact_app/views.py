from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .serializers import ContactSerializer
from busel.settings import EMAIL_HOST_USER
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def contact(request) -> Response:
    message_serializer = ContactSerializer(data=request.data)

    if message_serializer.is_valid(raise_exception=True):
        data = message_serializer.validated_data
        send_mail(data['subject'], data['content'], EMAIL_HOST_USER,
                  ['jackson0102almeida@gmail.com'],
                  fail_silently=False)
        return Response({
            'message': "Enviado con exito"
        }, status=status.HTTP_200_OK)



