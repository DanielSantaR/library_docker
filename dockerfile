#imagen base
FROM python:3.7.4

# This is the internal port (Container port)
EXPOSE 8000

WORKDIR /project

# Adding requirements file
ADD requirements.txt /project/

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#script for run the project inside the container 
CMD ["python", "./main.py", "runserver", "0.0.0.0:8000"]
