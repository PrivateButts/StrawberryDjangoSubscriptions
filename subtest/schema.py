import typing
import strawberry

from foo.gql import FooQuery, FooMutation, FooSubscription


@strawberry.type
class Query(FooQuery):
    pass

@strawberry.type
class Mutation(FooMutation):
    pass

@strawberry.type
class Subscription(FooSubscription):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)