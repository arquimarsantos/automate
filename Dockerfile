ARG PORT=443

RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y dbus-x11 google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get install python3 -y

RUN echo $(python3 -m site --user-base)

COPY requirements.txt .

ENV PATH /home/.local/bin:${PATH}

RUN apt-get update && apt-get install -y python3-pip && pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
