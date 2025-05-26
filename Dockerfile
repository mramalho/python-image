FROM python:3.12-alpine as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY src/app.py .

EXPOSE 9000

CMD [ "python", "app.py" ]