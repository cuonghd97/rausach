-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: rausach
-- ------------------------------------------------------
-- Server version	5.7.25-1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add my users',6,'add_myusers'),(22,'Can change my users',6,'change_myusers'),(23,'Can delete my users',6,'delete_myusers'),(24,'Can view my users',6,'view_myusers'),(25,'Can add chi tiet hoa don',7,'add_chitiethoadon'),(26,'Can change chi tiet hoa don',7,'change_chitiethoadon'),(27,'Can delete chi tiet hoa don',7,'delete_chitiethoadon'),(28,'Can view chi tiet hoa don',7,'view_chitiethoadon'),(29,'Can add chi tiet phieu nhap',8,'add_chitietphieunhap'),(30,'Can change chi tiet phieu nhap',8,'change_chitietphieunhap'),(31,'Can delete chi tiet phieu nhap',8,'delete_chitietphieunhap'),(32,'Can view chi tiet phieu nhap',8,'view_chitietphieunhap'),(33,'Can add chi tiet phieu tra',9,'add_chitietphieutra'),(34,'Can change chi tiet phieu tra',9,'change_chitietphieutra'),(35,'Can delete chi tiet phieu tra',9,'delete_chitietphieutra'),(36,'Can view chi tiet phieu tra',9,'view_chitietphieutra'),(37,'Can add chi tiet phieu tra hang nhap',10,'add_chitietphieutrahangnhap'),(38,'Can change chi tiet phieu tra hang nhap',10,'change_chitietphieutrahangnhap'),(39,'Can delete chi tiet phieu tra hang nhap',10,'delete_chitietphieutrahangnhap'),(40,'Can view chi tiet phieu tra hang nhap',10,'view_chitietphieutrahangnhap'),(41,'Can add chi tiet phieu xuat huy',11,'add_chitietphieuxuathuy'),(42,'Can change chi tiet phieu xuat huy',11,'change_chitietphieuxuathuy'),(43,'Can delete chi tiet phieu xuat huy',11,'delete_chitietphieuxuathuy'),(44,'Can view chi tiet phieu xuat huy',11,'view_chitietphieuxuathuy'),(45,'Can add hinh anh sp',12,'add_hinhanhsp'),(46,'Can change hinh anh sp',12,'change_hinhanhsp'),(47,'Can delete hinh anh sp',12,'delete_hinhanhsp'),(48,'Can view hinh anh sp',12,'view_hinhanhsp'),(49,'Can add hoa don',13,'add_hoadon'),(50,'Can change hoa don',13,'change_hoadon'),(51,'Can delete hoa don',13,'delete_hoadon'),(52,'Can view hoa don',13,'view_hoadon'),(53,'Can add nha cung cap',14,'add_nhacungcap'),(54,'Can change nha cung cap',14,'change_nhacungcap'),(55,'Can delete nha cung cap',14,'delete_nhacungcap'),(56,'Can view nha cung cap',14,'view_nhacungcap'),(57,'Can add phieu nhap',15,'add_phieunhap'),(58,'Can change phieu nhap',15,'change_phieunhap'),(59,'Can delete phieu nhap',15,'delete_phieunhap'),(60,'Can view phieu nhap',15,'view_phieunhap'),(61,'Can add phieu tra',16,'add_phieutra'),(62,'Can change phieu tra',16,'change_phieutra'),(63,'Can delete phieu tra',16,'delete_phieutra'),(64,'Can view phieu tra',16,'view_phieutra'),(65,'Can add phieu tra hang nhap',17,'add_phieutrahangnhap'),(66,'Can change phieu tra hang nhap',17,'change_phieutrahangnhap'),(67,'Can delete phieu tra hang nhap',17,'delete_phieutrahangnhap'),(68,'Can view phieu tra hang nhap',17,'view_phieutrahangnhap'),(69,'Can add phieu xuat huy',18,'add_phieuxuathuy'),(70,'Can change phieu xuat huy',18,'change_phieuxuathuy'),(71,'Can delete phieu xuat huy',18,'delete_phieuxuathuy'),(72,'Can view phieu xuat huy',18,'view_phieuxuathuy'),(73,'Can add san pham',19,'add_sanpham'),(74,'Can change san pham',19,'change_sanpham'),(75,'Can delete san pham',19,'delete_sanpham'),(76,'Can view san pham',19,'view_sanpham'),(77,'Can add loai hang',20,'add_loaihang'),(78,'Can change loai hang',20,'change_loaihang'),(79,'Can delete loai hang',20,'delete_loaihang'),(80,'Can view loai hang',20,'view_loaihang'),(81,'Can add log',21,'add_log'),(82,'Can change log',21,'change_log'),(83,'Can delete log',21,'delete_log'),(84,'Can view log',21,'view_log'),(85,'Can add so quy',22,'add_soquy'),(86,'Can change so quy',22,'change_soquy'),(87,'Can delete so quy',22,'delete_soquy'),(88,'Can view so quy',22,'view_soquy'),(89,'Can add hang dat',23,'add_hangdat'),(90,'Can change hang dat',23,'change_hangdat'),(91,'Can delete hang dat',23,'delete_hangdat'),(92,'Can view hang dat',23,'view_hangdat'),(93,'Can add trang thai hoa don',24,'add_trangthaihoadon'),(94,'Can change trang thai hoa don',24,'change_trangthaihoadon'),(95,'Can delete trang thai hoa don',24,'delete_trangthaihoadon'),(96,'Can view trang thai hoa don',24,'view_trangthaihoadon');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_hoa_don`
--

