#!/bin/bash
new_users=$1
base_username="TestUser_"
base_password="TestPassword_"
for i in $(seq 1 $new_users)
do
    username="${base_username}${i}"
    password="${base_password}${i}"
    docker exec -e OC_PASS="$password" \
        --user www-data nextcloud /var/www/html/occ \
        user:add --password-from-env "$username"
done