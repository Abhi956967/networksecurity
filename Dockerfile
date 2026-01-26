# FROM python:3.11-slim-bookworm
# WORKDIR /app
# COPY . /app

# RUN apt update -y && apt install awscli -y

# RUN apt-get update && pip install -r requirements.txt
# CMD ["python3", "app.py"]

FROM python:3.11-slim-bookworm

WORKDIR /app

# install OS deps
RUN apt-get update -y && apt-get install -y awscli && rm -rf /var/lib/apt/lists/*

# copy project files
COPY . .

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

###