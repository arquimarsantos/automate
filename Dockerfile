FROM python:3.10

WORKDIR /app

COPY . /app

COPY . /proxy.crx

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    apt-get clean

#CMD python app.py
CMD gunicorn --workers=2 --access-logfile '-' --error-logfile '-' app:app --timeout 0
