# ### os 模块
import os

#system()  在python中执行系统命令
os.system("ifconfig")  # linux
# os.system("ipconfig") windows
# os.system("rm -rf ceshi.txt")

#popen()   执行系统命令返回对象,通过read方法读出字符串
"""
obj = os.popen("ipconfig")
print(obj)
print(obj.read())
"""

#listdir() 获取指定文件夹中所有内容的名称列表 ***
lst = os.listdir()
print(lst)

#getcwd()  获取当前文件所在的默认路径 ***
"""/mnt/hgfs/python32_gx/day16"""
# 路径
res = os.getcwd()
print(res)

# 路径 + 文件名 ***
print(__file__)


#chdir()   修改当前文件工作的默认路径
os.chdir("/home/wangwen/mywork")
os.system("touch 2.txt")

#environ   获取或修改环境变量
"""
[windows]
(1)右键qq属性找路径
(2)右键我的电脑属性->高级系统设置->环境变量->path 打开环境变量添加对应路径
(3)cmd => QQScLauncher

[linux]
(1)在家目录中创建个文件夹,里面创建个文件wangwen,写入ifconfig
(2)增加wangwen的可执行权限 chmod 777 wangwen 测试一下 sudo ./wangwen
(3)添加环境变量在os.environ["PATH"] 中拼接wangwen所有的绝对路径
(4)os.system("wangwen")

总结: 环境变量path的好处是,让系统自动的找到该命令的实际路径进行执行;
"""
print(os.environ["PATH"])
"""
environ(
{
'PATH': '/home/wangwen/bin:/home/wangwen/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 
'XAUTHORITY': '/home/wangwen/.Xauthority', 
'XMODIFIERS': '@im=fcitx', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 
'GDMSESSION': 'ubuntu', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'GTK_IM_MODULE': 'fcitx', 
'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-5JjXbZOpKC', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 
'XDG_CURRENT_DESKTOP': 'Unity', 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/1603', 'QT4_IM_MODULE': 'fcitx', 
'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1', 'LOGNAME': 'wangwen', 'JOB': 'unity-settings-daemon', 'PWD': '/mnt/hgfs/python32_gx/day16', 
'IM_CONFIG_PHASE': '1', 'PYCHARM_HOSTED': '1', 'LANGUAGE': 'zh_CN:zh', 'PYTHONPATH': '/home/wangwen/pylianxi', 'SHELL': '/bin/bash', 'GIO_LAUNCHED_DESKTOP_FILE': '/home/wangwen/.local/share/applications/jetbrains-pycharm-ce.desktop', 'INSTANCE': '', 'GTK2_MODULES': 'overlay-scrollbar', 'UPSTART_INSTANCE': '', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module', 'CLUTTER_IM_MODULE': 'xim', 
'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 
'COMPIZ_BIN_PATH': '/usr/bin/', 'SESSIONTYPE': 'gnome-session', 'XDG_SESSION_DESKTOP': 'ubuntu', 'SHLVL': '0', 
'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'UPSTART_JOB': 'unity7', 'QT_IM_MODULE': 'fcitx', 
'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'GNOME_KEYRING_CONTROL': '', 'LANG': 'zh_CN.UTF-8', 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'XDG_SESSION_TYPE': 'x11', 'XDG_SESSION_ID': 'c2', 'DISPLAY': ':0', 'GDM_LANG': 'zh_CN', 'PYTHONIOENCODING': 'UTF-8', 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/wangwen', 
'UPSTART_EVENTS': 'xsession started', 'SESSION': 'ubuntu', 'GPG_AGENT_INFO': '/home/wangwen/.gnupg/S.gpg-agent:0:1', 'DESKTOP_SESSION': 'ubuntu', 'USER': 'wangwen', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '12487', 'QT_ACCESSIBILITY': '1', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XDG_SEAT': 'seat0', 'PYTHONUNBUFFERED': '1', 'QT_QPA_PLATFORMTHEME': 'appmenu-qt5', 'XDG_RUNTIME_DIR': '/run/user/1000', 'XDG_VTNR': '7', 'HOME': '/home/wangwen', 'GNOME_KEYRING_PID': ''
}
)
"""
os.environ["PATH"] += ":/home/wangwen/mywork"
os.system("wangwen")



#--os 模块属性
#name 获取系统标识   linux,mac ->posix      windows -> nt
print(os.name)
#sep 获取路径分割符号  linux,mac -> /       window-> \ ***
print(os.sep)
#linesep 获取系统的换行符号  linux,mac -> \n    window->\r\n 或 \n
print(repr(os.linesep))





