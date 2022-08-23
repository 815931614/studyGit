



# GIT简介

1. 什么是GIT

   git是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件

2. 代码管理工具的用途

   - 防止代码丢失，做备份
   - 项目的版本管理和控制，可以通过设置节点进行跳转
   - 建立各自的开发环境分支，互不影响，方便合并
   - 在多终端开发时，方便代码的相互传输

3. git的特点

   - git是开源的，多在*nix下使用，可以管理各种文件
   - git是分布式的项目管理工作（SVN是集中式的）
   - git数据管理更多样化，分享速度快，数据安全
   - git拥有更多的分支支持，方便多人协调

4. git安装

   sudo apt-get install git

5. 配置

    配置命令: git config

   - 配置所有用户: git config --system[选项]

     配置文件位置:/etc/gitconfig

   - 配置当前用户:git config --global[选项]

     配置文件位置：~/.gitconfig

   - 配置当前项目:git config[选项]

     配置文件文件:project/.git/config

   1. 配置用户邮箱
   
      ```
      e.g. 将用户名设置为Tedu
      sudo git config -- system user.name 用户名
      cat /etc/gitconfig # 查看配置
      ```
   
   2. 配置用户邮箱
   
      ```
      e.g.  将邮箱设置为lvze@tedu.cn
      git config --global user.email lvze@tedu.cn
      cat ~/.gitconfig # 查看配置
      ```
   
   3. 配置编译器
   
      ```
      e.g. 配置编译器为pycharm
      git init
      git config core.editor pycharm
      cat .git/config # 查看配置
      ```

#### 基本命令

1. ​	初始化仓库

   ```
    git init
   意义： 将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用	git管理
   ```

2. 查看本地仓库状态

   ```
   git status
   说明： 初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。
   ```

3. 将工作内容记录到暂存区

   ```
   git add [files..]
   e.g. 将 a，b记录到暂存区
   
   git add  a b
   e.g. 将所有文件（不包含隐藏文件）记录到暂存区
   git add *
   ```

4. 取消文件暂存记录

   ```
   git rm --cached [file]
   ```

5. 将文件同步到本地仓库

   git commit [file] -m [message]

   说明：-m表示添加一些同步信息，表达同步内容

   ```
   e.g. 将暂存区所有记录同步到仓库区
   git commit -m 'add files'
   ```

6. 查看commit 日至记录

   ```
   git log 
   git log --pretty=oneline
   ```

7. 比较工作区文件和仓库文件差异

   ```
   git diff [file]
   ```

8. 放弃工作区文件修改

   ```
   git checkout -- [file]
   ```

9. 从仓库区恢复文件

   ```
   git checkout [file]
   ```

10. 移动或着删除文件

    ```
    git mv [file] [path]
    git rm [files]
    注意：这两个操作会修改工作区内容，同时将操作记录提交到暂存区。
    ```

####  版本控制

1. 退回到上一个commit节点

   ```
   git reset --hard HEAD^
   注意：一个^表示会退1个版本，依次类推。当版本会退之后工作区会自动和当前commit版本保持一致
   ```

2. 退回到指定的commit_id节点

   ```
   git reset --hard [commit_id]
   ```

3. 查看所有操作记录

   ```
   git reflog
   注意：最上面的为最新记录，可以利用commit_id去往任何位置
   ```

4. 创建标签

   ```
   标签：在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。
   git tag [tag_name] [commit_id] -m [message]
   说明:commit_id可以不写默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
   
   e.g. 在最新的commit处添加标签v1.0
   git tag v1.0 -m '版本1'
   ```

5. 查看标签

   ```
   git tag 查看标签列表
   git show [tag_name]查看标签详细信息
   ```

6. 去往某个标签节点

   ```
   git reset --hard [tag]
   ```

7. 删除标签

   ```
   git tag -d [tag]
   ```

### 保存工作区

1. 保存工作区内容

   ```
   git stash save [message]
   说明：将工作区未提交的修改封存，让工作区回到修改前的状态
   ```

2. 查看工作区列表

   ```
   git stash list
   ```

