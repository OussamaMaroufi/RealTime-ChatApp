## Django Channels (or just Channels) extends the built-in capabilities of Django allowing Django projects to handle not only HTTP but also protocols that require long-running connections, such as WebSockets, MQTT (IoT), chatbots, radios, and other real-time applications


# Sync vs Async : 
    - Django database needs to be accessed  using synchronous code while the Channels channel layer needs to be accessed using asynchronous code.

    1.sync_to_async - takes a sync function and returns an async function that wraps it

    2. async_to_sync - takes an async function and returns a sync function

# Channel Layer:
    -A channel layer is a kind of a communication system, which allows multiple parts of our application to exchange messages, without shuttling all the messages or events through the database.

    --we'll use a production-ready layer, RedisChannelLayer.
    ==>Run this commande :(env)$ docker run -p 6379:6379 -d redis:5

    -This command downloads the image and spins up a Redis Docker container on port 6379.

# To connect to Redis from Django, we need to install an additional package called channels_redis:
    -(env)$ pip install channels_redis==3.3.1

# Channels Consumer  :
    -A consumer is the basic unit of Channels code. They are tiny ASGI applications, driven by events. They are akin to Django views. However, unlike Django views, consumers are long-running by default. A Django project can have multiple consumers that are combined using Channels routing .

    Each consumer has it's own scope, which is a set of details about a single incoming connection. They contain pieces of data like protocol type, path, headers, routing arguments, user agent, and more.
     

-- Since WebsocketConsumer is a synchronous consumer, we had to call async_to_sync when working with the channel layer.

# Channels Routing :
    Channels provides different routing classes which allow us to combine and stack consumers. They are similar to Django's URLs.

# WebSockets (frontend) : 

    -To communicate with Channels from the frontend, we'll use the WebSocket API.

    WebSockets are extremely easy to use. First, you need to establish a connection by providing a url and then you can listen for the following events:

    onopen - called when a WebSocket connection is established
    onclose - called when a WebSocket connection is destroyed
    onmessage - called when a WebSocket receives a message
    onerror - called when a WebSocket encounters an error

# Authentication : 
    -Channels comes with a built-in class for Django session and authentication management called AuthMiddlewareStack.
    








