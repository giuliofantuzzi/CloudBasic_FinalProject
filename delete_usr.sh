#!/bin/bash

num_users=$1
base_username="TestUser_"
for i in $(seq 1 $num_users); do
    username="${base_username}${i}"
    docker exec --user www-data nextcloud /var/www/html/occ \
        user:delete "$username"
done