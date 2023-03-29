FROM python:3.9-slim

ENV ROOT_DIR /app

WORKDIR ${ROOT_DIR}

# Install system dependencies 
# RUN apt-get install dependencies 

# Install Python dependencies
# RUN pip install dependencies


# context is repo root 
COPY . . 


ENTRYPOINT [ "python", "src/dockerHelloWorld.py" ]

