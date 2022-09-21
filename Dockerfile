FROM python:3.7

# Setup working directory
WORKDIR /code

# Copy files
COPY main.py /code
COPY ./artifacts/1/7dd1bab9d15f4505ad936d25fe295bfc/artifacts/models /code
COPY application /code/application

RUN pip install fastapi==0.78.0
RUN pip install uvicorn==0.17.6
RUN pip install joblib==0.17.0
RUN pip install -r requirements.txt


# Run the application
EXPOSE 8000

CMD ["python", "main.py"]