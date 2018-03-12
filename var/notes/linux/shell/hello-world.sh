#! /bin/bash
echo "Hello World !";
echo "Shell 传递参数实例: $0";
echo "第一个参数是: $1";
echo "参数的个数是: $#";
echo "传递的参数作为一个字符串显示: $*"

echo "--- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "--- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

