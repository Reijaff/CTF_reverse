FROM ubuntu:xenial
RUN apt update && apt install -y gdb python3 wget vim 
RUN wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh
ADD challenge .challenge
ADD libc.so .libc.so
ENTRYPOINT /bin/bash
