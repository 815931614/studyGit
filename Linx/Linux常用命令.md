# Docker

- 将一整套环境打包封装成镜像，`无需重复配置环境`，解决环境带来的种种问题。
- Docker容器间是进程隔离的，谁也不会影响谁。

#### 安装Docker

- 环境

  ```
  linux版本	CentOs7(6版本不支持docker，非要安装的话还得先装点别的)
  
  // 系统内核是 3.10以上的
  [root@lala/]# uname -r
  3.10.0-1160.el7.x86_64
  ```

- 在线安装

  ```
  // 卸载旧的docker
  // 这个命令是官网的，但貌似只能卸载docker服务，不能卸载docker客户端
  yum remove docker \
                    docker-client \
                    docker-client-latest \
                    docker-common \
                    docker-latest \
                    docker-latest-logrotate \
                    docker-logrotate \
                    docker-engine
  
  // 安装需要的安装包
  yum install -y yum-utils
  
  // 设置镜像的仓库
  // 这是默认的，国外的
  yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo
  
  // 建议安装阿里云
  http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
  
  // 更新yum软件包索引
  yum makecache fast
  
  // 安装docker	docker-ce社区版	ee企业版
  yum install docker-ce docker-ce-cli containerd.io
  
  // 安装指定版本
  yum list docker-ce --showduplicates | sort -r
  
  yum install docker-ce-19.03.13 docker-ce-cli-19.03.13
  
  // 启动docker
  systemctl start docker
  
  docker version
  
  // 测试docker
  docker run hello-world
  // 开始会找不到镜像，回去下载
  // 出现	Hello from Docker!	则下载成功
  
  // 查看	hello-world	镜像
  docker images
  
  // 开机自启
  systemctl enable docker
  
  ```

- 离线安装

  ```
  # 将镜像使用ftp工具上传服务器
  
  tar -zxvf docker-18.06.3-ce.tgz
  
  cp docker/* /usr/bin/
  
  # 这两个文件可以去在线安装docker的目录直接复制过来就可以
  # centos7 systemctl 管理 docker 的文件
  cp docker.socket /etc/systemd/system
  # 运行docker所需要的文件
  cp docker.service /etc/systemd/system
  
  chmod 777 /etc/systemd/system/docker.service
  chmod 777 /etc/systemd/system/docker.socket
  
  systemctl daemon-reload
  
  systemctl start docker
  
  # 设置开机启动
  systemctl enable docker.service
  ```

- 阿里云镜像加速

  ```
  // 在镜像加速器目录
  sudo mkdir -p /etc/docker
  
  
  sudo tee /etc/docker/daemon.json <<-'EOF'
  {
    "registry-mirrors": 
   // 这个地址不对，用自己的
   ["https://xxxxx.mirror.aliyuncs.com"]
  }
  EOF
  
  sudo systemctl daemon-reload
  
  sudo systemctl restart docker
  
  ```

#### 卸载docker client

```
// 卸载依赖
yum remove docker-ce docker-ce-cli containerd.io

// 删除docker的默认工作路径
rm -rf /var/lib/docker
```

#### 

#### 



