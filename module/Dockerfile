ARG IMAGE="python:3.6-slim-buster"

FROM $IMAGE

ENV PYTHON_VERSION=3.6 \
    PATH=/opt/app-root/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PIP_NO_CACHE_DIR=off \
    HOME=/opt/app-root

RUN set -ex \
    && groupadd --system --gid 1001 default \
    && useradd -u 1001 -g 1001 -M -d /opt/app-root default && \
    mkdir -p /opt/app-root/src && \
    chown -R 1001:1001 /opt/app-root

RUN apt-get update \
    && apt-get install -y \
        --no-install-recommends \
        gcc libc-dev curl libgnutls30 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists

USER 1001

RUN python -m pip install --upgrade pip

WORKDIR $HOME/src

COPY --chown=default:default requirements.txt requirements.txt
COPY --chown=default:default app.py app.py

RUN pip install -r requirements.txt

CMD ["flask", "run", "-h", "0.0.0.0"]

HEALTHCHECK CMD python --version