# 1. Use a lightweight Python image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (to cache layers)
COPY requirements.txt .

# 4. Install dependencies (including the nflreadpy successor)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your source code
COPY . .

# 6. Run the scout script when the container starts
CMD ["python", "src/evaluate.py"]