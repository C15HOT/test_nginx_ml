FROM python:3.10 as build-image

WORKDIR /service
RUN python -m pip install --upgrade pip
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt


FROM python:3.10 as runtime-image
RUN adduser service
RUN usermod -u 1001 service \
  && groupmod -g 1001 service
USER service

USER service
COPY --chown=service:service --from=build-image /opt/venv /opt/venv

COPY --chown=service:service . /service
WORKDIR /service

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "-m", "app"]