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
    cover_Image varchar(120),# 影片封面
    title varchar(255), # 影片标题介绍
    translated_name varchar(255), # 影片译名
    old_name varchar(255), # 影片原名
    country varchar(15),# 产地
    years varchar(10), # 年代
    release_date varchar(20), # 上映日期
    category varchar(50), # 类别
    duration varchar(20), # 影片时长
    language varchar(50), # 语言
    imdb_grade varchar(100),# IMDb评分
    imdb_id varchar(130),# IMDb id
    imdb_link varchar(100), # IMDb链接
    douban_grade varchar(50), # 豆瓣评分
    douban_id varchar(100), # 豆瓣id
    douban_link varchar(100),# 豆瓣链接
    rottenTomatoes varchar(60),  #烂 番 茄
    metacritic varchar(50),#Metacritic 
    director varchar(100),  # 导演
    scriptwriter varchar(200),# 编剧
    actor text, # 演员
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

