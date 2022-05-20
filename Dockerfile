FROM ubuntu:18.04
ARG ARG_EMOJI_TELEGRAM_TOKEN
ENV EMOJI_TELEGRAM_TOKEN=$ARG_EMOJI_TELEGRAM_TOKEN
COPY . /emoji-bot
RUN apt-get update
RUN apt-get install python3-pip -y
RUN ln -s $(which python3) /bin/python
RUN python -m pip install -U --force-reinstall pip
RUN pip3 install -r /emoji-bot/requirements.txt
WORKDIR /emoji-bot
CMD "./runbot_telegram.sh"
