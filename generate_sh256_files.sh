#!/bin/bash
for file in ~/Downloads/*.tar.gz
do
    echo $file
    checksumFileName=`awk -F'[-]' '{print $3}' <<< $file`
    checksumFileName="./vars/versions/$checksumFileName.yml"
    echo "$checksumFileName"

    checksumValue=`awk -F'[  ]' '{print $1}' <<< $(sha256sum $file)`
    # echo "$checksumValue"
    echo "---" >> $checksumFileName
    echo "# SHA256 sum for the redistributable package" >> $checksumFileName
    echo "cm_redis_sha256sum: '$checksumValue'" >> $checksumFileName
done