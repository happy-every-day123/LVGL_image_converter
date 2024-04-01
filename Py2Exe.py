from os import system
from os import path
from os import environ
from time import strftime
from time import localtime
from time import time


main_py_file_str = "LVGLImageGUI.py"

# 其他需要导入的py文件
otherPyFiles = [
    
]


def to_exe():
    global main_py_file_str
    # 希望cmd看见就注销下面-w这句话
    visible_cmd_command = "--console"
    # visible_cmd_command = "-w "

    # 添加icon命令 + exe图标路径
    icon_image_str = "-i icon/serial_icon.ico "

    # 获取当前最新版本信息
    ver_info = ''
    with open('version_info.txt', encoding="utf-8") as file_info_obj:
        ver_info = file_info_obj.read()
    print("现在的版本为：", ver_info)

    # 用户输入新的版本信息
    ver_info = input("请输入新的版本号(输入q取消), 示例格式：Major_Version_Number.Minor_Version_Number：\n\t")
    if ver_info == 'q':
        return
    print("新的版本为：V", ver_info)

    # 删除.spec文件
    del_spec = 'del ' + main_py_file_str[:-2] + 'spec'  # 合成删除spec的命令
    print('->>executive ' + del_spec)  # 输出要执行的命令
    system(del_spec)  # 执行删除spec文件的命令

    # 合成命令：需要使用的python文件字符串
    needful_py_file_str = "-p "
    for i in range(len(otherPyFiles)):
        needful_py_file_str += otherPyFiles[i]
        if i != len(otherPyFiles) - 1:
            needful_py_file_str += ";"
    needful_py_file_str += " "
    main_py_file_str = "-F " + main_py_file_str + " "

    # 合成exe名称
    exe_name = " -n FS04_Serial_Port_V" + ver_info

    # 输出要执行的打包命令
    print("->>pyinstaller " + icon_image_str + main_py_file_str +
          needful_py_file_str + visible_cmd_command + exe_name)
    # 执行打包命令
    system("pyinstaller "  + icon_image_str + main_py_file_str +
           needful_py_file_str + visible_cmd_command + exe_name )

    # 记录版本
    with open('version_info.txt', 'w') as file_info_obj:
        file_info_obj.write(ver_info)

    # 获取名字信息
    strname = ''
    if path.isfile('name'):
        with open('name', 'r', encoding='UTF-8') as file_name_obj:
            strname = file_name_obj.read()
    else:
        strname = environ['USERNAME']

    # 在版本日志中记录版本
    with open('version_info_log.txt', 'a') as file_log_obj:
        str_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
        file_log_obj.write(str_time + '\t' + strname +
                           '\tserial_port_V' + ver_info + '\n')

    print("====> Succeeded!!!")


if __name__ == '__main__':
    to_exe()
