from fastapi import Body, FastAPI, Request
from realtime import ablyPublisher
from followers import follower_manager
from questdb import quest
from screach_sender import sender
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError, validator
import pprint

app = FastAPI()


from models import *

app = FastAPI()
my_db = quest(9009,'localhost')
my_db.connect_tcp()
test_msg = {'name':'my message name', 'data':'my message data'}
realtime = ablyPublisher('Ceq-xQ.OLKXeQ:wXKx1Kj00ZqoUhGi')
social = follower_manager('0.0.0.0','6379')
my_sender = sender(realtime, my_db)

pp = pprint.PrettyPrinter(indent=4)

 
@app.get("/")
async def root():
    # await realtime.test_publish(test_msg)
    pp.pprint(await my_sender.get_latest_from_quest())
    return {"message": "Hello World"}

 

@app.post("/inbound")
async def data_firehose(data: Ably_webhook, request: Request):
    pp.pprint (data)
    #process this into a list of screechs
    # screech_records : List[Screech_data]
    screech_records = []
    try:
        screech_records = [Screech_data.parse_raw(x.data) for x in data.items[0].data.messages]
        my_db.send_screech_to_quest(screech_records)
    except ValidationError as e:
        print(e)

    pp.pprint (request.headers)
    
    return 200


@app.post("/presence")
async def presence_firehose(data: Ably_webhook, request: Request):
    # print(data)
    # all presence events
    #sreech_records = [x for x in data.items[0].data.messages]
    #quest.send_screech_to_quest(screech_record.screachs)
    pp.pprint (data)
    
    return 200


