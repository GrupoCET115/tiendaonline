"""
ASGI config for myshop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import shop.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "https": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': AuthMiddlewareStack(
    URLRouter(shop.routing.websocket_urlpatterns)
    ),
})