3. 应用某个工作区

   ```
   git stash apply [stash@{n}]
   ```

4. 删除工作区

   ```
   git stash drop [stash@{n}] 删除某一个工作区
   git stash clear 删除所有保存的工作区
   ```

### 分支管理

```
定义：分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作后再进行分支统一合并。
```

1. 查看分支情况

   ```
   git branch
   说明：前面带*的分支表示当前工作分支
   ```

2. 创建分支

   ```
   git branch [branch_name]
   说明：基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支‘干净’状态。
   ```

3. 切换工作分支

   ```
   git checkout [branch]
   
   说明：2，3可以同时操作，即创建并切换分支
   git checkout -b [branch_name]
   ```

4. 合并分支

   ```
    git merge [branch]
    冲突问题是合并分支过程中最为棘手的问题
    当分支合并时，原分支和以前发生了变化
   ```

5. 删除分支

   ```
   git branch -d [branch]删除分支
   git branch -D [branch]删除没有被合并的分支
   ```

## 远程仓库

1. 什么是远程仓库

   ```
   元从主机上的git仓库。实际上git是分布式结构，每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。
   ```

2. 共享仓库

   ```
   在git仓库中bare属性为True的共享仓库可以很好的和远程仓库进行交互
   ```

   创建步骤：

   - 选择共享仓库目录，将该目录属主设置为当前用户

     ```
     mkdir gitrepo
     chown 主机用户名:主机用户名 gitrepo
     ```

   - 将该目录初始化为git共享目录，下例中tedu为自己取的项目名词，.git为通用结尾后缀

     ```
     cd gitrepo
     git init --bare tedu.git
     ```

   - 将git配置目录与项目目录设置为相同的属主

     ```
     chown -R 主机用户名:主机用户名 tedu.git
     ```

### 远程仓库操作命令

所有操作在本地git仓库下进行

1. 添加远程仓库

   ```
   git remote add 远程仓库名称 主机名称@127.0.0.1:/home/tarena/gitrepo/tedu.git
   ```

2. 删除远程主机

   ```
   git remote rm [origin]
   ```

3. 查看连接的主机

   ```
   git remote
   注意：一个git项目连接的远程主机名不会重复
   ```

4. 将本地分支推送给远程仓库

   ```
   将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应
   git push -u origin master
   ```

5. 删除远程分支

   ```
   git branch -a 查看所有分支
   git push origin [:branch] 删除远程分支
   ```

6. 其他推送方法

   ```
   git push --force origin 用于本地版本比远程版本旧时强行推送本地版本
   git push origin [tag]推送本地标签到远程
   git push origin --tags 推送本地所有标签到远程
   git push origin --delete tag [tagname] 删除远程仓库标签
   ```

   - 从远程获取项目

     ```
     git clone tarena@127.0.0.1:/home/tarena/gitrepo/tedu.git
     注意：获取到本地的项目会自动和远程仓库建立连接。且获取的项目本生也是个git项目。
     ```

   - 从远程获取代码

     ```
     git pull
     
     将远程分支master拉取到本地，作为tmp分支
     git fetch origin master:tmp
     
     区别
     	pull将远程内容直接拉取到本地，并和对应分支内容进行合并
     	fetch 将远程分支内容拉取到本地，但不会和本地对应分支合并，可以自己判断后再使用merge合并。
     ```

### GitHub使用

#### 介绍			

```
github是一个开源的项目社区网站，拥有全球最多的开源项目。开发者可以注册网站在github建立自己的项目仓库。
网址：github.com
代码管理工具：git
```

​	配置git

​		

```

第1步git config --global --list 验证邮箱与GitHub注册时输入的是否一致
git config --global user.name 'yourname'
git config --global user.email 'email@email.com'（这里得名字和邮箱都是注册github时用的）设置全局用户名和邮箱。

 第2步，ssh-keygen -t rsa -C “这里换上你的邮箱”，一路回车，在出现选择时输入Y，再一路回车直到生成密钥。
/home/lfc/.ssh/id_rsa.pub
第3步，使用浏览器到git仓库，添加秘钥，
 
```

