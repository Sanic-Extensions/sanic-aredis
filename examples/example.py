# @Author: Huang Sizhe
# @Date:   10-Apr-2017
# @Email:  hsz1273327@gmail.com
# @Last modified by:   Huang Sizhe
# @Last modified time: 10-Apr-2017
# @License: MIT



""" To run this example you need additional aioredis package
"""
from sanic import Sanic, response
from sanic.response import json
# import aioredis
from sanic_redis import Redis,Namespace
import ujson
app = Sanic('redis_test')
#redis_pool = aredis.ConnectionPool(host='localhost', port=6379, db=0)
Redis.SetConfig(app,test="redis://localhost:6379/1")
Redis(app)
appspace = Namespace(app.name)

@app.get("/test-my-key/<key>")
async def handle(request,key):
    val = await request.app.redis["test"].get(appspace(key))
    return response.text(val.decode('utf-8'))

@app.post("/test-my-key")
async def handle(request):
    doc = request.json
    for k,v in doc.items():
        await request.app.redis["test"].set(appspace(k), v)
    return json({"result":True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
