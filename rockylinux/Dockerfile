FROM rockylinux:9.3

RUN dnf install -y \
    dnf-utils \
    tar zip unzip \
    net-tools vim\
    git gcc make cmake \
    && dnf clean all \
    && rm -rf /var/cache/dnf

WORKDIR /root
CMD ["/bin/bash"]
