ARG PORT=443

FROM ubuntu:24.04

RUN apt-get update

RUN apt-get install python3 -y

RUN echo $(python3 -m site --user-base)

COPY requirements.txt .

ENV PATH /home/.local/bin:${PATH}

RUN apt-get install python3-pip -y && python -m venv venv && source venv/bin/activate && pip3 install requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
