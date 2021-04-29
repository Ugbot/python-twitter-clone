import redis
from redisgraph import Node, Edge, Graph, Path


class follower_manager:
    def __init__(self, redis_host, redis_port):
        self.my_redis = redis.Redis(host = redis_host, port = redis_port)
        self.social_graph = Graph('followers', self.my_redis)

    def add_User():
        pass

    def add_follower():
        pass

    