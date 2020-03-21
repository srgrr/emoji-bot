FROM ubuntu:18.04
ARG ARG_EMOJI_TWITTER_API_KEY
ARG ARG_EMOJI_TWITTER_PRIVATE_API_KEY
ARG ARG_EMOJI_TWITTER_ACCESS_KEY
ARG ARG_EMOJI_TWITTER_ACCESS_SECRET
ARG ARG_EMOJI_TELEGRAM_TOKEN
ENV EMOJI_TWITTER_API_KEY=$ARG_EMOJI_TWITTER_API_KEY
ENV EMOJI_TWITTER_PRIVATE_KEY=$ARG_EMOJI_TWITTER_PRIVATE_API_KEY
ENV EMOJI_TWITTER_ACCESS_KEY=$ARG_EMOJI_TWITTER_ACCESS_KEY
ENV EMOJI_TWITTER_ACCESS_SECRET=$ARG_EMOJI_TWITTER_ACCESS_SECRET
ENV EMOJI_TELEGRAM_TOKEN=$ARG_EMOJI_TELEGRAM_TOKEN
COPY . /emoji-bot
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install -r /emoji-bot/requirements.txt
RUN ln -s $(which python3) /bin/python
