#! /bin/bash
echo "hello !"

# 文件名称为当天日期
logs_name="$(date '+%Y-%m-%d')"

# 输出创建的文件名称
echo "  file name：${logs_name}"

# 仓库路径
git_path=$(find ~/ -type d -name 'joker-zzp')
if [ -d "${git_path}" ];
then
    echo "  git 仓库路径:"${git_path}
else
    echo -e "  No \"joker-zzp\" path can be found "
    exit 1
fi

# 输出创建的路径
logs_path="${git_path}/var/logs/"

# 判断日志路径是否存在正确 
if [ -d ${logs_path} ];
then
    echo "  logs path: ${logs_path}"
    logs_path=${logs_path}${logs_name}
else
    echo -e "  No \"logs\" path can be found"
    exit 1
fi

# 创建写日记人
if [ -n $(whoami) ];then username=$(whoami); else username="zzp"; fi
echo -e "\n  - name: ${username} -"

# 写入的时间
write_file_time=$(date '+%Y-%m-%d %T')
echo -e "  - date: "${write_file_time}" -"

# 在什么地方提交的
from="$(hostname)"
echo -e "  - from: ${from} -"

# 写入日志头
if [ -f ${logs_path} ];
then
    # 文件以存在,写入文件
    echo "write file "${logs_path}"..."
    echo -e "-- name: "${username}" --\n-- time: "${write_file_time}" --\n-- from: "${from}" --\n" >> ${logs_path}
else
    # 文件不存在,添加文件
    echo "create a file: ${logs_name}"
    echo "The create file path is "${logs_path}
    touch ${logs_path}
    chmod 644 ${logs_path}
    echo -e "-- name: "${username}" --\n-- data: "${write_file_time}" --\n-- from: "${from}" --\n" > ${logs_path}
fi

# 编辑日志
vi ${logs_path}
