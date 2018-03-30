#!/bin/bash

echo "查找文件："${1}

find ${2:-$(pwd)} -iname *${1}*
