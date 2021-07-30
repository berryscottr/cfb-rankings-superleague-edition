FROM python
WORKDIR /app
COPY . .
CMD ["python", "./src/ranking/main.py"]
