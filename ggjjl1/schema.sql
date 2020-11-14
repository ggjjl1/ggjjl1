##数据库建表语句##
##create-data: 2016-03-23

##--创建db
CREATE DATABASE IF NOT EXISTS `ggjjl1` /*!40100 DEFAULT CHARACTER SET utf8 */

##--user表
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` VARCHAR(50) NOT NULL COMMENT '用户名',
  `password` VARCHAR(200) NOT NULL COMMENT '密码',
  `email` VARCHAR(120) NOT NULL COMMENT '邮箱',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_time` DATETIME NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`),
  UNIQUE KEY(`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

##--article表
CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `title` varchar(100) NOT NULL COMMENT '标题',
  `content` text COMMENT '文章内容',
  `author` int(11) NOT NULL COMMENT '用户ID',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章表';

