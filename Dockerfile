FROM python
COPY . /app
WORKDIR /app/src/ranking
CMD ["python", "./ranking.py"]
