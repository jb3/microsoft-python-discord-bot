FROM acidrain/python-poetry:3.8-slim

WORKDIR /bot

COPY pyproject.toml poetry.lock /bot/

RUN poetry install

COPY . /bot/

CMD ["poetry", "run", "bot"]
