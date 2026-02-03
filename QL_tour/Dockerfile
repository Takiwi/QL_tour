FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    binutils \
    libproj-dev \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/QL_tour


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "QL_tour/manage.py", "runserver", "0.0.0.0:8000"]
