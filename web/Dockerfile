# FROM python:3.10

# COPY requirements.txt requirements.txt

# RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt
FROM pico/official
RUN apt-get update && apt-get install -y netcat-openbsd
COPY run_app.py .
COPY app /app/

COPY script_production/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
#

#CMD ["gunicorn", "-w", "2", "-b", ":4050", "app:my_app"]


CMD ["/bin/sh", "-c", "/entrypoint.sh && gunicorn -w 2 -b :4050 app:my_app"]