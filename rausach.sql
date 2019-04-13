-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: rausach
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
  PRIMARY KEY (`id`),
  KEY `chi_tiet_hoa_don_hoa_don_id_12b76d4f_fk_hoa_don_id` (`hoa_don_id`),
  KEY `chi_tiet_hoa_don_san_pham_id_727ebd74_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_hoa_don_hoa_don_id_12b76d4f_fk_hoa_don_id` FOREIGN KEY (`hoa_don_id`) REFERENCES `hoa_don` (`id`),
  CONSTRAINT `chi_tiet_hoa_don_san_pham_id_727ebd74_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_hoa_don`
--

LOCK TABLES `chi_tiet_hoa_don` WRITE;
/*!40000 ALTER TABLE `chi_tiet_hoa_don` DISABLE KEYS */;
INSERT INTO `chi_tiet_hoa_don` VALUES (1,1,1,16),(2,4,1,17),(3,5,1,16);
/*!40000 ALTER TABLE `chi_tiet_hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_phieu_nhap`
--

DROP TABLE IF EXISTS `chi_tiet_phieu_nhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chi_tiet_phieu_nhap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_luong` int(11) NOT NULL,
  `don_gia_nhap` int(11) NOT NULL,
  `phieu_nhap_id` int(11) DEFAULT NULL,
  `san_pham_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chi_tiet_phieu_nhap_phieu_nhap_id_113c221a_fk_phieu_nhap_id` (`phieu_nhap_id`),
  KEY `chi_tiet_phieu_nhap_san_pham_id_a46c489a_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_phieu_nhap_phieu_nhap_id_113c221a_fk_phieu_nhap_id` FOREIGN KEY (`phieu_nhap_id`) REFERENCES `phieu_nhap` (`id`),
  CONSTRAINT `chi_tiet_phieu_nhap_san_pham_id_a46c489a_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_phieu_nhap`
--

LOCK TABLES `chi_tiet_phieu_nhap` WRITE;
/*!40000 ALTER TABLE `chi_tiet_phieu_nhap` DISABLE KEYS */;
/*!40000 ALTER TABLE `chi_tiet_phieu_nhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_phieu_tra`
--

DROP TABLE IF EXISTS `chi_tiet_phieu_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chi_tiet_phieu_tra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gia_nhap_lai` int(11) NOT NULL,
  `phieu_tra_id` int(11) NOT NULL,
  `san_pham_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chi_tiet_phieu_tra_phieu_tra_id_cf54fc2f_fk_phieu_tra_hang_id` (`phieu_tra_id`),
  KEY `chi_tiet_phieu_tra_san_pham_id_b515b123_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_phieu_tra_phieu_tra_id_cf54fc2f_fk_phieu_tra_hang_id` FOREIGN KEY (`phieu_tra_id`) REFERENCES `phieu_tra_hang` (`id`),
  CONSTRAINT `chi_tiet_phieu_tra_san_pham_id_b515b123_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_phieu_tra`
--

LOCK TABLES `chi_tiet_phieu_tra` WRITE;
/*!40000 ALTER TABLE `chi_tiet_phieu_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `chi_tiet_phieu_tra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_phieu_tra_hang_nhap`
--

DROP TABLE IF EXISTS `chi_tiet_phieu_tra_hang_nhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chi_tiet_phieu_tra_hang_nhap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_luong` int(11) NOT NULL,
  `gia_tra_lai` int(11) NOT NULL,
  `phieu_tra_hang_nhap_id` int(11) NOT NULL,
  `san_pham_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chi_tiet_phieu_tra_h_phieu_tra_hang_nhap__103ec7f6_fk_phieu_tra` (`phieu_tra_hang_nhap_id`),
  KEY `chi_tiet_phieu_tra_hang_nhap_san_pham_id_14cd1028_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_phieu_tra_h_phieu_tra_hang_nhap__103ec7f6_fk_phieu_tra` FOREIGN KEY (`phieu_tra_hang_nhap_id`) REFERENCES `phieu_tra_hang_nhap` (`id`),
  CONSTRAINT `chi_tiet_phieu_tra_hang_nhap_san_pham_id_14cd1028_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_phieu_tra_hang_nhap`
--

LOCK TABLES `chi_tiet_phieu_tra_hang_nhap` WRITE;
/*!40000 ALTER TABLE `chi_tiet_phieu_tra_hang_nhap` DISABLE KEYS */;
/*!40000 ALTER TABLE `chi_tiet_phieu_tra_hang_nhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_phieu_xuat_huy`
--

DROP TABLE IF EXISTS `chi_tiet_phieu_xuat_huy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chi_tiet_phieu_xuat_huy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_luong` int(11) NOT NULL,
  `phieu_xuat_huy_id` int(11) NOT NULL,
  `san_pham_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chi_tiet_phieu_xuat__phieu_xuat_huy_id_e9fb788b_fk_phieu_xua` (`phieu_xuat_huy_id`),
  KEY `chi_tiet_phieu_xuat_huy_san_pham_id_8291feaa_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `chi_tiet_phieu_xuat__phieu_xuat_huy_id_e9fb788b_fk_phieu_xua` FOREIGN KEY (`phieu_xuat_huy_id`) REFERENCES `phieu_xuat_huy` (`id`),
  CONSTRAINT `chi_tiet_phieu_xuat_huy_san_pham_id_8291feaa_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_phieu_xuat_huy`
--

LOCK TABLES `chi_tiet_phieu_xuat_huy` WRITE;
/*!40000 ALTER TABLE `chi_tiet_phieu_xuat_huy` DISABLE KEYS */;
/*!40000 ALTER TABLE `chi_tiet_phieu_xuat_huy` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hang_dat`
--

LOCK TABLES `hang_dat` WRITE;
/*!40000 ALTER TABLE `hang_dat` DISABLE KEYS */;
INSERT INTO `hang_dat` VALUES (1,1,0,16,16,'2019-04-12 07:04:46.692040'),(3,4,0,17,16,'2019-04-12 08:36:36.279322'),(4,5,0,16,16,'2019-04-12 08:56:05.556239');
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
  `hinh_anh` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `san_pham_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hinh_anh_san_pham_san_pham_id_5d337f7b_fk_san_pham_id` (`san_pham_id`),
  CONSTRAINT `hinh_anh_san_pham_san_pham_id_5d337f7b_fk_san_pham_id` FOREIGN KEY (`san_pham_id`) REFERENCES `san_pham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hinh_anh_san_pham`
