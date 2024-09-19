ARG BASE_IMAGE=registry-ia.ensma.fr/depia-dev/ada-gpr-alr
FROM $BASE_IMAGE

LABEL maintainer="Mikky Richard richardm@mikkyrichard.fr"

ARG USER_CONFIG_DIR="${HOME}/.local/share/code-server/User"
ARG REMOTE_CONFIG_DIR="${HOME}/.local/share/code-server/Machine"

USER root

# Install VSCode
RUN curl -fsSL https://code-server.dev/install.sh | bash && \
    mkdir -p ${USER_CONFIG_DIR} ${REMOTE_CONFIG_DIR}

# Copy custom VSCode settings
COPY --chown=${USERNAME}:${GROUPNAME} settings/User.json ${USER_CONFIG_DIR}/settings.json
COPY --chown=${USERNAME}:${GROUPNAME} settings/Remote.json ${REMOTE_CONFIG_DIR}/settings.json

# VSCode extensions and language-specific configuration
RUN EXT_LIST="AdaCore.ada" && \
    for EXT in $EXT_LIST; do code-server --install-extension $EXT; done
RUN /opt/install-vscode-extensions.sh && \
    # Fix permissions
    chown -R ${USERNAME}:${GROUPNAME} ${HOME} && \
    # Clean
    rm -rf /var/lib/apt/lists/*

USER 1000

EXPOSE 8080

CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "${WORKSPACE_DIR}"]