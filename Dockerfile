FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirments.txt

# EXPOSE $PORT

# CMD exec uvicorn model_app:app --port=$PORT --host=0.0.0.0 

# CMD ["uvicorn","bm_fastapi:app","--host","0.0.0.0","--port","$PORT"]   

ENV PORT = $PORT

# CMD exec streamlit run webview2.py   

# CMD exec streamlit run webview2.py   --server.port $PORT --server.address 0.0.0.0

#Running both Streamlit and FastAPI -- using "&" to run the applications in background and wait to shell to respond

CMD   uvicorn model_app:app --port=$PORT --host=0.0.0.0 &\
      streamlit run webview2.py --server.port $PORT --server.address 0.0.0.0 &\
      wait
