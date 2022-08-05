-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 02, 2022 at 09:02 AM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `reserv`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_airplane`
--

CREATE TABLE `add_airplane` (
  `login_id` varchar(100) NOT NULL,
  `staff_username` varchar(300) NOT NULL,
  `staff_password` varchar(200) NOT NULL,
  `airline_name` varchar(80) NOT NULL,
  `id_num` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `add_airport`
--

CREATE TABLE `add_airport` (
  `login_id` varchar(100) NOT NULL,
  `staff_username` varchar(300) NOT NULL,
  `staff_password` varchar(200) NOT NULL,
  `airport_name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `airline_name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `staff_username` varchar(300) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `airline_name` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airline_name` varchar(80) NOT NULL,
  `id_num` varchar(50) NOT NULL,
  `num_seats` int(10) DEFAULT NULL,
  `manufactoring_company` varchar(80) DEFAULT NULL,
  `age` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `airport_name` varchar(80) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `attempt_purchase`
--

CREATE TABLE `attempt_purchase` (
  `cust_email` varchar(320) NOT NULL,
  `ticket_id` varchar(15) NOT NULL,
  `card_number` varchar(20) DEFAULT NULL,
  `card_name` varchar(80) DEFAULT NULL,
  `exp_date` varchar(20) DEFAULT NULL,
  `purchase_date_time` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cancel_ticket`
--

CREATE TABLE `cancel_ticket` (
  `ticket_id` varchar(15) NOT NULL,
  `cust_email` varchar(320) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `create_review`
--

CREATE TABLE `create_review` (
  `ticket_id` varchar(15) NOT NULL,
  `cust_email` varchar(320) NOT NULL,
  `login_id` varchar(100) NOT NULL,
  `cust_password` varchar(200) NOT NULL,
  `cust_comment` varchar(10000) DEFAULT NULL,
  `cust_rating` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `create_set_price`
--

CREATE TABLE `create_set_price` (
  `login_id` varchar(100) NOT NULL,
  `staff_password` varchar(200) NOT NULL,
  `staff_username` varchar(300) NOT NULL,
  `flight_number` varchar(10) NOT NULL,
  `airline_name` varchar(80) NOT NULL,
  `departure_date_time` varchar(30) NOT NULL,
  `base_price` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cust_email` varchar(320) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `building_number` varchar(50) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `passport_number` varchar(20) DEFAULT NULL,
  `passport_expiration` varchar(20) DEFAULT NULL,
  `passport_country` varchar(60) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `email`
--

CREATE TABLE `email` (
  `email_staff` varchar(320) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `airline_name` varchar(80) NOT NULL,
  `flight_number` varchar(10) NOT NULL,
  `departure_date_time` varchar(30) NOT NULL,
  `departure_airport` varchar(80) NOT NULL,
  `arrival_airport` varchar(80) NOT NULL,
  `arrival_date_time` varchar(30) DEFAULT NULL,
  `base_price` int(10) DEFAULT NULL,
  `id_num` varchar(50) NOT NULL,
  `flight_status` varchar(10) DEFAULT NULL,
  `departure_date` varchar(10) DEFAULT NULL,
  `return_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `login_cust`
--

CREATE TABLE `login_cust` (
  `login_id` varchar(100) NOT NULL,
  `cust_email` varchar(320) NOT NULL,
  `cust_password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `login_staff`
--

CREATE TABLE `login_staff` (
  `login_id` varchar(100) NOT NULL,
  `staff_username` varchar(300) NOT NULL,
  `staff_password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `phone_number`
--

CREATE TABLE `phone_number` (
  `staff_phone_num` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `set_flight_status`
--

CREATE TABLE `set_flight_status` (
  `login_id` varchar(100) NOT NULL,
  `staff_username` varchar(300) NOT NULL,
  `staff_password` varchar(200) NOT NULL,
  `flight_number` varchar(10) NOT NULL,
  `airline_name` varchar(80) NOT NULL,
  `departure_date_time` varchar(30) NOT NULL,
  `new_status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `staff_email`
--

CREATE TABLE `staff_email` (
  `staff_username` varchar(300) NOT NULL,
  `email_staff` varchar(320) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `staff_phone`
--

CREATE TABLE `staff_phone` (
  `staff_username` varchar(300) NOT NULL,
  `staff_phone_num` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `ticket_id` varchar(15) NOT NULL,
  `cust_email` varchar(320) DEFAULT NULL,
  `airline_name` varchar(80) DEFAULT NULL,
  `flight_number` varchar(10) NOT NULL,
  `sold_price` int(10) DEFAULT NULL,
  `card_number` varchar(20) DEFAULT NULL,
  `card_name` varchar(80) DEFAULT NULL,
  `exp_date` varchar(20) DEFAULT NULL,
  `purchase_date_time` varchar(30) DEFAULT NULL,
  `card_type` varchar(10) DEFAULT NULL,
  `purchase_date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_airplane`
--
ALTER TABLE `add_airplane`
  ADD PRIMARY KEY (`login_id`,`staff_username`,`staff_password`,`airline_name`,`id_num`),
  ADD KEY `airline_name` (`airline_name`,`id_num`);

--
-- Indexes for table `add_airport`
--
ALTER TABLE `add_airport`
  ADD PRIMARY KEY (`login_id`,`staff_username`,`staff_password`,`airport_name`),
  ADD KEY `airport_name` (`airport_name`);

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`airline_name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`staff_username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`airline_name`,`id_num`),
  ADD UNIQUE KEY `id_num` (`id_num`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`airport_name`);

--
-- Indexes for table `attempt_purchase`
--
ALTER TABLE `attempt_purchase`
  ADD PRIMARY KEY (`cust_email`,`ticket_id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Indexes for table `cancel_ticket`
--
ALTER TABLE `cancel_ticket`
  ADD PRIMARY KEY (`ticket_id`,`cust_email`),
  ADD KEY `cust_email` (`cust_email`);

--
-- Indexes for table `create_review`
--
ALTER TABLE `create_review`
  ADD PRIMARY KEY (`ticket_id`,`cust_email`,`login_id`,`cust_password`),
  ADD KEY `login_id` (`login_id`,`cust_email`,`cust_password`);

--
-- Indexes for table `create_set_price`
--
ALTER TABLE `create_set_price`
  ADD PRIMARY KEY (`login_id`,`staff_username`,`staff_password`,`flight_number`,`airline_name`,`departure_date_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date_time`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cust_email`);

--
-- Indexes for table `email`
--
ALTER TABLE `email`
  ADD PRIMARY KEY (`email_staff`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`departure_date_time`),
  ADD UNIQUE KEY `flight_number` (`flight_number`),
  ADD KEY `departure_airport` (`departure_airport`),
  ADD KEY `arrival_airport` (`arrival_airport`),
  ADD KEY `airplane_id_num` (`id_num`);

--
-- Indexes for table `login_cust`
--
ALTER TABLE `login_cust`
  ADD PRIMARY KEY (`login_id`,`cust_email`,`cust_password`),
  ADD KEY `cust_email` (`cust_email`);

--
-- Indexes for table `login_staff`
--
ALTER TABLE `login_staff`
  ADD PRIMARY KEY (`login_id`,`staff_username`,`staff_password`),
  ADD KEY `staff_username` (`staff_username`);

--
-- Indexes for table `phone_number`
--
ALTER TABLE `phone_number`
  ADD PRIMARY KEY (`staff_phone_num`);

--
-- Indexes for table `set_flight_status`
--
ALTER TABLE `set_flight_status`
  ADD PRIMARY KEY (`login_id`,`staff_username`,`staff_password`,`airline_name`,`flight_number`,`departure_date_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date_time`);

--
-- Indexes for table `staff_email`
--
ALTER TABLE `staff_email`
  ADD PRIMARY KEY (`staff_username`,`email_staff`),
  ADD KEY `email_staff` (`email_staff`);

--
-- Indexes for table `staff_phone`
--
ALTER TABLE `staff_phone`
  ADD PRIMARY KEY (`staff_username`,`staff_phone_num`),
  ADD KEY `staff_phone_num` (`staff_phone_num`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ticket_id`),
  ADD KEY `cust_email` (`cust_email`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `flight_num` (`flight_number`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `add_airplane`
--
ALTER TABLE `add_airplane`
  ADD CONSTRAINT `add_airplane_ibfk_1` FOREIGN KEY (`login_id`,`staff_username`,`staff_password`) REFERENCES `login_staff` (`login_id`, `staff_username`, `staff_password`),
  ADD CONSTRAINT `add_airplane_ibfk_2` FOREIGN KEY (`airline_name`,`id_num`) REFERENCES `airplane` (`airline_name`, `id_num`);

--
-- Constraints for table `add_airport`
--
ALTER TABLE `add_airport`
  ADD CONSTRAINT `add_airport_ibfk_1` FOREIGN KEY (`login_id`,`staff_username`,`staff_password`) REFERENCES `login_staff` (`login_id`, `staff_username`, `staff_password`),
  ADD CONSTRAINT `add_airport_ibfk_2` FOREIGN KEY (`airport_name`) REFERENCES `airport` (`airport_name`);

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`);

--
-- Constraints for table `attempt_purchase`
--
ALTER TABLE `attempt_purchase`
  ADD CONSTRAINT `attempt_purchase_ibfk_1` FOREIGN KEY (`cust_email`) REFERENCES `customer` (`cust_email`),
  ADD CONSTRAINT `attempt_purchase_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`);

--
-- Constraints for table `cancel_ticket`
--
ALTER TABLE `cancel_ticket`
  ADD CONSTRAINT `cancel_ticket_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`),
  ADD CONSTRAINT `cancel_ticket_ibfk_2` FOREIGN KEY (`cust_email`) REFERENCES `customer` (`cust_email`);

--
-- Constraints for table `create_review`
--
ALTER TABLE `create_review`
  ADD CONSTRAINT `create_review_ibfk_1` FOREIGN KEY (`login_id`,`cust_email`,`cust_password`) REFERENCES `login_cust` (`login_id`, `cust_email`, `cust_password`),
  ADD CONSTRAINT `create_review_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`);

--
-- Constraints for table `create_set_price`
--
ALTER TABLE `create_set_price`
  ADD CONSTRAINT `create_set_price_ibfk_1` FOREIGN KEY (`login_id`,`staff_username`,`staff_password`) REFERENCES `login_staff` (`login_id`, `staff_username`, `staff_password`),
  ADD CONSTRAINT `create_set_price_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_date_time`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`departure_airport`) REFERENCES `airport` (`airport_name`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`arrival_airport`) REFERENCES `airport` (`airport_name`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`id_num`) REFERENCES `airplane` (`id_num`);

--
-- Constraints for table `login_cust`
--
ALTER TABLE `login_cust`
  ADD CONSTRAINT `login_cust_ibfk_1` FOREIGN KEY (`cust_email`) REFERENCES `customer` (`cust_email`);

--
-- Constraints for table `login_staff`
--
ALTER TABLE `login_staff`
  ADD CONSTRAINT `login_staff_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `airline_staff` (`staff_username`);

--
-- Constraints for table `set_flight_status`
--
ALTER TABLE `set_flight_status`
  ADD CONSTRAINT `set_flight_status_ibfk_1` FOREIGN KEY (`login_id`,`staff_username`,`staff_password`) REFERENCES `login_staff` (`login_id`, `staff_username`, `staff_password`),
  ADD CONSTRAINT `set_flight_status_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_date_time`);

--
-- Constraints for table `staff_email`
--
ALTER TABLE `staff_email`
  ADD CONSTRAINT `staff_email_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `airline_staff` (`staff_username`),
  ADD CONSTRAINT `staff_email_ibfk_2` FOREIGN KEY (`email_staff`) REFERENCES `email` (`email_staff`);

--
-- Constraints for table `staff_phone`
--
ALTER TABLE `staff_phone`
  ADD CONSTRAINT `staff_phone_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `airline_staff` (`staff_username`),
  ADD CONSTRAINT `staff_phone_ibfk_2` FOREIGN KEY (`staff_phone_num`) REFERENCES `phone_number` (`staff_phone_num`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`cust_email`) REFERENCES `customer` (`cust_email`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`),
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`flight_number`) REFERENCES `flight` (`flight_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