DROP TABLE IF EXISTS `chi_tiet_hoa_don`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chi_tiet_hoa_don` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_luong_mua` int(11) NOT NULL,
  `hoa_don_id` int(11) DEFAULT NULL,
  `san_pham_id` int(11) DEFAULT NULL,
  `gia_ban` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chi_tiet_hoa_don_hoa_don_id_12b76d4f_fk_hoa_don_id` (`hoa_don_id`),
  KEY `chi_tiet_hoa_don_san_pham_id_727ebd74_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_hoa_don_hoa_don_id_12b76d4f_fk_hoa_don_id` FOREIGN KEY (`hoa_don_id`) REFERENCES `hoa_don` (`id`),
  CONSTRAINT `chi_tiet_hoa_don_san_pham_id_727ebd74_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_hoa_don`
--

LOCK TABLES `chi_tiet_hoa_don` WRITE;
/*!40000 ALTER TABLE `chi_tiet_hoa_don` DISABLE KEYS */;
INSERT INTO `chi_tiet_hoa_don` VALUES (1,10,NULL,1,0),(2,20,NULL,2,0),(3,20,NULL,2,0),(4,11,NULL,2,0),(5,11,NULL,2,0),(6,10,NULL,1,0),(7,10,NULL,2,2000);
/*!40000 ALTER TABLE `chi_tiet_hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_my_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_my_users_id` FOREIGN KEY (`user_id`) REFERENCES `my_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(7,'Store','chitiethoadon'),(8,'Store','chitietphieunhap'),(9,'Store','chitietphieutra'),(10,'Store','chitietphieutrahangnhap'),(11,'Store','chitietphieuxuathuy'),(23,'Store','hangdat'),(12,'Store','hinhanhsp'),(13,'Store','hoadon'),(20,'Store','loaihang'),(21,'Store','log'),(6,'Store','myusers'),(14,'Store','nhacungcap'),(15,'Store','phieunhap'),(16,'Store','phieutra'),(17,'Store','phieutrahangnhap'),(18,'Store','phieuxuathuy'),(19,'Store','sanpham'),(22,'Store','soquy'),(24,'Store','trangthaihoadon');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Store','0001_initial','2019-04-18 18:27:00.206064'),(2,'Store','0002_auto_20190319_2152','2019-04-18 18:27:44.887712'),(3,'Store','0003_myusers_username','2019-04-18 18:27:46.059763'),(4,'Store','0004_auto_20190320_2240','2019-04-18 18:27:50.012955'),(5,'Store','0005_remove_hinhanhsp_duong_dan','2019-04-18 18:27:50.792488'),(6,'Store','0006_sanpham_avt','2019-04-18 18:27:51.639402'),(7,'Store','0007_myusers_is_active','2019-04-18 18:27:52.464826'),(8,'Store','0008_myusers_email','2019-04-18 18:27:53.523225'),(9,'Store','0009_myusers_avatar','2019-04-18 18:27:54.516327'),(10,'Store','0010_log_soquy','2019-04-18 18:28:02.327076'),(11,'Store','0011_auto_20190412_1103','2019-04-18 18:28:06.992494'),(12,'Store','0012_hangdat','2019-04-18 18:28:09.621872'),(13,'Store','0013_hangdat_create_at','2019-04-18 18:28:10.581448'),(14,'Store','0014_hoadon_ten_khach_hang','2019-04-18 18:28:11.367843'),(15,'Store','0015_auto_20190414_1612','2019-04-18 18:28:12.374246'),(16,'Store','0016_auto_20190414_1613','2019-04-18 18:28:14.481275'),(17,'Store','0017_sanpham_update_at','2019-04-18 18:28:15.328844'),(18,'contenttypes','0001_initial','2019-04-18 18:28:16.285396'),(19,'admin','0001_initial','2019-04-18 18:28:18.470428'),(20,'admin','0002_logentry_remove_auto_add','2019-04-18 18:28:18.548434'),(21,'admin','0003_logentry_add_action_flag_choices','2019-04-18 18:28:18.625673'),(22,'contenttypes','0002_remove_content_type_name','2019-04-18 18:28:20.076530'),(23,'auth','0001_initial','2019-04-18 18:28:24.974686'),(24,'auth','0002_alter_permission_name_max_length','2019-04-18 18:28:26.047296'),(25,'auth','0003_alter_user_email_max_length','2019-04-18 18:28:26.099141'),(26,'auth','0004_alter_user_username_opts','2019-04-18 18:28:26.167292'),(27,'auth','0005_alter_user_last_login_null','2019-04-18 18:28:26.267545'),(28,'auth','0006_require_contenttypes_0002','2019-04-18 18:28:26.336250'),(29,'auth','0007_alter_validators_add_error_messages','2019-04-18 18:28:26.407595'),(30,'auth','0008_alter_user_username_max_length','2019-04-18 18:28:26.470896'),(31,'auth','0009_alter_user_last_name_max_length','2019-04-18 18:28:26.526154'),(32,'sessions','0001_initial','2019-04-18 18:28:27.305883'),(33,'Store','0018_auto_20190420_1711','2019-04-20 10:11:31.882529'),(34,'Store','0019_auto_20190421_0944','2019-04-21 02:44:55.706816'),(35,'Store','0020_remove_trangthaihoadon_ten_trang_thai','2019-04-21 03:31:43.929397'),(36,'Store','0021_trangthaihoadon_ma','2019-04-21 04:02:09.587678'),(37,'Store','0022_auto_20190422_1418','2019-04-23 03:04:26.863188'),(38,'Store','0023_remove_hoadon_ngay_lap','2019-04-23 03:04:27.631843');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5m758u1pifc4feje361b03yf37005297','ZGZhNTBmODg4MDRhZDYyNDE1N2QyZGFmZjk5MzczZWUwN2ZiMzljZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2YTM1ZmQzOGM0MjhjMDgwNjhlMTg2M2RmZjMxNTUyMzMxZmJiZDNiIn0=','2019-05-05 03:25:12.549030'),('9wiir2prjl6vbpdxqbdln0gjzbcyyubx','NjA3ZjVkNDNiZjJiMTBjYjMwYWEyYzU2MWU4NTZjZjFlNjNjNTM0OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YWRiNjk3ZmMzN2UyMTIyZWMzYjZmMDQzN2RiZTY4MDE4Yjg1MzhmIn0=','2019-05-05 03:25:28.777927'),('lu3xzrt5vr3ntxt7v7br1bgtom7m05ho','ZGZhNTBmODg4MDRhZDYyNDE1N2QyZGFmZjk5MzczZWUwN2ZiMzljZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2YTM1ZmQzOGM0MjhjMDgwNjhlMTg2M2RmZjMxNTUyMzMxZmJiZDNiIn0=','2019-05-07 03:05:15.891833');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hang_dat`
--

DROP TABLE IF EXISTS `hang_dat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hang_dat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_luong` int(11) NOT NULL,
  `check` int(11) NOT NULL,
  `hang_dat_id` int(11) NOT NULL,
  `nguoi_dung_id` int(11) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hang_dat_hang_dat_id_db9372d7_fk_san_pham_id` (`hang_dat_id`),
  KEY `hang_dat_nguoi_dung_id_068bb32d_fk_my_users_id` (`nguoi_dung_id`),
  CONSTRAINT `hang_dat_hang_dat_id_db9372d7_fk_san_pham_id` FOREIGN KEY (`hang_dat_id`) REFERENCES `san_pham` (`id`),
  CONSTRAINT `hang_dat_nguoi_dung_id_068bb32d_fk_my_users_id` FOREIGN KEY (`nguoi_dung_id`) REFERENCES `my_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hang_dat`
