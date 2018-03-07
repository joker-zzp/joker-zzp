#!/bin/bash

echo "开始安装Python3.6.0"

# 下载Python3.6.0
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz

# 安装所需依赖
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum -y install gcc kernel-devel kenel-headers make bzip2
yum -y install gcc gcc-c++ zlib zlib-devel libffi-devel

# 解压Python
tar -xzvf Python-3.6.0.tgz -C /tmp/

cd /tmp/Python-3.6.0/
./configure --prefix=/usr/local

make && make install

mv /usr/bin/python /usr/bin/python.bak

ln -s /usr/local/bin/python3 /usr/bin/python

python -V && pip3 -V


