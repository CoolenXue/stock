-- MySQL dump 10.13  Distrib 5.7.21, for Win64 (x86_64)
--
-- Host: localhost    Database: stock
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `code` varchar(8) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `quarter` int(11) DEFAULT NULL,
  `report_date` date DEFAULT NULL,
  `eps` float DEFAULT NULL,
  `eps_yoy` float DEFAULT NULL,
  `bvps` float DEFAULT NULL,
  `roe` float DEFAULT NULL,
  `epcf` float DEFAULT NULL,
  `net_profits` float DEFAULT NULL,
  `profits_yoy` float DEFAULT NULL,
  `net_profit_ratio` float DEFAULT NULL,
  `bips` float DEFAULT NULL,
  `business_income` float DEFAULT NULL,
  `gross_profit_rate` float DEFAULT NULL,
  `targ` float DEFAULT NULL,
  `mbrg` float DEFAULT NULL,
  `nprg` float DEFAULT NULL,
  `epsg` float DEFAULT NULL,
  `seg` float DEFAULT NULL,
  `nav` float DEFAULT NULL,
  `sheqratio` varchar(32) DEFAULT NULL,
  `adratio` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `code` varchar(16) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `industry` varchar(16) DEFAULT NULL,
  `area` varchar(16) DEFAULT NULL,
  `pe` float DEFAULT NULL,
  `outstanding` float DEFAULT NULL,
  `totals` float DEFAULT NULL,
  `totalAssets` float DEFAULT NULL,
  `liquidAssets` float DEFAULT NULL,
  `fixedAssets` float DEFAULT NULL,
  `reserved` float DEFAULT NULL,
  `reservedPerShare` float DEFAULT NULL,
  `esp` float DEFAULT NULL,
  `bvps` float DEFAULT NULL,
  `pb` float DEFAULT NULL,
  `timeToMarket` int(11) DEFAULT NULL,
  `undp` float DEFAULT NULL,
  `perundp` float DEFAULT NULL,
  `rev` float DEFAULT NULL,
  `profit` float DEFAULT NULL,
  `gpr` float DEFAULT NULL,
  `npr` float DEFAULT NULL,
  `holders` float DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `dat` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `trade`
--

DROP TABLE IF EXISTS `trade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trade` (
  `id` int(11) NOT NULL,
  `code` varchar(8) NOT NULL,
  `date` date NOT NULL,
  `open` float NOT NULL,
  `close` float NOT NULL,
  `high` float NOT NULL,
  `low` float NOT NULL,
  `volume` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-27 19:47:17
