# Create the base image
FROM python:3.7-slim

# Change the working directory
WORKDIR /app/

# Install Dependency
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy local folder into the container
COPY ./app.py /app/
COPY Model_Age.sav /app/
COPY Model_Gender.sav /app/
COPY templates/* /app/templates/
COPY Test_Flask.csv /app/


# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["app.py"]