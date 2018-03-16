#! /bin/bash

echo "提交git!"

# 查看当前状态
status=""
status_value=""

#add_path=""
#staging_path=""

function main(){

    # 查看当前状态
    search;
    # echo ${status}

    # 过滤信息
    filter "${status}";
    for i in add_check reset_check push_check;
    do
        ${i} ${status_value}
    done        
    #add_check ${status_value}
    #push_check ${status_value}
}

function quit(){
    echo "退出程序..."
    exit 1
}

# 检查上条命令是否执行成功
function is_ok(){
    if [[ $? -eq 0 ]];
    then
        echo ${1}"执行成功"
    else
        echo ${1}"失败!"
    fi
}

# 查询未提交文件
function search(){
    status=`git status`
}

function push_check(){
    if [[ ${1} =~ (push) ]];
    then
        echo "有更新可以上传"
        `git push origin master`
        is_ok "上传github,";
        quit;
    fi
    return 0
}

function reset_check(){
    if [[ ${1} =~ (reset) ]];
    then
        echo "有缓存可以提交"
        date_time=$(date +%Y-%m-%d)
        git commit -m ${date_time}
        is_ok "本地缓存更新,";
    else
        echo "没有缓存可以提交"
    fi
}

# 检查是否有未添加目录或文件
function add_check(){
    if [[ ${1} =~ (add) ]];
    then
        echo -e "\n有未添加的目录或文件!!!"
        choice;
    fi
    return 0
}

# 是否继续提交现有缓存目录文件
function choice(){
    read -p "是否提交已添加的目录文件? [y/n]" a
    case ${a:='y'} in
        'y'|'yes')
            echo -e "提交文件中..."
            ;;
        'n'|'no')
            echo -e "取消提交..."
            quit;
            ;;
        *)
            echo "输入有误,请重新输入"
            choice ${1};
    esac
}

# 获取结果数据
function get_result(){
    status_value=${1}
    if [[ ${status_value} =~ ^(\(|"（").*?(\)|"）")$ ]];
    then
        echo "开始判断"
        if [[ ${status_value} =~ (add) ]];
        then
            echo "有add文件"
            status_value=""
        elif [[ ${status_value} =~ (reset) ]];
        then
            echo "有本地提交文件"
            status_value=""
        elif [[ ${status_value} =~ (push) ]];
        then
            echo "有可以上传的文件"
            status_value=""
        fi
    fi      
}

choice=0
status_value=""

function test_aa(){
    
    if [[ ${1} =~ ^(\(|"（") ]];
    then
        choice=1
    elif [[ ${1} =~ (\)|"）")$ ]];
    then
        choice=0
        status_value=${status_value}${1}
        # get_result ${status_value}
    else
        return 1
    fi
    return 0
}

# 过滤需要提交的目录文件
function filter(){
    
    for i in ${1}
    do
        test_aa ${i}
        if [ ${choice} == 1 ];
        then
            # echo ${i}
            status_value=${status_value}${i}
        fi
    done
    #echo ${status_value}
}

main;
