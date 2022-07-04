from django.contrib import admin
from django.urls import path
from strawberry.django.views import GraphQLView
from django.conf import settings

from .schema import schema


gqlView = GraphQLView.as_view(
    schema=schema,
    graphiql=settings.DEBUG,
    subscriptions_enabled=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', gqlView),
]
