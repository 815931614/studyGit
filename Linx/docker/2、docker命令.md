# Docker命令

#### Docker服务相关命令

- 启动docker服务：

  systemctl start docker

- 停止docker服务:

  systemctl stop docker

- 重启docker服务：

  systemctl restart docker

- 查看docker服务状态

  systemctl status docker

- 设置开机启动docker服务

  systemctl enable docker

#### Docker镜像相关命令

- 查看镜像:查看本地所有的镜像

  ```
  docker images
  docker images -q # 查看所有镜像的id
  ```

- 搜索镜像：从网络中查找需要的镜像

  ```
  docker search 镜像名称
  ```

- 拉取镜像：从Docker仓库下载镜像到本地，镜像名称格式为 名称:版本号，如果版本号不指定则是最新的版本。如果不知道镜像版本，可以去docker hub搜索对应镜像查看。

  ```
  docker pull 镜像名称
  ```

- 删除镜像：删除本地镜像

  ```
  docker rmi 镜像id # 删除指定本地镜像
  docker rmi `docker images -q` # 删除所有本地镜像
  ```

#### Docker容器相关命令

- 查看容器

  ```
  docker ps # 查看正在运行的容器
  docker ps -a # 查看所有容器
  ```

- 创建并启动容器

  ```
  docker run 参数
  ```

  参数说明：

  - -i : 保持容器运行。通常与-t同时使用。加入it这两个参数后，容器创建后自动进入容器中，退出容器后，容器自动关闭。
  - -t: 为容器重新分配一个伪输入终端，通常与-i同时使用。
  - -d:以守护(后台)模式运行容器。创建一个容器在后台运行，需要使用docker exec进入容器。退出后，容器不会关闭。
  - -it创建创建的容器一般称为交互式容器，-id创建的容器一般称为守护式容器
  - --name: 为创建容器的名称。

- 进入容器

  ```
  docker exec 参数 # -id创建的容器退出容器，容器不会关闭
  docker exec -it c_mysql /bin/bash
  ```

- 停止容器

  ```
  docker stop 容器名称
  ```

- 启动容器

  ```
  docker start 容器名称
  ```

- 删除容器：如果容器是运行状态则删除失败，需要停止容器才能删除

  ```
  docker rm 容器名称1 [容器名称2 容器名称3 .....]
  ```

- 查看容器信息

  ```
  docker inspect 容器名称
  ```

  