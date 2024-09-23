FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirments.txt

EXPOSE 80

# EXPOSE $PORT

# ENV  NAME World

CMD ["uvicorn","bm_fastapi:app","--host","0.0.0.0","--port","80"]   

# CMD exec uvicorn bm_fastapi:app --host=0.0.0.0 --port=$PORT
