DATE=`date +"%d_%b_%Y_%H%M"`
SQLFILE=/var/backup/db/db_backup_${DATE}.sql
mysqldump -u root -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE}|gzip > ${SQLFILE}.gz