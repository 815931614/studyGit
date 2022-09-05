# Docker应用部署

#### 部署

- 容器内的网络服务和外部机器不能直接通信
- 外部机器和宿主可以直接通信
- 宿主机和容器可以直接通信
- 当容器中的网络服务需要被外部机器访问时，可以将容器中提供服务的端口映射到宿主机的端口上。外部机器访问宿主机的该端口，从而间接访问容器的服务。
- 这种操作称为：**端口映射**

#### 部署MySQL

1. 搜索MySQL镜像：

   ```
   docker search mysql
   ```

2. 拉取mysql镜像

   ```
   docker pull mysql:5.7
   ```

3. 创建容器，设置端口映射、目录映射

   ```
   mkdir ~/mysql
   cd ~/mysql
   ```

   ```
   docker run -id \
   -p 3307:3306 \
   --name=c_mysql \
   -v $PWD/conf:/etc/mysql/conf.d \
   -v $PWD/logs:/logs \
   -v $PWD/data:/var/lib/mysql \
   -e MYSQL_ROOT_PASSWORD=123456 \
   mysql:5.7
   ```

   - 参数说明
     - -p 3306:3307: 将容器的3306端口映射到宿主机的3307端口
     - -v $PWD/conf:/etc/mysql/conf.d: 将主机当前目录下的conf/my.cnf挂载到容器的/etc/mysql/my.cnf。配置目录
     - $PWD/logs:/logs：将主机当前目录下的logs目录挂载到容器的/logs。日志目录
     - -v $PWD/data:/var/lib/mysql $ PWD/data:/var/lib/mysql: 将主机当前目录下的data目录挂载到容器的/var/lib/mysql。数据目录
     - -e MYSQL_ROOT_PASSWORD=123456: 初始化root用户的密码

#### 部署Redis

1. 搜索redis镜像

   ```
   docker search redis
   ```

2. 拉取redis镜像

   ```
   docker pull redis:5.0
   ```

3. 创建容器，设置端口映射

   ```
   docker run -id --name=c_redis -p 6379:6379 redis:5.0
   ```

4. 使用外部机器链接redis

   ```
   ./redis-cli.exe -h 192.168.1.5 -p 6379
   ```

   