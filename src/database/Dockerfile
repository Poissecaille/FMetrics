FROM mysql:8.0.30-debian

# Install crontab
RUN apt-get update && apt-get -y install cron

# Add crontab file in the cron directory
COPY backup/backup.cron /etc/cron.d/backup-cron

# Add conf file to config directory
COPY config/log.cnf /etc/mysql/conf.d

# Give execution rights on the cron job
COPY entrypoint.sh /
# RUN chmod 644 /etc/cron.d/backup-cron

# Give ONLY read rights on the config file
RUN chmod 444 /etc/mysql/conf.d/log.cnf

# Apply cron job
RUN crontab /etc/cron.d/backup-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
RUN chmod 644 /entrypoint.sh
CMD ["bash","/entrypoint.sh"]