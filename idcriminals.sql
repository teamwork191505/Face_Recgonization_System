-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2023 at 09:33 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `criminal_managment_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `idcriminals`
--

CREATE TABLE `idcriminals` (
  `id` int(10) NOT NULL DEFAULT 21,
  `Name` varchar(25) NOT NULL,
  `Birth Date` date NOT NULL,
  `height` int(5) NOT NULL,
  `weight` int(3) NOT NULL,
  `crime place` varchar(30) NOT NULL,
  `crime` varchar(30) NOT NULL,
  `photo` varchar(30) NOT NULL,
  `Address` text NOT NULL DEFAULT 'write null if not available'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
