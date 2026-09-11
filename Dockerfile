FROM python:3.14.7-slim

WORKDIR /app

COPY auditor.py .

CMD ["pyton", "auditor.py"]