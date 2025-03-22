FROM python:3.9-slim

# Install dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copy code and data
COPY . /app

# Run the script
CMD ["python", "code/preprocess.py"]