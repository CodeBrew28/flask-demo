FROM python:3-alpine
WORKDIR /usr/src
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "index.py"]