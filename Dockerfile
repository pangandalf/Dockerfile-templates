FROM python
WORKDIR /app
COPY . /app
RUN pwd
CMD ["python3", "app.py"]

# docker build -t Dockerfile .