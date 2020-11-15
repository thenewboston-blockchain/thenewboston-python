from django_redis.pool import ConnectionFactory


class FakeConnectionFactory(ConnectionFactory):
    """Used for faking Redis, as we don't want to implement fake Redis connection pooling."""

    def get_connection(self, params):
        return self.redis_client_cls(**self.redis_client_cls_kwargs)
