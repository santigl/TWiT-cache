# TWiT-cache
Script that caches requests to the TWiT api to avoid exceding the requests-per-minute limit.

The idea was to use it for developing in a Roku, where it is not possible to configure a proxy server.

Just add your `app_id` and `app_key`, launch it, and make your API requests to *http://ip:8000/[request]*. For example: `http://127.0.0.1:8000/episodes`. If the request fails, it returns an empty JSON.

**Caution**: For simplicity, the requests are made using HTTPS from the script to the TWiT server, but then are relayed through HTTP.