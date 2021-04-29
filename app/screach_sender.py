
from models import *
from realtime import ablyPublisher
from questdb import quest
import httpx
import pprint


pp = pprint.PrettyPrinter(indent=4)


class sender():

    def __init__(self, ably_publisher : ablyPublisher, quest_instance : quest):
        self.publisher = ably_publisher
        self.client = httpx.Client()
        self.quest_instance = quest_instance 
        pass


    async def get_latest_from_quest(self, query = 'select * from Screech_list'):
        params = {'query': query, 'count': 'true'} 
        # params = {'query': self.test_query, 'count': 'true'} 
        query_string = 'http://' + self.quest_instance.host + ':9000/exec' 
        response = self.client.get(query_string, params=params)
        #pp.pprint(response.text)
        data =  Quest_return.parse_raw(response.text)
        return data


