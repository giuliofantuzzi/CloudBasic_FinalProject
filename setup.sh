#!/bin/bash
# Set default quote-per-user
docker exec --user www-data nextcloud php occ config:app:set files default_quota --value '2 GB'
# Enable encryption
docker exec --user www-data nextcloud /var/www/html/occ app:enable encryption
docker exec --user www-data nextcloud /var/www/html/occ encryption:enable
# Set trusted domain
docker exec --user www-data nextcloud /var/www/html/occ config:system:set trusted_domains 1 --value=nextcloud
# Create users and generate files
sh ./create_usr.sh 50
sh ./generate_files.sh
