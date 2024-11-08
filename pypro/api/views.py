import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Servicio
from .serializers import ServicioSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework.permissions import AllowAny
class ServicioPorTag(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, tag):
        try:
            servicio = Servicio.objects.get(tag=tag)
            url = servicio.url
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    return Response(response.json(), status=status.HTTP_200_OK)
                else:
                    return Response(
                        {"detail": f"Error al acceder a la URL. Código de estado: {response.status_code}"},
                        status=status.HTTP_502_BAD_GATEWAY
                    )
            except requests.exceptions.RequestException as e:
                return Response(
                    {"detail": f"Error en la conexión a la URL externa: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Servicio.DoesNotExist:
            return Response(
                {"detail": "Servicio no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )