FROM ubuntu:22.04

RUN apt update && apt install -y \
    cmake bzip2 g++ python3 vim wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root
RUN wget https://www.nsnam.org/releases/ns-allinone-3.43.tar.bz2 && \
    tar xvf ns-allinone-3.43.tar.bz2 && \
    rm -rf ns-allinone-3.43.tar.bz2

WORKDIR /root/ns-allinone-3.43/ns-3.43
RUN ./ns3 configure && ./ns3 build
CMD ["/bin/bash"]