--

LOCK TABLES `hinh_anh_san_pham` WRITE;
/*!40000 ALTER TABLE `hinh_anh_san_pham` DISABLE KEYS */;
INSERT INTO `hinh_anh_san_pham` VALUES (34,'product/wolf_howling_at_the_moon-wallpaper-1920x1080.jpg',11),(35,'product/54523021_2236854019960587_7592170919854866432_n.jpg',11),(36,'product/seb_vs_mia.jpg',11),(37,'product/52911406_373731700132772_3554804893463352876_n.jpg',11),(38,'product/52886948_587062731761735_3433025242967048192_n.jpg',11),(39,'product/52692431_10156342887670910_8074481234501173248_n.jpg',11),(40,'product/52551973_174504696850805_7347846461066838016_n.jpg',11),(45,'product/52474510_432052677334776_1864900870374686720_n.jpg',13),(46,'product/52426215_432052340668143_2070176925321527296_n.jpg',13),(47,'product/52293374_432052227334821_8198896253698834432_n.jpg',13),(57,'product/Screenshot_from_2019-03-27_15-30-01.png',14),(58,'product/wolf_howling_at_the_moon-wallpaper-1920x1080_mTWcKlb.jpg',14),(59,'product/54523021_2236854019960587_7592170919854866432_n_mA2Up4F.jpg',14),(63,'product/52886948_587062731761735_3433025242967048192_n_wgAeHDH.jpg',1),(64,'product/52692431_10156342887670910_8074481234501173248_n_5TZqOXv.jpg',1),(65,'product/52551973_174504696850805_7347846461066838016_n_nbdXTfV.jpg',1),(66,'product/52173617_1155364267958828_3043257562150469632_n_FOKhshk.jpg',1),(67,'product/52426215_432052340668143_2070176925321527296_n_SjsYTR7.jpg',15),(68,'product/52474510_432052677334776_1864900870374686720_n_zjFd0pT.jpg',15),(69,'product/FB_IMG_1550330036432_FSSL9My.jpg',15),(70,'product/45690116_1152840774878573_2426769050383155200_o_IIi1W6G.png',16),(71,'product/40921011_1096575153838469_520346922976804864_o_J8ZlTiT.png',16),(72,'product/20507448_823385014490819_4872274261724149439_o_IlEfXkT.png',16),(73,'product/45690116_1152840774878573_2426769050383155200_o_du2qfGL.png',17),(74,'product/40921011_1096575153838469_520346922976804864_o_3sCPWMe.png',17),(75,'product/20507448_823385014490819_4872274261724149439_o_DlT7yZA.png',17),(76,'product/45690116_1152840774878573_2426769050383155200_o_ybmvTRc.png',18),(77,'product/40921011_1096575153838469_520346922976804864_o_sJv2KHR.png',18),(78,'product/20507448_823385014490819_4872274261724149439_o_ONw6ajj.png',18),(79,'product/45690116_1152840774878573_2426769050383155200_o_neW5PII.png',19),(80,'product/40921011_1096575153838469_520346922976804864_o_KHItOTJ.png',19),(81,'product/20507448_823385014490819_4872274261724149439_o_RbXDAhT.png',19),(82,'product/52712959_114934412973205_8935315727137636352_n_bSz11V3.jpg',20),(83,'product/46450993_1159612390868078_857858282163798016_n_ML3mVHr.png',20),(84,'product/52717566_2399793040243727_1478093998278049792_n_586puXS.jpg',20),(85,'product/52712959_114934412973205_8935315727137636352_n_bAqdaF6.jpg',21),(86,'product/46450993_1159612390868078_857858282163798016_n_JP0FWUA.png',21),(87,'product/52717566_2399793040243727_1478093998278049792_n_UQ9jVqA.jpg',21),(88,'product/52712959_114934412973205_8935315727137636352_n_u03wsqm.jpg',22),(89,'product/46450993_1159612390868078_857858282163798016_n_vCyurNJ.png',22),(90,'product/52717566_2399793040243727_1478093998278049792_n_KMyQhEO.jpg',22),(91,'product/52712959_114934412973205_8935315727137636352_n_3UgKhUb.jpg',23),(92,'product/46450993_1159612390868078_857858282163798016_n_wRdwVun.png',23),(93,'product/52717566_2399793040243727_1478093998278049792_n_LmQaGJb.jpg',23),(94,'product/52712959_114934412973205_8935315727137636352_n_KBViGPO.jpg',24),(95,'product/46450993_1159612390868078_857858282163798016_n_ii5XqMO.png',24),(96,'product/52717566_2399793040243727_1478093998278049792_n_uvrHWaw.jpg',24);
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
  `ngay_lap` datetime(6) DEFAULT NULL,
  `created_at` date NOT NULL,
  `ghi_chu` longtext COLLATE utf8_unicode_ci,
  `is_paid` int(11) NOT NULL,
  `khach_hang_id` int(11) DEFAULT NULL,
  `nguoiTao_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hoa_don_khach_hang_id_8f140a45_fk_my_users_id` (`khach_hang_id`),
  KEY `hoa_don_nguoiTao_id_d67f750d_fk_my_users_id` (`nguoiTao_id`),
  CONSTRAINT `hoa_don_khach_hang_id_8f140a45_fk_my_users_id` FOREIGN KEY (`khach_hang_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `hoa_don_nguoiTao_id_d67f750d_fk_my_users_id` FOREIGN KEY (`nguoiTao_id`) REFERENCES `my_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
INSERT INTO `hoa_don` VALUES (1,'2019-04-12 09:08:52.580461','2019-04-12',NULL,0,16,NULL);
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
  `ten_loai` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loai_hang`
--

LOCK TABLES `loai_hang` WRITE;
/*!40000 ALTER TABLE `loai_hang` DISABLE KEYS */;
INSERT INTO `loai_hang` VALUES (1,'Rau 1aa'),(2,'Rau 3');
/*!40000 ALTER TABLE `loai_hang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `hanh_dong` longtext COLLATE utf8_unicode_ci NOT NULL,
  `hoa_don_id` int(11) DEFAULT NULL,
  `nguoi_tao_id` int(11) DEFAULT NULL,
  `phieu_nhap_id` int(11) DEFAULT NULL,
  `phieu_tra_id` int(11) DEFAULT NULL,
  `phieu_tra_hang_nhap_id` int(11) DEFAULT NULL,
  `phieu_xuat_huy_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `log_hoa_don_id_b77b767c_fk_hoa_don_id` (`hoa_don_id`),
  KEY `log_nguoi_tao_id_fbac3779_fk_my_users_id` (`nguoi_tao_id`),
  KEY `log_phieu_nhap_id_a89f2cfb_fk_phieu_nhap_id` (`phieu_nhap_id`),
  KEY `log_phieu_tra_id_bbcba38d_fk_phieu_tra_hang_id` (`phieu_tra_id`),
  KEY `log_phieu_tra_hang_nhap_id_daff1b1d_fk_phieu_tra_hang_nhap_id` (`phieu_tra_hang_nhap_id`),
  KEY `log_phieu_xuat_huy_id_bcf10c6b_fk_phieu_xuat_huy_id` (`phieu_xuat_huy_id`),
  CONSTRAINT `log_hoa_don_id_b77b767c_fk_hoa_don_id` FOREIGN KEY (`hoa_don_id`) REFERENCES `hoa_don` (`id`),
  CONSTRAINT `log_nguoi_tao_id_fbac3779_fk_my_users_id` FOREIGN KEY (`nguoi_tao_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `log_phieu_nhap_id_a89f2cfb_fk_phieu_nhap_id` FOREIGN KEY (`phieu_nhap_id`) REFERENCES `phieu_nhap` (`id`),
  CONSTRAINT `log_phieu_tra_hang_nhap_id_daff1b1d_fk_phieu_tra_hang_nhap_id` FOREIGN KEY (`phieu_tra_hang_nhap_id`) REFERENCES `phieu_tra_hang_nhap` (`id`),
  CONSTRAINT `log_phieu_tra_id_bbcba38d_fk_phieu_tra_hang_id` FOREIGN KEY (`phieu_tra_id`) REFERENCES `phieu_tra_hang` (`id`),
  CONSTRAINT `log_phieu_xuat_huy_id_bcf10c6b_fk_phieu_xuat_huy_id` FOREIGN KEY (`phieu_xuat_huy_id`) REFERENCES `phieu_xuat_huy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_users`
--

DROP TABLE IF EXISTS `my_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `huyen` longtext COLLATE utf8_unicode_ci NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` int(11) NOT NULL,
  `tinh` longtext COLLATE utf8_unicode_ci NOT NULL,
  `dia_chi` longtext COLLATE utf8_unicode_ci NOT NULL,
  `ho_ten` longtext COLLATE utf8_unicode_ci NOT NULL,
  `ngay_sinh` date NOT NULL,
  `luong` int(11) NOT NULL,
  `sdt` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `gioi_tinh` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `role` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_users`
--

LOCK TABLES `my_users` WRITE;
/*!40000 ALTER TABLE `my_users` DISABLE KEYS */;
INSERT INTO `my_users` VALUES (1,'pbkdf2_sha256$120000$Nw4Od25u4r8N$IZcRXE5qAw2H3HhvozOq+czNxXhNc98mBXLjeqDDQ3w=','2019-04-11 03:49:46.960328','',1,1,'','','cuong','2019-03-19',0,'012','','2019-03-19 16:46:45.820110',0,'admin',1,'1','0'),(2,'pbkdf2_sha256$120000$zWmJa2tXK79g$mMknaT971W6p3/QiF96FLa/geth/+k6wkym19RKHLEI=','2019-04-01 10:40:35.601606','',0,1,'','','cuong','2019-04-01',0,'123','','2019-04-01 10:20:00.718408',0,'cuong',1,'',''),(4,'pbkdf2_sha256$120000$LWhyllXNjDSJ$+E8Lvabw3AbaZW2dqsVsLsRZwpfIAFXBiTMqrLULz5c=',NULL,'001HH',0,1,'01TTT','acaca','xxxxx','2019-04-02',0,'123123213','nam','2019-04-02 02:27:47.424545',2,'11111duccuongdc97@gmail.com',1,'hoangduccuong97@gmail.com','users/51464652_1217329338429716_7154108152860901376_o.jpg'),(6,'pbkdf2_sha256$120000$bRJjCUVKdATt$x4ZTlwYZtjJrl/V8z0B02GE4YJHnDwbLGPmtNUFmVEE=',NULL,'001HH',0,1,'01TTT','123213213','dsasadas','1990-09-09',11111,'123213','nu','2019-04-02 02:29:04.081433',1,'1232131231',1,'cuong1@yahoo.com','users/54523021_2236854019960587_7592170919854866432_n.jpg'),(7,'pbkdf2_sha256$120000$GiAAJaLqLxsf$vKJTMxKpxBDerUNa1NTIyTWB2rP9quY0W+CKy9aAZZY=',NULL,'001HH',0,1,'01TTT','123213213','asas','1990-09-09',11111,'123213','nu','2019-04-02 02:30:15.911394',1,'12321312311',1,'cuong11@yahoo.com','users/wolf_howling_at_the_moon-wallpaper-1920x1080.jpg'),(8,'pbkdf2_sha256$120000$QBIQ6DoRTtrh$j+1Rt5y/5txciG57XKRF4JyZfN33Fqo/UqmUmBtZxRw=',NULL,'027HH',0,1,'02TTT','sdsad','dasdsad','1990-09-09',111,'0343944610','nam','2019-04-08 04:39:49.418677',1,'asdsad',1,'duccuonssgdc97@gmail.com','users/52717566_2399793040243727_1478093998278049792_n.jpg'),(9,'pbkdf2_sha256$120000$8LaZ1tE7fgzV$AqPEHdkHnnho+lOd7FjwiunOZKff5Y9iqhKZikE/W9w=',NULL,'006HH',0,1,'01TTT','xzcvzc','cuong n','1997-11-05',1212,'0343944610','nu','2019-04-08 04:44:07.568861',2,'adminasdas',1,'duccuongdc97asda@gmail.com','users/53429827_824071307927970_5228132529709514752_n.jpg'),(11,'pbkdf2_sha256$120000$t0r9MtlSnMBZ$HwM9zIXzEmvky2slJMh/J6+JULrqWP9RKqpqmQezKvE=',NULL,'043HH',0,1,'04TTT','','dbfdbfgnn','1997-11-11',0,'342423','nam','2019-04-08 16:18:51.727554',3,'yjkyuk',1,'cuong3@cus.com','users/52365675_1227509464078370_9117898356008419328_o_2U6Yok0.png'),(12,'pbkdf2_sha256$120000$cayIFBoabWQE$PAEbMMNqqSu2m5XMo+VoAKdff1kiIz5zX9M7RLrGsJc=',NULL,'',0,1,'','','cuong','2019-04-10',0,'','','2019-04-10 16:39:35.739161',3,'cuong1221',1,'cuong1222@gmail.com',''),(13,'pbkdf2_sha256$120000$m0e5QQ9zTjcx$uwjdjUO/ofPgC9TZQU7Z96sv6aF4Y2bJutc41PMkqNY=','2019-04-10 16:50:22.697676','',0,1,'','','zssss','2019-04-10',0,'','','2019-04-10 16:40:57.417022',3,'cuong12@gmail.com',1,'duccuongdc97ssss@gmail.com',''),(14,'pbkdf2_sha256$120000$6RIzuQs13fqR$BfFn1ZiicMSpH8TEqZog2yNah5B5fc0xnuzaTYvzcNw=','2019-04-10 16:52:47.939351','',0,1,'','','cuong','2019-04-10',0,'','','2019-04-10 16:50:51.250193',3,'cuongnhung',1,'cuongnhung12@gmail.com',''),(15,'pbkdf2_sha256$120000$Uf6LJy8owLRH$9zd1u8hT83NZbqB+1Q6gSOy5g7W+5OcAuY7ilnsrrSw=','2019-04-10 17:29:32.935131','',0,1,'','','nhung cuong','2019-04-10',0,'','','2019-04-10 16:53:25.404843',3,'nhungcuong',1,'nhungcuong@gmail.com',''),(16,'pbkdf2_sha256$120000$sXkJGaw5kQaE$cH04nXYEH1scoW7twvU/mEOcWXMkyonnMHyjalHsKcs=','2019-04-12 05:08:06.863168','',0,1,'','asdasdasd','cuong','2019-04-11',0,'0343944610','nam','2019-04-11 03:12:07.555318',3,'cuongdz',1,'cuongdz@gmail.com','users/50986818_1388739007928636_6252149215221252096_o.jpg');
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
  `ten` longtext COLLATE utf8_unicode_ci NOT NULL,
  `sdt` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `dia_chi` longtext COLLATE utf8_unicode_ci NOT NULL,
  `huyen` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tinh` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `is_active` int(11) NOT NULL,
  `mo_ta` longtext COLLATE utf8_unicode_ci NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nha_cung_cap`
--

LOCK TABLES `nha_cung_cap` WRITE;
/*!40000 ALTER TABLE `nha_cung_cap` DISABLE KEYS */;
INSERT INTO `nha_cung_cap` VALUES (1,'cuong','0343944610','hoangduccuong97@gmail.com','asdasd','001HH','01TTT',0,'asdasdsa','2019-03-22'),(2,'asd','03439446101','hoangduccuong97@gmail.com','asdasd','001HH','01TTT',1,'asdasdsa','2019-03-22');
/*!40000 ALTER TABLE `nha_cung_cap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_nhap`
--

DROP TABLE IF EXISTS `phieu_nhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phieu_nhap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thoi_gian_nhap` datetime(6) NOT NULL,
  `ghi_chu` longtext COLLATE utf8_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `nguoi_tao_id` int(11) DEFAULT NULL,
  `nha_cung_cap_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `phieu_nhap_nguoi_tao_id_82e10138_fk_my_users_id` (`nguoi_tao_id`),
  KEY `phieu_nhap_nha_cung_cap_id_f6798100_fk_nha_cung_cap_id` (`nha_cung_cap_id`),
  CONSTRAINT `phieu_nhap_nguoi_tao_id_82e10138_fk_my_users_id` FOREIGN KEY (`nguoi_tao_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `phieu_nhap_nha_cung_cap_id_f6798100_fk_nha_cung_cap_id` FOREIGN KEY (`nha_cung_cap_id`) REFERENCES `nha_cung_cap` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_nhap`
--

LOCK TABLES `phieu_nhap` WRITE;
/*!40000 ALTER TABLE `phieu_nhap` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu_nhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_tra_hang`
--

DROP TABLE IF EXISTS `phieu_tra_hang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phieu_tra_hang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thoi_gian_tra` datetime(6) NOT NULL,
  `ghi_chu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `khach_hang_tra_id` int(11) DEFAULT NULL,
  `nguoi_ban_id` int(11) DEFAULT NULL,
  `nguoi_tao_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `phieu_tra_hang_khach_hang_tra_id_f6128ad1_fk_my_users_id` (`khach_hang_tra_id`),
  KEY `phieu_tra_hang_nguoi_ban_id_bb3414fc_fk_my_users_id` (`nguoi_ban_id`),
  KEY `phieu_tra_hang_nguoi_tao_id_a43824e4_fk_my_users_id` (`nguoi_tao_id`),
  CONSTRAINT `phieu_tra_hang_khach_hang_tra_id_f6128ad1_fk_my_users_id` FOREIGN KEY (`khach_hang_tra_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `phieu_tra_hang_nguoi_ban_id_bb3414fc_fk_my_users_id` FOREIGN KEY (`nguoi_ban_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `phieu_tra_hang_nguoi_tao_id_a43824e4_fk_my_users_id` FOREIGN KEY (`nguoi_tao_id`) REFERENCES `my_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_tra_hang`
--

LOCK TABLES `phieu_tra_hang` WRITE;
/*!40000 ALTER TABLE `phieu_tra_hang` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu_tra_hang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_tra_hang_nhap`
--

DROP TABLE IF EXISTS `phieu_tra_hang_nhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phieu_tra_hang_nhap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thoi_gian_tao` datetime(6) NOT NULL,
  `ghi_chu` longtext COLLATE utf8_unicode_ci,
  `nguoi_tao_id` int(11) DEFAULT NULL,
  `nha_cung_cap_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `phieu_tra_hang_nhap_nguoi_tao_id_27f22d29_fk_my_users_id` (`nguoi_tao_id`),
  KEY `phieu_tra_hang_nhap_nha_cung_cap_id_9ee9742a_fk_nha_cung_cap_id` (`nha_cung_cap_id`),
  CONSTRAINT `phieu_tra_hang_nhap_nguoi_tao_id_27f22d29_fk_my_users_id` FOREIGN KEY (`nguoi_tao_id`) REFERENCES `my_users` (`id`),
  CONSTRAINT `phieu_tra_hang_nhap_nha_cung_cap_id_9ee9742a_fk_nha_cung_cap_id` FOREIGN KEY (`nha_cung_cap_id`) REFERENCES `nha_cung_cap` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_tra_hang_nhap`
--

LOCK TABLES `phieu_tra_hang_nhap` WRITE;
/*!40000 ALTER TABLE `phieu_tra_hang_nhap` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu_tra_hang_nhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_xuat_huy`
--

DROP TABLE IF EXISTS `phieu_xuat_huy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phieu_xuat_huy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thoi_gian_tao` datetime(6) NOT NULL,
  `ghi_chu` longtext COLLATE utf8_unicode_ci,
  `nguoi_tao_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `phieu_xuat_huy_nguoi_tao_id_8608d881_fk_my_users_id` (`nguoi_tao_id`),
  CONSTRAINT `phieu_xuat_huy_nguoi_tao_id_8608d881_fk_my_users_id` FOREIGN KEY (`nguoi_tao_id`) REFERENCES `my_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_xuat_huy`
--

LOCK TABLES `phieu_xuat_huy` WRITE;
/*!40000 ALTER TABLE `phieu_xuat_huy` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu_xuat_huy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `san_pham`
--

DROP TABLE IF EXISTS `san_pham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `san_pham` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ten_san_pham` longtext COLLATE utf8_unicode_ci NOT NULL,
  `ngay_them` date NOT NULL,
  `gia_von` int(11) NOT NULL,
  `gia_ban` int(11) NOT NULL,
  `so_luong` int(11) NOT NULL,
  `ton_kho` int(11) NOT NULL,
  `is_active` int(11) NOT NULL,
  `loai_hang_id` int(11) DEFAULT NULL,
  `mo_ta` longtext COLLATE utf8_unicode_ci NOT NULL,
  `nha_cung_cap_id` int(11) DEFAULT NULL,
  `avt` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `san_pham_nha_cung_cap_id_7c1fe04c_fk_nha_cung_cap_id` (`nha_cung_cap_id`),
  KEY `san_pham_loai_hang_id_d40b1e9a` (`loai_hang_id`),
  CONSTRAINT `san_pham_loai_hang_id_d40b1e9a_fk_loai_hang_id` FOREIGN KEY (`loai_hang_id`) REFERENCES `loai_hang` (`id`),
  CONSTRAINT `san_pham_nha_cung_cap_id_7c1fe04c_fk_nha_cung_cap_id` FOREIGN KEY (`nha_cung_cap_id`) REFERENCES `nha_cung_cap` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `san_pham`
--

LOCK TABLES `san_pham` WRITE;
/*!40000 ALTER TABLE `san_pham` DISABLE KEYS */;
INSERT INTO `san_pham` VALUES (1,'ADA','2019-03-26',1,1,1,1,1,1,'1sa',1,''),(11,'asd','2019-03-27',122,12,1212,1212,1,1,'1212',1,'product/avatar/52911406_373731700132772_3554804893463352876_n.jpg'),(13,'112','2019-03-28',222,222,222,222,1,1,'2222',2,'product/avatar/52474510_432052677334776_1864900870374686720_n.jpg'),(14,'asd','2019-03-28',123,123,123,123,1,1,'asdasd',2,'product/avatar/52886948_587062731761735_3433025242967048192_n_E55YMXB.jpg'),(15,'gfhfghfg','2019-04-11',1000,1000,10,10,1,1,'sdfsdfsdf',1,'product/avatar/50104288_10210432821895701_4407942665509797888_n.jpg'),(16,'121321','2019-04-11',1000,1000,10,10,1,1,'sdfsdfsdf',2,'product/avatar/52712959_114934412973205_8935315727137636352_n.jpg'),(17,'121321','2019-04-11',1000,1000,10,10,1,1,'sdfsdfsdf',2,'product/avatar/52712959_114934412973205_8935315727137636352_n_yNmENze.jpg'),(18,'121321','2019-04-11',1000,1000,10,10,1,2,'sdfsdfsdf',1,'product/avatar/52712959_114934412973205_8935315727137636352_n_liKfzTl.jpg'),(19,'121321','2019-04-11',1000,1000,10,10,1,2,'sdfsdfsdf',1,'product/avatar/52712959_114934412973205_8935315727137636352_n_ZH8cz9E.jpg'),(20,'vcvxv','2019-04-11',11212,121212,1111,1111,1,1,'ssadfasd',1,'product/avatar/20507448_823385014490819_4872274261724149439_o.png'),(21,'vcvxv','2019-04-11',11212,121212,1111,1111,1,2,'ssadfasd',2,'product/avatar/20507448_823385014490819_4872274261724149439_o_YH6WIgJ.png'),(22,'vcvxv','2019-04-11',11212,121212,1111,1111,1,2,'ssadfasd',1,'product/avatar/20507448_823385014490819_4872274261724149439_o_s1PIeEL.png'),(23,'vcvxv','2019-04-11',11212,121212,1111,1111,1,2,'ssadfasd',2,'product/avatar/20507448_823385014490819_4872274261724149439_o_tVmPFm7.png'),(24,'vcvxv','2019-04-11',11212,121212,1111,1111,1,2,'ssadfasd',1,'product/avatar/20507448_823385014490819_4872274261724149439_o_DNbdqPE.png');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `so_quy`
--

LOCK TABLES `so_quy` WRITE;
/*!40000 ALTER TABLE `so_quy` DISABLE KEYS */;
/*!40000 ALTER TABLE `so_quy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-13 14:16:16
