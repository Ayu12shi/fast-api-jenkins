FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# FROM
#  ↓
# Python environment

# WORKDIR
#  ↓
# Create /app

# COPY requirements.txt
#  ↓
# Copy dependencies

# RUN pip install
#  ↓
# Install FastAPI/Uvicorn

# COPY .
#  ↓
# Copy application

# EXPOSE
#  ↓
# Application uses port 8000

# CMD
#  ↓
# Start FastAPI