# Docker数据卷

#### 数据卷的概念作用

- 概念

  - 数据卷是宿主机中的一个目录或文件

  - 当容器目录和数据卷目录绑定后，对方的修改会立即同步

  - 一个数据卷可以被多个容器同时挂载

- 作用

  - 容器数据持久化
  - 外部机器和容器间接通信
  - 容器之间数据交换

#### 配置数据卷

- 创建启动容器时，使用-v参数设置数据卷

  ```
  docker run ... -v 宿主机目录(文件):容器内目录(文件)...
  
  docker run -it --name=rd -v /root/data:/root/data_container redis /bin/bash
  ```

- 注意事项

  - 目录必须是绝对路径
  - 如果目录不存在，会自动创建
  - 可以挂载多个数据卷

#### 配置数据卷容器

1. 创建启动c3数据卷容器，使用-v 参数设置数据卷

   ```
   docker run -it --name=c3 -v /volume centos:7 /bin/bash
   ```

2. 创建启动c1,c2容器，使用--volumes-from参数设置数据卷

   ```
   docker run -it --name=c1 --volumes-from c3 centos:7 /bin/bash
   docker run -it --name=c2 --volumes-from c3 centos:7 /bin/bash
   ```

   