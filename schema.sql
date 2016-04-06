##数据库建表语句##
##create-data: 2016-03-23

##--创建db
CREATE DATABASE `ggjjl1` /*!40100 DEFAULT CHARACTER SET utf8 */

##--user表
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `account` int(11) DEFAULT NULL COMMENT '帐号',
  `username` varchar(100) DEFAULT NULL COMMENT '用户名',
  `password` varchar(100) DEFAULT NULL COMMENT '密码',
  `name` varchar(100) DEFAULT NULL COMMENT '姓名',
  `gender` int(1) DEFAULT NULL COMMENT '性别',
  `age` int(3) DEFAULT NULL COMMENT '年龄',
  `mail` varchar(100) DEFAULT NULL COMMENT '邮箱',
  `priority` int(2) DEFAULT NULL COMMENT '权限；0：禁止，1：管理员',
  `ctime` int(11) DEFAULT NULL COMMENT '创建时间',
  `utime` int(11) DEFAULT NULL COMMENT '更新时间',
  `valid` int(1) DEFAULT NULL COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'


##--article表
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `title` varchar(100) DEFAULT NULL COMMENT '标题',
  `content` text COMMENT '文章内容',
  `tag` varchar(100) COMMENT '标签',
  `user_id` int(11) DEFAULT NULL COMMENT '用户id',
  `ctime` int(11) DEFAULT NULL COMMENT '创建时间',
  `utime` int(11) DEFAULT NULL COMMENT '更新时间',
  `valid` int(1) DEFAULT NULL COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章表'

