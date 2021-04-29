from pydantic import BaseModel
from typing import *
from datetime import date, datetime, time, timedelta


class Quest_colomns(BaseModel):
    name: str
    type: str
    pass

class Quest_timings(BaseModel):
    compiler: int
    count: int 
    execute: int 
    pass

class Quest_return(BaseModel):
    query: str
    columns: List[dict]
    dataset: List[List[str]]
    count: Optional[int]
    timings: Optional[Quest_timings]



class Presence_message(BaseModel):
    id: str
    clientId: str
    connectionId: str
    timestamp: datetime
    data: Optional[Union[dict, str]]
    action: int
    pass

class Presence_wrapper(BaseModel):
    channelId: str
    site: str
    presence: List[Presence_message]

class Screech_data(BaseModel):
    raw: str
    author: str
    users: List[str]
    hashtags: List[str]
    image_urls: List[str]

class Ably_webhook_message(BaseModel):
    id: str
    timestamp: datetime
    data: Union[Screech_data, str] # turns out its Ably....
    name: str

class Webhook_data(BaseModel):
    channelId: str
    site: str
    messages: List[Ably_webhook_message]

class Webhook_item(BaseModel):
    webhookId: str
    source: str
    timestamp: datetime
    serial: Optional[str] = None
    name: str
    data: Union[Webhook_data, Presence_wrapper]

class AblyWebhook(BaseModel):
    items: List[Webhook_item]

