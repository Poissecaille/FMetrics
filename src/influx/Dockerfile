FROM influxdb:2.4.0

# Install crontab
RUN apt-get update && apt-get -y install cron

# Create folders
RUN mkdir /var/backup
RUN mkdir /var/backup/influx
RUN mkdir /var/log/influx
RUN mkdir /var/log/influx/logs
RUN mkdir /etc/cron.d/custom-cron

# Copy backup script and give it execution rights
COPY backup/backup.sh /var/backup/influx
RUN chmod 644 /var/backup/influx/backup.sh

# Copy log script and give it execution rights
COPY config/logs.sh /var/log/influx
RUN chmod 644 /var/log/influx/logs.sh

# Copy cron file
COPY cronjob.cron /etc/cron.d/custom-cron
# Apply cron job
RUN crontab /etc/cron.d/custom-cron/cronjob.cron

# Run the command on container startup
RUN chmod 777 /entrypoint.sh
CMD ["bash","/entrypoint.sh"]