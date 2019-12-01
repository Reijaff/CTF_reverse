FROM ubuntu:disco
RUN apt update && apt install -y gdb python3 wget radare2
RUN wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh
ADD babyheap /babyheap
ENTRYPOINT /bin/bash
