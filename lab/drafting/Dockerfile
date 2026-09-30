# The only place dsh runs (issue #21): a throwaway container, never the host.
# Version pinned: dsh is a developer preview with breaking changes between releases.
FROM node:24-bookworm-slim
ARG DSH_VERSION=0.2.0-rc.2
RUN npm install -g "@deepseek-ai/dsh@${DSH_VERSION}" \
 && npm cache clean --force
# DSH_TELEMETRY_DISABLED: any non-empty value opts the process out of OTel feedback export.
ENV DSH_TELEMETRY_DISABLED=1 \
    NO_UPDATE_NOTIFIER=1 \
    NPM_CONFIG_UPDATE_NOTIFIER=false \
    DSH_HOME=/home/node/.dsh
# Baked in, not mounted: the container gets no path of the host at all.
COPY privacy.patch.yml capture.mjs /cfg/
COPY --chmod=755 entrypoint.sh /usr/local/bin/dsh-run
USER node
WORKDIR /work
ENTRYPOINT ["dsh-run"]
