FROM python:3.7.6-slim-stretch

ENV CODEDIR=/opt/code VENVDIR=/opt/venv

WORKDIR "${CODEDIR}"

COPY . "${CODEDIR}"

# install dependencies
RUN set -ex \
    && buildDeps=" \
        g++ \
        make \
        gcc \
    " \
    && runDeps=" \
        default-libmysqlclient-dev \
        uwsgi \
        uwsgi-src \
        libcap-dev \
        libpcre3-dev \
        git \
        uuid-dev \ 
        libsasl2-dev \
        libssl-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $runDeps $buildDeps && rm -rf /var/lib/apt/lists/* \
    && python3 -m venv --prompt 'x3' "${VENVDIR}" \
    && ${VENVDIR}/bin/pip install cython pip-tools \
    && ${VENVDIR}/bin/pip install -r "${CODEDIR}/requirements.txt" \
    && cd /opt \
    && PYTHON=python3.7 \
    && uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python37" \
    && mv python37_plugin.so /usr/lib/uwsgi/plugins/python37_plugin.so \
    && chmod 644 /usr/lib/uwsgi/plugins/python37_plugin.so \
    && cd ${CODEDIR} \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf "${HOME}/.cache"

EXPOSE 8000

# setting "LANG=C.UTF-8" to fix non-ascii support inside container
ENV LANG="C.UTF-8" \
    PATH="${VENVDIR}/bin:${PATH}" \
    PYTHONPATH="${CODEDIR}"

CMD uwsgi --ini uwsgi.ini
