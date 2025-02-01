FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 9090

# Command to run the application
CMD ["python", "app.py"]
