FROM apify/actor-python:3.11

# Copy source
COPY . ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Actor
CMD ["python", "main.py"]
