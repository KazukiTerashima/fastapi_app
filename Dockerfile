FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
# コンテナ内で必要なパッケージをインストール
RUN apk add --no-cache build-base \
 && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
 && apk del build-base

COPY . .
EXPOSE 8000
# FastAPIを8000ポートで待機
CMD ["python", "run.py"]
