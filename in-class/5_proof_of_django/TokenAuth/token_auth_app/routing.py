from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from token_auth_app.consumers import TokenAuthConsumer
from token_auth_app.middlewares import TokenAuthMiddleWare

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleWare(
            AllowedHostsOriginValidator(
                URLRouter(
                [path("", TokenAuthConsumer.as_asgi())]
                )
            )
        )
    }
)
