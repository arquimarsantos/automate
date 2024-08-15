FROM python:3.10

WORKDIR /app

COPY . /app

COPY . /urban.crx

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    apt-get clean
    
CMD gunicorn --workers=2 app:app --timeout 90
