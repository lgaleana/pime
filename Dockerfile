FROM --platform=linux/amd64 python:3.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Set environment variables
ENV TEQUILA_API_KEY=${TEQUILA_API_KEY}
