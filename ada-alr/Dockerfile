ARG BASE_IMAGE=registry-ia.ensma.fr/depia-dev/ada-gpr
FROM $BASE_IMAGE

LABEL maintainer="Mikky Richard richardm@mikkyrichard.fr"

USER root
COPY ./alr-2 /opt/alr-2

USER 1000
RUN \
    /opt/alr-2/bin/alr toolchain --select gnat_native && \
    /opt/alr-2/bin/alr toolchain --select gprbuild

RUN \
    echo 'export PATH="/opt/alr-2/bin:$PATH"' >> /home/onyxia/.zshrc
RUN \
    echo 'export PS1="🐳 %F{blue}Ada-Alr %f %~ > "' >> /home/onyxia/.zshrc && \
    echo 'export PS1="🐳 %F{blue}Ada-Alr %f %~ > "' >> /home/onyxia/.bashrc




