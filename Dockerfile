FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip3 install --no-cache-dir -U pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "echo '=== CONTAINER TIME ==='; date -u '+%Y-%m-%d %H:%M:%S UTC'; echo '=== PYTHON TIME ==='; python3 -c 'import datetime; print(datetime.datetime.now(datetime.timezone.utc))'; echo '=== START BOT ==='; python3 -m Codexun"]
