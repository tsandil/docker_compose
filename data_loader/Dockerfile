FROM python:3.11.9-alpine 


WORKDIR /app

# Install redis-tools for redis-cli and dependencies
RUN apk add --no-cache redis

# Copy requirements and install all the dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# For module as load_data.py uses the module called queries.py
COPY setup.py .
COPY ./utilities ./utilities
COPY ./utilities/__init__.py ./utilities/__init__.py
RUN pip install -e .

COPY ./data_loader/load_data.py ./

CMD ["python","./load_data.py"]
