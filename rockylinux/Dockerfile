FROM rockylinux:9.3

RUN dnf install -y \
    dnf-utils \
    tar zip unzip \
    man-db man-pages \
    net-tools vim\
    git gcc make cmake \
    && dnf clean all

RUN useradd -m r9user

WORKDIR /root
CMD ["/bin/bash"]
