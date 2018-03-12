#! /bin/bash
echo "hello !"

# 文件名称为当天日期
logs_name="$(date '+%Y-%m-%d')"

# 输出创建的文件名称
echo " file name：${logs_name}"

# 仓库路径
git_path=$(find ~/ -type d -name 'joker-zzp')
if [ ! -d "${path}"];then
    echo "找不到路径"
    exit 1
fi

# 输出创建的路径
logs_path="${git_path}/logs/${logs_name}"
echo " file path: ${logs_path}"

# 创建写日记人
if [ -n $(whoami) ];then username=$(whoami); else username="zzp"; fi
echo "user name: ${username}"

# 在什么地方提交的
from="$(hostname)"

# 判断文件是否存在 存在时向后插入文件头 不存在时创建文件并输入文件头
if ! test -f $logs_path
then
    echo "create a file: ${logs_name}"
    touch ${logs_path}
    chmod 644 ${logs_path}
    echo "- name: ${username} -
- date：${logs_name} $(date '+%T') -
- from: ${from} -" > ${logs_path}
    echo "" >> ${logs_path}
else
    echo "write file ${logs_name}..."
    echo "" >> ${logs_path}
    echo "- name: ${username} -" >> ${logs_path}
    echo "- date：${logs_name} $(date '+%T') -" >> ${logs_path}
    echo "- from: ${from} -" >> ${logs_path}
fi

# 编辑日志
vi ${logs_path}
