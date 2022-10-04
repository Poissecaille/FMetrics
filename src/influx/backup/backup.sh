influx backup \
  /var/backup/influx/influx_$(date '+%Y-%m-%d_%H-%M') \
-t ${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN}