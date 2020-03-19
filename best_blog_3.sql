-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2020 at 07:18 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `best_blog_3`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'Nadim', '01639508333', 'oh', '2020-02-19 13:52:23', 'www.nadim77@gmail.com'),
(2, 'Nadim', '7897851252', 'dakhlam', '2020-03-19 13:38:23', 'www.nadim77@gmail.com'),
(3, 'Nadim', '7897851252', 'dekhlam', '2020-03-19 13:40:38', 'www.nadim77@gmail.com'),
(4, 'Nadim', '7897851252', 'dekhlam', '2020-03-19 13:42:55', 'www.nadim77@gmail.com'),
(5, 'Nadim', '7897851252', 'dekhlam', '2020-03-19 13:43:15', 'www.nadim77@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `postss`
--

CREATE TABLE `postss` (
  `sno` int(100) NOT NULL,
  `title` text NOT NULL,
  `slug` int(50) NOT NULL,
  `content` text NOT NULL,
  `tagline` text NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `postss`
--

INSERT INTO `postss` (`sno`, `title`, `slug`, `content`, `tagline`, `img_file`, `date`) VALUES
(17, 'ghg', 4, 'fgvhbn', 'ghjkl', 'ik.png', '2020-03-18 15:47:33'),
(18, 'yty', 12, 'kjhgfdsser', 'gfdryh', 'oi.png', '2020-03-17 20:40:27'),
(19, '', 0, ' \"\"', '', '', '2020-03-19 00:01:12'),
(20, 'das', 0, 'cvbn', 'fg', 'rt', '2020-03-17 22:25:50'),
(21, 'cds', 0, 'dfghj', 'vb', 'df', '2020-03-17 23:44:15'),
(22, 'bvn', 0, ' \"sdbvn,olempyc', 'acv', 'v', '2020-03-19 00:20:51'),
(23, 'ioit', 15, ' \"sdfghj\"', 'dnm', 'home-bg.jpg', '2020-03-19 13:55:14'),
(24, 'df', 12, 'dfghbnm', 'cvb', 'ko', '2020-03-18 19:43:13'),
(26, 'ami', 54, 'f', 'bn', 'nmm', '2020-03-18 20:02:10'),
(29, 'pkn', 0, 'vbnm', '', '', '2020-03-18 23:07:45'),
(30, '5', 0, ' \"\"bn m', '', '', '2020-03-19 00:08:40'),
(31, 'last', 0, ' \"\"sdfghjm', '', '', '2020-03-19 00:11:32'),
(32, 'atlast', 15, ' \"\"mkfmd;v', 'po', 'im.png', '2020-03-19 00:22:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `postss`
--
ALTER TABLE `postss`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `postss`
--
ALTER TABLE `postss`
  MODIFY `sno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
