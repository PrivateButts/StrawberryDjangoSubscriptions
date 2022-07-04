import strawberry
import typing
import channels.layers
import pickle

from .models import Bar as BarModel


# Queries

@strawberry.type
class Bar:
    id: strawberry.ID
    name: str


def get_bars():
    return BarModel.objects.all()


@strawberry.type
class FooQuery:
    bars: typing.List[Bar] = strawberry.field(resolver=get_bars)


# Mutations

@strawberry.type
class FooMutation:
    @strawberry.mutation
    def create_bar(self, name: str) -> Bar:
        bar = BarModel.objects.create(
            name=name
        )
        return bar

    @strawberry.mutation
    def update_bar(self, id: strawberry.ID, name: str) -> Bar:
        bar = BarModel.objects.get(id=id)
        bar.name = name
        bar.save()
        return bar


# Subscriptions

channel_layer = channels.layers.get_channel_layer()

async def updateBar(bar: BarModel):
    pickled_bar = pickle.dumps(bar)
    await channel_layer.group_send(f"bar_updates", {"bar": pickled_bar})


@strawberry.type
class FooSubscription:
    @strawberry.subscription
    async def bar_updated(self) -> Bar:
        # Enroll user for updates
        channel = await channel_layer.new_channel()
        await channel_layer.group_add('bar_updates', channel)

        # Loop until disconnect
        try:
            while True:
                # Wait for update
                msg = await channel_layer.receive(channel)
                # Send update to client
                yield pickle.loads(msg['bar'])
        finally:
            # Unenroll user from updates and disconnect
            await channel_layer.group_discard('bar_updates', channel)

