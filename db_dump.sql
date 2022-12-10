-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `mydb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `mydb`;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `user_uid` int NOT NULL,
  PRIMARY KEY (`user_uid`),
  KEY `fk_admin_user_idx` (`user_uid`),
  CONSTRAINT `fk_admin_user` FOREIGN KEY (`user_uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `content` varchar(45) NOT NULL,
  `write_time` datetime DEFAULT NULL,
  `watched_user_uid` int NOT NULL,
  `watched_video_vid` int NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `fk_comment_watched1_idx` (`watched_user_uid`,`watched_video_vid`),
  CONSTRAINT `fk_comment_watched1` FOREIGN KEY (`watched_user_uid`, `watched_video_vid`) REFERENCES `watched` (`user_uid`, `video_vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (7,'this is good','2022-12-04 06:16:17',3,7);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has_playlist`
--

DROP TABLE IF EXISTS `has_playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `has_playlist` (
  `playlist_pid` int NOT NULL,
  `user_uid` int NOT NULL,
  PRIMARY KEY (`playlist_pid`,`user_uid`),
  KEY `fk_has_playlist_playlist1_idx` (`playlist_pid`),
  KEY `fk_has_playlist_user1_idx` (`user_uid`),
  CONSTRAINT `fk_has_playlist_playlist1` FOREIGN KEY (`playlist_pid`) REFERENCES `playlist` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_has_playlist_user1` FOREIGN KEY (`user_uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has_playlist`
--

LOCK TABLES `has_playlist` WRITE;
/*!40000 ALTER TABLE `has_playlist` DISABLE KEYS */;
INSERT INTO `has_playlist` VALUES (8,5);
/*!40000 ALTER TABLE `has_playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has_tag`
--

DROP TABLE IF EXISTS `has_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `has_tag` (
  `video_vid` int NOT NULL,
  `tag_tid` int NOT NULL,
  KEY `fk_has_tag_video1_idx` (`video_vid`),
  KEY `fk_has_tag_tag1_idx` (`tag_tid`),
  CONSTRAINT `fk_has_tag_tag1` FOREIGN KEY (`tag_tid`) REFERENCES `tag` (`tid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_has_tag_video1` FOREIGN KEY (`video_vid`) REFERENCES `video` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has_tag`
--

LOCK TABLES `has_tag` WRITE;
/*!40000 ALTER TABLE `has_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `has_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has_video`
--

DROP TABLE IF EXISTS `has_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `has_video` (
  `playlist_pid` int NOT NULL,
  `video_vid` int NOT NULL,
  KEY `fk_has_video_playlist1_idx` (`playlist_pid`),
  KEY `fk_has_video_video1_idx` (`video_vid`),
  CONSTRAINT `fk_has_video_playlist1` FOREIGN KEY (`playlist_pid`) REFERENCES `playlist` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_has_video_video1` FOREIGN KEY (`video_vid`) REFERENCES `video` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has_video`
--

LOCK TABLES `has_video` WRITE;
/*!40000 ALTER TABLE `has_video` DISABLE KEYS */;
/*!40000 ALTER TABLE `has_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist`
--

DROP TABLE IF EXISTS `playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlist` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `is_playlist_public` int DEFAULT NULL,
  `playlist_title` varchar(45) NOT NULL,
  `creator` int DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
INSERT INTO `playlist` VALUES (4,1,'test playlist',2),(8,1,'my playlist',5);
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `related_video`
--

DROP TABLE IF EXISTS `related_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `related_video` (
  `video_vid` int NOT NULL,
  `rel_video_vid` int NOT NULL,
  KEY `fk_related_video_video1_idx` (`video_vid`),
  KEY `fk_related_video_video2_idx` (`rel_video_vid`),
  CONSTRAINT `fk_related_video_video1` FOREIGN KEY (`video_vid`) REFERENCES `video` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_related_video_video2` FOREIGN KEY (`rel_video_vid`) REFERENCES `video` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `related_video`
--

LOCK TABLES `related_video` WRITE;
/*!40000 ALTER TABLE `related_video` DISABLE KEYS */;
/*!40000 ALTER TABLE `related_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(45) NOT NULL,
  PRIMARY KEY (`tid`),
  UNIQUE KEY `tid_UNIQUE` (`tid`),
  UNIQUE KEY `tag_name_UNIQUE` (`tag_name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (3,'1'),(15,'database'),(8,'private'),(12,'programming'),(7,'public'),(13,'python'),(16,'real');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `id` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'other','other','other','other@naver.com'),(5,'last','last','last','last@naver.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `video` (
  `vid` int NOT NULL AUTO_INCREMENT,
  `video_title` varchar(45) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `creation_time` datetime DEFAULT NULL,
  `is_video_public` int DEFAULT NULL,
  `uploader` int NOT NULL,
  PRIMARY KEY (`vid`),
  KEY `fk_video_user1_idx` (`uploader`),
  CONSTRAINT `fk_video_user1` FOREIGN KEY (`uploader`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video`
--

LOCK TABLES `video` WRITE;
/*!40000 ALTER TABLE `video` DISABLE KEYS */;
INSERT INTO `video` VALUES (7,'other test','other test','2022-12-04 06:02:50',1,3),(8,'other test 2','other test 2','2022-12-04 06:03:13',0,3);
/*!40000 ALTER TABLE `video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watched`
--

DROP TABLE IF EXISTS `watched`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `watched` (
  `user_uid` int NOT NULL,
  `video_vid` int NOT NULL,
  `is_like` int DEFAULT '0',
  PRIMARY KEY (`user_uid`,`video_vid`),
  KEY `fk_watched_user1_idx` (`user_uid`),
  KEY `fk_watched_video1_idx` (`video_vid`),
  CONSTRAINT `fk_watched_user1` FOREIGN KEY (`user_uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_watched_video1` FOREIGN KEY (`video_vid`) REFERENCES `video` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watched`
--

LOCK TABLES `watched` WRITE;
/*!40000 ALTER TABLE `watched` DISABLE KEYS */;
INSERT INTO `watched` VALUES (3,7,0),(3,8,0);
/*!40000 ALTER TABLE `watched` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-09 13:40:31
