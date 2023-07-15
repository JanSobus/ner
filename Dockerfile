FROM python:3.10-slim-buster


# Don't create .pyc files
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install -y --no-install-recommends \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

#Install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip3 install torch torchvision torchaudio \
 --index-url https://download.pytorch.org/whl/cpu --no-cache-dir\
 && python3 -m pip install -r requirements.txt --no-cache-dir

# Copy project
COPY . /app

#Run the app
WORKDIR /app

#Preload the model so that server doesn't crash
RUN python3 modules/ner_inference.py

#run the server with the app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]

