FROM debian:buster

RUN apt-get update && \
    apt-get install libswitch-perl -y \
    git \
    build-essential

RUN cd /root && git clone --single-branch --depth 1 https://github.com/pjacklam/p5-Text-Unaccent-PurePerl && \
    cd p5-Text-Unaccent-PurePerl && \
    perl Makefile.PL && \
    make install

RUN cd /root && git clone --single-branch --depth 1 https://github.com/Softcatala/catalan-dict-tools

CMD cd /root/catalan-dict-tools/ && ./build-lt.sh && cp resultats/lt/dicc.txt /app

