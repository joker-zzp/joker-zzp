#! /bin/bash
echo $(pwd)
pach=$(find ~/ -type d -name 'joker-zzp')
if [ -d "${pach}" ];then
    echo 0
    echo "${pach}/test.txt"
    echo $(date +%Y-%m-%d) >> ${pach}/test.txt
else
    echo 1
    exit 1
fi
