# PIP的使用

1. 作用：管理python的标准第三方库中第三方软件包

2. 安装

   sudo apt-get install python3-pip

3. 常用命令：

   安装软件：pip3 intall [package]

   sudo pip3 install ssh

   查看当前python软件包：pip3 list

   搜索某个名字的python包：pip3 search [name]

   查看软件包信息：pip3 show [package]

   升级软件包：pip3 install --upgrade [package]

​		卸载软件包：sudo pip3 uninstall [package]

​		导出软件包环境：pip3  freeze > requirements.txt

​		根据文档自动安装：pip3 install -r requirements.txt