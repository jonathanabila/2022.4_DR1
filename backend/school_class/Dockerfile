FROM school_base.2022.4_dr1

RUN mkdir school_class
WORKDIR /app/school_class

COPY poetry.lock pyproject.toml /app/school_class/

RUN poetry install --no-dev
COPY . /school_class

ENV PYTHONPATH=/app/school_class:$PYTHONPATH

EXPOSE 8082
