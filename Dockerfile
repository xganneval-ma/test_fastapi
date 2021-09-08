FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install aiohttp

COPY . /app

CMD "uvicorn", "test_fastapi.adapters.create_app:app", "--host", "0.0.0.0", "--port", "9600"