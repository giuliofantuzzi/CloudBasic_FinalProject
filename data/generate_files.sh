#!/bin/bash
# 1) Generate file.txt
echo "Hello everyone from file.txt :)" > file.txt
# 2) Generate small file (1kb)
dd if=/dev/zero of=file_1kb bs=1024 count=1
# 3) Generate medium file (1Mb)
dd if=/dev/zero of=file_1Mb bs=1024 count=1024
# 4) Generate large file (1Gb)
dd if=/dev/zero of=file_1Gb bs=1M count=1024
