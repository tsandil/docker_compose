FROM python:3.11.9-alpine 

WORKDIR /app

# Install redis-tools for redis-cli and dependencies
RUN apk add --no-cache redis


# Copying all requirements and install required dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copying Data Fetcher Script
COPY ./data_fetcher/fetch_data.py ./

CMD [ "python","./fetch_data.py" ]
