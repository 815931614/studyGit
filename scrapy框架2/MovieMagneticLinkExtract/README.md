#### 项目简介

​	MovieMagneticLinkExtract是一个基于scrapy的电影信息爬取程序。

#### 支持

- 数据来源：

  - https://www.bugutv.net/14565.html

- 存储：

  mysql，MongoDB，redis

- 支持增量爬虫，定时启动，数据更新

  - 增量爬虫实现方式：redis_redis
  - 数据更新
    - reids_redis只能对url去重，同一个电影在不同的网站上都存在，并且不同网站的url地址不一致、电影名称也存在添字少字，所以无法根据url、电影名称判断电影的重复性
    - 但是电影数据来源网站中都会有该电影的豆瓣链接，所以可以根据豆瓣链接进行校验重复

​	

```sql
create table translatedInfo(
	id int primary key auto_increment, # id
    cover_Image varchar(100),# 影片封面
    title varchar(50), # 影片标题介绍
    translated_name varchar(50), # 影片译名
    old_name varchar(50), # 影片原名
    country varchar(15),# 产地
    years varchar(10), # 年代
    release_date varchar(20), # 上映日期
    category varchar(30), # 类别
    duration varchar(10), # 影片时长
    language varchar(10), # 语言
    imdb_grade varchar(20),# IMDb评分
    imdb_id varchar(15),# IMDb id
    imdb_link varchar(50), # IMDb链接
    douban_grade varchar(20), # 豆瓣评分
    douban_id varchar(15), # 豆瓣id
    douban_link varchar(50),# 豆瓣链接
    rottenTomatoes varchar(20),  #烂 番 茄
    metacritic varchar(20),#Metacritic 
    director varchar(30),  # 导演
    scriptwriter varchar(30),# 编剧
    actor varchar(255), # 演员
    intro text, # 简介
    source varchar(20) # 来源
);

create table magnetism(
	 imdb_id varchar(15),# IMDb id
     douban_id varchar(15), # 豆瓣id
     magnetism_name varchar(50), # 磁力名称
     magnetism_link varchar(50)  # 磁力链接
);
```