--

LOCK TABLES `hang_dat` WRITE;
/*!40000 ALTER TABLE `hang_dat` DISABLE KEYS */;
INSERT INTO `hang_dat` VALUES (1,10,1,1,2,'2019-04-21 03:28:45.754078'),(2,20,1,2,2,'2019-04-21 03:39:06.685350'),(3,10,1,2,2,'2019-04-21 03:56:18.591712'),(4,10,1,1,2,'2019-04-21 04:39:22.545229'),(5,10,1,2,2,'2019-04-21 18:43:32.346911');
/*!40000 ALTER TABLE `hang_dat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hinh_anh_san_pham`
--

DROP TABLE IF EXISTS `hinh_anh_san_pham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hinh_anh_san_pham` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hinh_anh` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `san_pham_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hinh_anh_san_pham_san_pham_id_5d337f7b_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `hinh_anh_san_pham_san_pham_id_5d337f7b_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hinh_anh_san_pham`
--

LOCK TABLES `hinh_anh_san_pham` WRITE;
/*!40000 ALTER TABLE `hinh_anh_san_pham` DISABLE KEYS */;
INSERT INTO `hinh_anh_san_pham` VALUES (1,'product/images_1.jpeg',1),(2,'product/images_2.jpeg',1),(3,'product/images_3.jpeg',1),(4,'product/jew1264221807.jpg',1),(5,'product/images_1_eVDCXW3.jpeg',2),(6,'product/images_2_oHF2Ogz.jpeg',2),(7,'product/images_3_r3M3EmT.jpeg',2),(8,'product/jew1264221807_GVJE8LR.jpg',2);
/*!40000 ALTER TABLE `hinh_anh_san_pham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoa_don`
--

DROP TABLE IF EXISTS `hoa_don`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hoa_don` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `ghi_chu` longtext COLLATE utf8mb4_unicode_ci,
  `khach_hang_id` int(11) DEFAULT NULL,
  `nguoiTao_id` int(11) DEFAULT NULL,
  `ten_khach_hang` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `trang_thai_id` int(11) DEFAULT NULL,
  `dia_chi` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `sdt` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hoa_don_khach_hang_id_8f140a45_fk_my_users_id` (`khach_hang_id`),
  KEY `hoa_don_nguoiTao_id_d67f750d_fk_my_users_id` (`nguoiTao_id`),
  KEY `hoa_don_trang_thai_id_dfccf52b_fk_trang_thai_id` (`trang_thai_id`),
  CONSTRAINT `hoa_don_khach_hang_id_8f140a45_fk_my_users_id` FOREIGN KEY (`khach_hang_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `hoa_don_nguoiTao_id_d67f750d_fk_my_users_id` FOREIGN KEY (`nguoiTao_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `hoa_don_trang_thai_id_dfccf52b_fk_trang_thai_id` FOREIGN KEY (`trang_thai_id`) REFERENCES `trang_thai` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
/*!40000 ALTER TABLE `hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loai_hang`
--

DROP TABLE IF EXISTS `loai_hang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loai_hang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ten_loai` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loai_hang`
--

LOCK TABLES `loai_hang` WRITE;
/*!40000 ALTER TABLE `loai_hang` DISABLE KEYS */;
INSERT INTO `loai_hang` VALUES (1,'Hang 1');
/*!40000 ALTER TABLE `loai_hang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_users`
--

DROP TABLE IF EXISTS `my_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `huyen` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` int(11) NOT NULL,
  `tinh` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `dia_chi` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ho_ten` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngay_sinh` date NOT NULL,
  `luong` int(11) NOT NULL,
  `sdt` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gioi_tinh` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `role` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `avatar` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_users`
--

LOCK TABLES `my_users` WRITE;
/*!40000 ALTER TABLE `my_users` DISABLE KEYS */;
INSERT INTO `my_users` VALUES (1,'pbkdf2_sha256$120000$HWL9orlppAjG$iUx56u/FJoW7V2vAJeoAJUE7Hz52Dan836TCCkMkZoI=','2019-04-23 03:05:15.832626','',0,1,'','','admin','2019-04-20',0,'12','','2019-04-20 10:39:12.126734',0,'admin',1,'',''),(2,'pbkdf2_sha256$120000$5VykCRNKgsHp$VuM0W4M1AG9quwfO9HDYzLQbwQCDL8wyFPSa1OUdRO0=','2019-04-21 03:25:28.689182','',0,1,'','','Hoang duc cuong','2019-04-21',0,'','','2019-04-21 03:25:28.467229',3,'cuong',1,'cuong@gmail.com','');
/*!40000 ALTER TABLE `my_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nha_cung_cap`
--

DROP TABLE IF EXISTS `nha_cung_cap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nha_cung_cap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ten` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `sdt` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dia_chi` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `huyen` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tinh` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` int(11) NOT NULL,
  `mo_ta` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nha_cung_cap`
--

LOCK TABLES `nha_cung_cap` WRITE;
/*!40000 ALTER TABLE `nha_cung_cap` DISABLE KEYS */;
INSERT INTO `nha_cung_cap` VALUES (1,'Ncc 1','0343944610','ncc1@gmail.com','Hn','119HH','14TTT',1,'','2019-04-21');
/*!40000 ALTER TABLE `nha_cung_cap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `san_pham`
--

DROP TABLE IF EXISTS `san_pham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `san_pham` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ten_san_pham` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngay_them` date NOT NULL,
  `gia_von` int(11) NOT NULL,
  `gia_ban` int(11) NOT NULL,
  `so_luong` int(11) NOT NULL,
  `ton_kho` int(11) NOT NULL,
  `is_active` int(11) NOT NULL,
  `loai_hang_id` int(11) DEFAULT NULL,
  `mo_ta` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `nha_cung_cap_id` int(11) DEFAULT NULL,
  `avt` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `khuyen_mai` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `san_pham_nha_cung_cap_id_7c1fe04c_fk_nha_cung_cap_id` (`nha_cung_cap_id`),
  KEY `san_pham_loai_hang_id_d40b1e9a` (`loai_hang_id`),
  CONSTRAINT `san_pham_loai_hang_id_d40b1e9a_fk_loai_hang_id` FOREIGN KEY (`loai_hang_id`) REFERENCES `loai_hang` (`id`),
  CONSTRAINT `san_pham_nha_cung_cap_id_7c1fe04c_fk_nha_cung_cap_id` FOREIGN KEY (`nha_cung_cap_id`) REFERENCES `nha_cung_cap` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `san_pham`
--

LOCK TABLES `san_pham` WRITE;
/*!40000 ALTER TABLE `san_pham` DISABLE KEYS */;
INSERT INTO `san_pham` VALUES (1,'Rau 1','2019-04-21',1000,2000,200,200,1,1,'rau sach',1,'product/avatar/hqdefault.jpg','2019-04-21 03:22:19.985297',100),(2,'Rau 2','2019-04-21',1000,2000,200,200,1,1,'rau sach',1,'product/avatar/muq1264221549.jpg','2019-04-21 03:02:45.149616',0);
/*!40000 ALTER TABLE `san_pham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `so_quy`
--

DROP TABLE IF EXISTS `so_quy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `so_quy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tong_thu` int(11) NOT NULL,
  `tong_chi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `so_quy`
--

LOCK TABLES `so_quy` WRITE;
/*!40000 ALTER TABLE `so_quy` DISABLE KEYS */;
/*!40000 ALTER TABLE `so_quy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trang_thai`
--

DROP TABLE IF EXISTS `trang_thai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trang_thai` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mo_ta` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ma` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trang_thai`
--

LOCK TABLES `trang_thai` WRITE;
/*!40000 ALTER TABLE `trang_thai` DISABLE KEYS */;
INSERT INTO `trang_thai` VALUES (8,'Đơn hàng khách chưa qua xử lý','phrase1'),(9,'Chờ hàng vận chuyển tiếp nhận thông tin hàng','phrase2'),(10,'Đơn hàng đã được hãng vận chuyển tiếp nhận','phrase3'),(11,'Đơn hàng đang được chuyển đi cho khách hàng','phrase4'),(12,'Đơn hàng đã được giao thành công cho khách hàng','phrase5'),(13,'Đơn hàng chưa được chuyển cho khách hàng','phrase6'),(14,'Sản phẩm khách đặt đã hết hàng','phrase7');
/*!40000 ALTER TABLE `trang_thai` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-23 10:15:51
