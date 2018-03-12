#! /bin/bash
echo "创建目录"

git_path=$(find ~/ -type d -name 'joker-zzp')
if [ ! -d "${git_path}" ];then
    echo "找不到路径"
    exit 1
fi

# 创建文件
file_path=${git_path}/../tree.joker-zzp.txt
touch ${file_path}
echo | tree -sDha ${git_path} -I .git --timefmt '%Y-%m-%d %a' > ${file_path}
echo "创建成功"
exit 0
