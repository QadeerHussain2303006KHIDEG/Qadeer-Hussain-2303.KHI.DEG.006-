# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster


# Copy the current directory contents into the container at /app
# ADD . /app.py

COPY app.py ./

# Install any needed packages specified in requirements.txt
RUN pip install pandas==0.24.2 numpy==1.18.5 seaborn==0.9.0 scikit-learn==0.23.2 && \
    echo "Dependencies installed successfully"

# Make port 7059 available to the world outside this container
EXPOSE 7059


# Run app.py when the container launches
CMD ["python","app.py"]

