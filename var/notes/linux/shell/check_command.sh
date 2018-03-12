#! /bin/bash

var=${1}

if command -v ${var} > /dev/null 2>&1;
then
    echo "命令存在"
else
    echo "命令不存在"
fi

if type ${var} >/dev/null 2>&1;
then
    echo "命令存在"
else
    echo "命令不存在"
fi

if hash ${var} 2>/dev/null;
then
    echo "命令存在"
else
    echo "命令不存在"
fi
