## Django Channels (or just Channels) extends the built-in capabilities of Django allowing Django projects to handle not only HTTP but also protocols that require long-running connections, such as WebSockets, MQTT (IoT), chatbots, radios, and other real-time applications


# Sync vs Async : 
    - Django database needs to be accessed  using synchronous code while the Channels channel layer needs to be accessed using asynchronous code.

    1.sync_to_async - takes a sync function and returns an async function that wraps it

    2. async_to_sync - takes an async function and returns a sync function

    

