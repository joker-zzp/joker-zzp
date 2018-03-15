#! /bin/bash
# set -v on

echo "hello, Please create a project!"
# echo -e "友情提示! 输入quit 时 退出程序.\n"
echo -e "PS: Enter the \"quit\" exit progtam at any location."

project_path=`pwd`
project_name_path=""

docs_path=""
test_path=""
script_path=""

readme_file=""
install_file=""
install_file_name=""
requirements_file=""

# 程序主函数
function main(){
    #create_process "test"
    # 是否确定创建项目
    if ! create_process "Do you want to create a project?" add_name;
    then
	quit;
    fi
    # 是否创建项目文档目录
    create_process "Do you want to create a document directory?" add_docs;
    # 是否创建自述文件
    create_process "Do you want to create an reatme?" add_readme;
    # 是否创建安装部署程序或脚本
    create_process "Do you want to create an installation file?" add_install
    # 是否创建所需依赖库目录
    create_process "Do you want to create a requirements.txt?" add_requirements;
    # 是否创建测试目录
    create_process "Do you want to create a test directory?" add_test;
    # 是否创建所需脚本目录
    create_process "Do you want to create a script directory?" add_script;

    # 创建项目文件夹
    `mkdir ${project_path}`
    if [ $? -eq 0 ];
    then 
        echo "mkdir "${project_path}
    else
        echo "Creaate an errot,exit the program!"
        quit;
    fi

    # 按需求创建相应文件
    for i in ${project_name_path} ${docs_path} ${test_path} ${script_path} ${readme_file} ${requirements_file} ${install_file};
    do
        # echo ${i}
	if [[ -z ${i} ]];
	then
	    continue
	fi
        if [[ ${i} =~ (install|${install_file_name})$ || ${i} =~ (README)$ || ${i} =~ (\.txt)$ ]];
        then
            test_bin "touch " ${i}
        else
            test_bin "mkdir " ${i}
        fi
    done
}

# 查看上条命令是否正常执行成功
function test_bin(){
    `${1}${2}`
    if [ $? -eq 0 ];
    then
	# 打印创建的文件
        echo "${1}${2}"
    else
        echo "Create an errot,exit the program!"
        quit;
    fi
}

# 退出程序
function quit(){
    echo "Exit..."
    exit 0
}

# 新建名称
function add_name(){
    echo "create project..."
    read -p "Please enter the name of the project : " project_name
    if [[ ${project_name} == "quit" ]];
    then
        quit;
    elif [[ "${project_name}" =~ ^[a-z]{1}+([A-Za-z0-9_.])+$ ]];
    then
        echo "project name: "${project_name}" ..."
        project_path=${project_path}"/"${project_name}
	project_name_path=${project_path}"/"${project_name}
        #echo "mkdir "${project_path}
        #echo "mkdir "${project_path}"/"${project_name}
        return 0
    else
        echo "Name error,please reenter!"
        add_name;
    fi
    return 0
}

# 新建docs目录
function add_docs(){ 
    # echo "创建docs目录..."
    docs_path=${project_path}"/docs"
}

# 创建test目录
function add_test(){
    # echo "创建test目录..."
    test_path=${project_path}"/test"
}

# 创建调用脚本目录
function add_script(){
    # echo "创建调用脚本目录..."
    script_path=${project_path}"/script"
}

# 创建自述文件
function add_readme(){
    # echo "创建自述文件..."
    readme_file=${project_path}"/README"
}

# 创建依赖库名称
function add_requirements(){
    # echo "创建依赖库名称"
    requirements_file=${project_path}"/requirements.txt"
}

# 创建安装程序脚本
function add_install(){
    # echo "创建安装程序脚本..."
    read -p "Please enter the name of the install or the script:" install_file
    if [[ ${install_file} == "quit" ]];
    then
        quit;
    else
	install_file_name=${install_file:="install"}
        echo -e "install name: "${install_file_name}"\n"
	install_file=${project_path}"/"${install_file_name}
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
            echo -e "  yes\n"
            ${2}
            ;;
        "n"|"no")
            echo -e "  no\n"
	    return 1
            ;;
        "quit"|"exit")
            quit;
            ;;
        *)
            # echo "输入有误,请重新输入."
	    echo "Name error,please reenter!"
            create_process "${1}" ${2};
    esac
}

# 执行主函数
main;
