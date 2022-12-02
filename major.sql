/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 5.5.30 : Database - vtpml03_2021
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`vtpml03_2021` /*!40100 DEFAULT CHARACTER SET latin1 */;

SELECT * FROM predictttt;
USE `vtpml03_2021`;

/*Table structure for table `covid` */

DROP TABLE IF EXISTS `covid`;

CREATE TABLE `covid` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Location` varchar(255) DEFAULT NULL,
  `NoDays` varchar(255) DEFAULT NULL,
  `Date` varchar(255) DEFAULT NULL,
  `Cond` longtext,
  KEY `Id` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `covid` */

/*Table structure for table `pre` */

DROP TABLE IF EXISTS `pre`;

CREATE TABLE `pre` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Precautions` longtext,
  `Date` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pre` */
CREATE TABLE `precautions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Precautions` longtext,
  `pred` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*Table structure for table `predict` */
INSERT INTO precautions (Precautions, pred) VALUES ('Be careful',18.499657958985452);
DROP TABLE IF EXISTS `predict`;

CREATE TABLE `predict` (
  `Date` varchar(255) DEFAULT NULL,
  `nd` varchar(255) DEFAULT NULL,
  `oz` varchar(255) DEFAULT NULL,
  `pm10` varchar(255) DEFAULT NULL,
  `pm2` varchar(255) DEFAULT NULL,
  `pred` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `predict` */

/*Table structure for table `travel` */

DROP TABLE IF EXISTS `travel`;
select * from travel;
CREATE TABLE `travel` (
  `UserId` varchar(255) DEFAULT NULL,
  `TP` varchar(255) DEFAULT NULL,
  `TM` varchar(255) DEFAULT NULL,
  `Age` varchar(255) DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `HC` varchar(255) DEFAULT NULL,
  `SD` varchar(255) DEFAULT NULL,
  `ED` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `travel` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Mobile` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
