#! /bin/bash

echo ${@}

### 函数 ###

# 检查 输入参数
check_parameters(){
    case ${1} in
        -h|--help)
            return 0
            ;;
        -a|--all)
            return 0
            ;;
        *)
            echo "Error : invalid parameter!"
            exit 2
    esac
    return 0
}

# 执行 输入参数

--help(){
    echo "hello is hellp !"
    echo ""
    exit
    return 0
}

--all(){
    echo all file
}


all_parameters=()
### 执行 ###

if [ ${#} -le 0 ];
then
    echo hello
else
    until [ ${#} -eq 0 ]
    do
        check_parameters ${1}
        all_parameters+=${1}" "
        shift
    done
fi
