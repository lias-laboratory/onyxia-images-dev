ARG BASE_IMAGE=registry-ia.ensma.fr/depia-dev/ada-minimal
FROM $BASE_IMAGE

LABEL maintainer="Mikky Richard richardm@mikkyrichard.fr"

USER root

# Gnat
RUN \
apt-get install --no-install-recommends --yes \
gprbuild gprbuild-doc gprconfig-kb

USER 1000
RUN \
    echo 'export PS1="🐳 %F{blue}Ada-Gpr %f %~ > "' >> /home/onyxia/.zshrc && \
    echo 'export PS1="🐳 %F{blue}Ada-GPR %f %~ > "' >> /home/onyxia/.bashrc
