#! /bin/bash
set -v on

echo hello!

echo -e "友情提示! 输入quit 时 退出程序.\n"

project_path=`pwd`
project_name_path=""
docs_path=""
test_path=""
readme_file=""
install_file=""
requirements_file=""
scirpt_path=""

function main(){
    #create_process "test"
    echo
    create_process "是否创建项目" add_name;
    echo
    create_process "是否创建文档目录" add_docs;
    echo
    create_process "是否创建自述文件" add_readme;
    echo
    create_process "是否创建安装文件" add_install
    echo
    create_process "是否创建依赖库名称文件" add_requirements;
    echo
    create_process "是否创建测试目录" add_test;
    echo
    create_process "是否创建脚本目录" add_scirpt;

    `mkdir ${project_path}`
    if [ $? -eq 0 ];
    then 
        echo "mkdir "${project_path}
    else
        echo "创建失败!"
        quit;
    fi
    
    for i in ${project_name_path} ${docs_path} ${test_path} ${scirpt_path} ${readme_file} ${requirements_file} ${install_file};
    do
        if [[ -z ${i} ]];
        then
            if [[ ${i} =~ [path]$ ]];
            then
               echo 'mkdir ${i}'
            else
               echo "touch ${i}"
            fi
        fi
    done
}

# 查看上条命令是否正常执行成功
function test_bin(){
    `${1}`
    if [ $? -eq 0 ];
    then
        echo "${1}"
    else
        echo "创建失败!"
        quit;
    fi
}

# 退出程序
function quit(){
    echo "程序退出..."
    exit 0
}

# 新建名称
function add_name(){
    echo "新建名称..."
    
    read -p "Please enter the name of the project : " project_name_path
    if [[ ${project_name_path} == "quit" ]];
    then
        quit;
    elif [[ "${project_name_path}" =~ ^[a-z]{1}+([A-Za-z0-9_.])+$ ]];
    then
        echo "新建项目: "${project_name}" ..."
        project_path=${project_path}"/"${project_name_path}
        #echo "mkdir "${project_path}
        #echo "mkdir "${project_path}"/"${project_name}
        return 0
    else
        echo "名称不合法,请重新输入"
        add_name;
    fi
    return 0
}

# 新建docs目录
function add_docs(){
    echo "创建docs目录..."
    docs_path=${project_path}"/docs"
    #echo "mkdir "${docs_path}
}

# 创建test目录
function add_test(){
    echo "创建test目录..."
    test_path=${project_path}"/test"
    #echo "mkdir "${test_path}
}

# 创建调用脚本目录
function add_scirpt(){
    echo "创建调用脚本目录..."
    scirpt_path=${project_path}"/script"
    #echo "mkdir "${scirpt_path}
}

# 创建自述文件
function add_readme(){
    echo "创建自述文件..."
    readme_file=${project_path}"/README"
    #echo "touch "${readme_file}
}

# 创建依赖库名称
function add_requirements(){
    echo "创建依赖库名称"
    requirements_file=${project_path}"/requirements.txt"
    #echo "touch "${requirements_file}
}

# 创建安装程序脚本
function add_install(){
    echo "创建安装程序脚本"
    read -p "请输入安装程序名称" install_file
    if [[ ${install_file} == "quit" ]];
    then
        quit;
    else
        echo "安装程序名称是: "${install_file:=${project_path}"/"install}
        #echo "touch "${install_path}"/"${install_file:="install"}
    fi
}

# 创建流程
function create_process(){
    # ${1}为名称 ${2}为执行函数
    # 询问是否要创建
    # 是否退出程序
    read -p "${1} [y/n]" a
    case ${a:='y'} in
        "y"|"yes")
            echo "是"
            ${2}
            ;;
        "n"|"no")
            echo "否"
            ;;
        "quit"|"exit")
            quit;
            ;;
        *)
            echo "输入有误,请重新输入."
            create_process "${1}" ${2};
    esac
}

# main;
    #create_process "test"
    echo
    create_process "是否创建项目" add_name;
    echo
    create_process "是否创建文档目录" add_docs;
    echo
    create_process "是否创建自述文件" add_readme;
    echo
    create_process "是否创建安装文件" add_install
    echo
    create_process "是否创建依赖库名称文件" add_requirements;
    echo
    create_process "是否创建测试目录" add_test;
    echo
    create_process "是否创建脚本目录" add_scirpt;

    `mkdir ${project_path}`
    if [ $? -eq 0 ];
    then 
        echo "mkdir "${project_path}
    else
        echo "创建失败!"
        quit;
    fi
    
    for i in ${project_name_path} ${docs_path} ${test_path} ${scirpt_path} ${readme_file} ${requirements_file} ${install_file};
    do
        # echo ${i}
        if [[ ${i} =~ ([README])+$ ]];
        then
            echo "touch "${i}
            echo 1
        elif [[ ${i} =~ [install]+$ ]];
        then
            echo "touch "${i}
            echo 2
        else
            echo "mkdir "${i}
        fi
    done
