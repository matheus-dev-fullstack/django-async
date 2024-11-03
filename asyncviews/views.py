import asyncio
from time import sleep
import httpx
from django.http import HttpResponse
import time

async def exercise_http_call_async():
    start_time = time.time()

    for i in range(1, 11):
        elapsed_time = time.time() - start_time
        true_elapsed_time = elapsed_time + 1
        print(f"{int(true_elapsed_time)} segundos")  
        await asyncio.sleep(1)
        
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def exercise_async_view(request):
    await exercise_http_call_async() 
    return HttpResponse("Deu tudo certo na contagem!")

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)
        
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)
    
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://httpbin.org")
#         print(r)
        
# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse("Non-blocking HTTP request")