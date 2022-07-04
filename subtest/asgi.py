"""
ASGI config for subtest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subtest.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

from strawberry.asgi import GraphQL
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL


django_asgi_app = get_asgi_application()

from .schema import schema
gql_app = GraphQL(schema, subscription_protocols=[
    GRAPHQL_TRANSPORT_WS_PROTOCOL,
    GRAPHQL_WS_PROTOCOL,
])

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": gql_app,
})