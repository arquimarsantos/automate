ARG PORT=443

FROM ubuntu:24.04

RUN apt-get install python -y

RUN echo $(python -m site --user-base)

COPY requirements.txt .

ENV PATH /home/.local/bin:${PATH}

RUN apt-get update && apt-get install -y python-pip && pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
