WIP -> massively incomplete

A basic clone of twitter designed support some of the functionalities at scale.
Mostly a test bed for ideals etc

Uses: </br>
Questdb for most of the data storage and wrangling. </br>
Redis for Likes & caching etc.  </br>
Ably for browser & mobile pubsub.  </br>
FastAPI for webserver and API. </br>


uvicorn main:app --reload
hypercorn for http/2 aka for production, uvicorn has much better debug infomation
