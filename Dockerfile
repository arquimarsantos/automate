ARG PORT=443

FROM ubuntu:24.04

RUN apt-get update

RUN echo $(python3 -m site --user-base)

COPY requirements.txt .

ENV PATH /home/.local/bin:${PATH}

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
