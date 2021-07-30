FROM python
WORKDIR /app
COPY . .
CMD ["python", "./src/main.py"]
