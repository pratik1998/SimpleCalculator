FROM python:2.7.14

RUN pip install flask

# copy all files to /app
COPY . /app


# change working directory to /app
WORKDIR /app

# expose port
EXPOSE 5000

# run python
ENTRYPOINT ["python", "app.py"]
