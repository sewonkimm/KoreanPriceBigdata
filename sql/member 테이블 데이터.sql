-- MariaDB dump 10.19  Distrib 10.5.9-MariaDB, for Win64 (AMD64)
--
-- Host: j4a301.p.ssafy.io    Database: ssafy
-- ------------------------------------------------------
-- Server version	10.5.9-MariaDB-1:10.5.9+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'ingu@gmail.com','qwer1234!','김인구','M','1994-10-25','인천광역시',NULL),(3,'taek@gmail.com','daa565e94a765520362474fe25806000f502042e1cfdcd08107d9467a6e5edc3','이은택','M','1993-10-12','서울특별시',NULL),(4,'test@test.com','daa565e94a765520362474fe25806000f502042e1cfdcd08107d9467a6e5edc3','tester','F','1993-10-12','인천광역시',NULL),(7,'chunawoos@gmail.com',NULL,'천창민','\0',NULL,NULL,'Google'),(8,'chunawoos@hanmail.net',NULL,'천창민','M',NULL,NULL,'Kakao'),(9,'swon962@gmail.com',NULL,'SeWon Kim','\0',NULL,NULL,'Google'),(10,'ksw962@naver.com',NULL,'김세원','\0',NULL,NULL,'Kakao'),(11,'test0405@test.com','daa565e94a765520362474fe25806000f502042e1cfdcd08107d9467a6e5edc3','string','M','1993-10-12','string',''),(12,'test1@test.com','7480fb9e85b9396af06f006cf1c95024af2531c65fb505cfbd0add1e2f31573','','\0',NULL,'',''),(13,'test2@test.com','7480fb9e85b9396af06f006cf1c95024af2531c65fb505cfbd0add1e2f31573','','\0',NULL,'',''),(14,'comkorea123@gmail.com',NULL,'정용우','\0',NULL,NULL,'Google'),(15,'rudus1012@gmail.com',NULL,'LeeTaek택이','\0',NULL,NULL,'Google'),(16,'qwer1234@qwer.com','7870a682eef2fb914ebb5b15a2eb8c4ea44eaee54793e04ae2b2589e68564409','','\0',NULL,'',''),(17,'15computer@hanmail.net','4e8c7551b02ec45ab665ed3040b9ae400342118f6225c68a13fdd0971667e2f','','\0',NULL,'',''),(18,'tsopime@gmail.com',NULL,'고양이나만없어','\0',NULL,NULL,'Google'),(19,'jiiioiyoung96@naver.com','c9538678d95119966b3095d5514ad362708965ebd2d903ff34e8c48e76368ec4','','\0',NULL,'',''),(20,'taek@naver.com','91e6e9a3e067e0dc4a4c78cc3406a7aa1ffbcf0c5d3ce2f165ebe2493fd46bda','','\0',NULL,'','');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-07 13:27:45
