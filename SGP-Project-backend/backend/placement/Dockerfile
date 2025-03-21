# Use a slim Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    && apt-get clean

# Copy requirements file to the container
COPY requirements.txt /app/

# Upgrade pip and install dependencies, including gunicorn
RUN pip install --upgrade pip && pip install gunicorn && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Set the default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]