# Manual
Build with
<code>docker build --tag sensor-server .</code>

Run with
<code>docker run --device /dev/gpiomem -p 5000:5000 sensor-server</code>

# Docker compose
<code>docker-compose -d -f docker-compose.dev.yml up --build</code>
