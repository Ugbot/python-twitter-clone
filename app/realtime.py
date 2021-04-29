from ably import AblyRest
import logging


class ablyPublisher:
    def __init__(self, APIKEY):
        self.ably = AblyRest(APIKEY)

        self.testchannel = self.ably.channels.get('test')

        pass

    async def make_ably_token(self, user):
        # query user db
        # make caperbilities
        # return the token request

        return await self.ably.auth.create_token_request(
            {
                'client_id': 'jim',
                'capability': {'channel1': '"*"'},
                'ttl': 3600 * 1000, # ms
            }
        )

    async def publish_to_all(self, msg):
        await self.ably



    async def test_publish(self, msg):
        # query graph DB for structure
        # query timeseries for messages
        # build channel mapping
        # publish batches ?
        self.testchannel.publish(msg['name'], msg['data'])
        print("published")
