FROM python:3.12
WORKDIR /Gravity
COPY . /Gravity
COPY requeriments.txt .
COPY .env .
COPY . /models
COPY . /routes
RUN pip install --no-cache-dir -r requeriments.txt --break-system-packages
EXPOSE 5000
CMD ["python3", "app.py", "flask", "run", "--host=0.0.0.0"]