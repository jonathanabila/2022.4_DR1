FROM school_base.2022.4_dr1

RUN mkdir classroom
WORKDIR /app/classroom/

COPY poetry.lock pyproject.toml /app/classroom/

RUN poetry install --no-dev
COPY . /classroom

ENV PYTHONPATH=/app/classroom:$PYTHONPATH

EXPOSE 8081
