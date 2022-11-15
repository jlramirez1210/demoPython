/*
Navicat MySQL Data Transfer

Source Server         : local_server
Source Server Version : 80031
Source Host           : localhost:3306
Source Database       : used_car_prices

Target Server Type    : MYSQL
Target Server Version : 80031
File Encoding         : 65001

Date: 2022-11-15 01:06:30
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `precio_autos`
-- ----------------------------
DROP TABLE IF EXISTS `precio_autos`;
CREATE TABLE `precio_autos` (
  `index` int NOT NULL,
  `car_model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `year_of_manufacture` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `fuel` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of precio_autos
-- ----------------------------

-- ----------------------------
-- Table structure for `precio_modelo`
-- ----------------------------
DROP TABLE IF EXISTS `precio_modelo`;
CREATE TABLE `precio_modelo` (
  `car_model` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of precio_modelo
-- ----------------------------
