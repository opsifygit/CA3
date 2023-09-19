FROM python
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY . /app/
EXPOSE 5000
CMD ["python", "main.py"]
