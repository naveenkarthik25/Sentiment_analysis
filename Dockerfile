FROM python
 
# Set working directory
WORKDIR /SENTIMENT_ML
 
# Copy requirements.txt to the container
COPY requirement.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt
 
# Install uvicorn
RUN pip install uvicorn
 
# Copy the Python script to the container
COPY main.py .
 
# Expose port 8000
EXPOSE 8001
 
# Command to run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
#The uvicorn server uses the app  object creted in main file to listen to client’s request.
#--host TEXT Bind socket to this host. [default 127.0.0.1]
#--port INTEGER Bind socket to this port. [default 8000]
 