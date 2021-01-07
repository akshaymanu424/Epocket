-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 06, 2021 at 09:08 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `epocket`
--

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

CREATE TABLE IF NOT EXISTS `budget` (
  `bugetid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `budgetname` varchar(50) NOT NULL,
  `bfrom` date NOT NULL,
  `bto` date NOT NULL,
  PRIMARY KEY (`bugetid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `budget`
--

INSERT INTO `budget` (`bugetid`, `rid`, `budgetname`, `bfrom`, `bto`) VALUES
(1, 2, 'BUDGET1', '2020-12-01', '2020-12-31');

-- --------------------------------------------------------

--
-- Table structure for table `budgetlist`
--

CREATE TABLE IF NOT EXISTS `budgetlist` (
  `blid` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) NOT NULL,
  `etype` int(11) NOT NULL,
  `amt` int(11) NOT NULL,
  PRIMARY KEY (`blid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `budgetlist`
--

INSERT INTO `budgetlist` (`blid`, `bid`, `etype`, `amt`) VALUES
(1, 1, 1, 3500),
(2, 1, 2, 750),
(3, 1, 4, 6000);

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE IF NOT EXISTS `expense` (
  `eid` int(10) NOT NULL AUTO_INCREMENT,
  `etype` varchar(20) NOT NULL,
  `amt` int(10) NOT NULL,
  `dt` date NOT NULL,
  `rid` int(10) NOT NULL,
  `etypeid` int(11) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`eid`, `etype`, `amt`, `dt`, `rid`, `etypeid`) VALUES
(1, 'aa', 45, '2020-10-01', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `expensetype`
--

CREATE TABLE IF NOT EXISTS `expensetype` (
  `etypeid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `expensetype` varchar(50) NOT NULL,
  PRIMARY KEY (`etypeid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `expensetype`
--

INSERT INTO `expensetype` (`etypeid`, `rid`, `expensetype`) VALUES
(1, 2, 'FOOD'),
(2, 2, 'Current bill'),
(3, 2, 'Water bill'),
(4, 2, 'Rent'),
(5, 4, 'Food'),
(6, 4, 'Travel'),
(7, 5, 'Food'),
(8, 5, 'Travel');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE IF NOT EXISTS `income` (
  `iid` int(10) NOT NULL AUTO_INCREMENT,
  `itype` varchar(20) NOT NULL,
  `amt` int(10) NOT NULL,
  `dt` date NOT NULL,
  `rid` int(10) NOT NULL,
  `itypeid` int(11) NOT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`iid`, `itype`, `amt`, `dt`, `rid`, `itypeid`) VALUES
(1, 'mjbhj', 455, '2020-10-02', 2, 1),
(2, 'oeirjfo', 500, '2020-10-21', 2, 1),
(3, 'lerijgfe', 4780, '2020-10-31', 2, 1),
(4, '2', 10000, '2020-12-26', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `incometype`
--

CREATE TABLE IF NOT EXISTS `incometype` (
  `itypeid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `incometype` varchar(50) NOT NULL,
  PRIMARY KEY (`itypeid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `incometype`
--

INSERT INTO `incometype` (`itypeid`, `rid`, `incometype`) VALUES
(1, 2, 'Salary'),
(2, 2, 'Reimbursement'),
(3, 4, 'Salary'),
(4, 4, 'Household income'),
(5, 5, 'Salary'),
(6, 5, 'Household income');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE IF NOT EXISTS `loan` (
  `loanid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `loanname` varchar(50) NOT NULL,
  `lender` varchar(50) NOT NULL,
  `amount` bigint(20) NOT NULL,
  `sdate` date NOT NULL,
  `interest` float NOT NULL,
  `loanstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`loanid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`loanid`, `rid`, `loanname`, `lender`, `amount`, `sdate`, `interest`, `loanstatus`) VALUES
(1, 2, 'jnh', 'njhjnl', 150000, '2020-02-01', 8.5, 'active');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `lid` int(10) NOT NULL AUTO_INCREMENT,
  `rid` int(10) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pword` varchar(20) NOT NULL,
  `utype` varchar(20) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`lid`, `rid`, `uname`, `pword`, `utype`) VALUES
(1, 2, 'aa@gmail.com', 'aa', 'user'),
(2, 3, 'todlin@gmail.com', 'todlin', 'user'),
(3, 4, 'todlin@gmail.com', 'todlin', 'user'),
(4, 5, 'kuruvila@gmail.com', 'kuruvi', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `reg`
--

CREATE TABLE IF NOT EXISTS `reg` (
  `rid` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  `addr` varchar(40) NOT NULL,
  `place` varchar(30) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `reg`
--

INSERT INTO `reg` (`rid`, `name`, `age`, `addr`, `place`, `dob`, `email`) VALUES
(2, 'aa', 23, 'nilayam', 'aluva', '12-09-1987', 'aa@gmail.com'),
(3, 'Todlin', 28, 'jkdfnvhdn', 'kjnkj', '1992-05-25', 'todlin@gmail.com'),
(4, 'Todlin', 28, 'jkdfnvhdn', 'kjnkj', '1992-05-25', 'todlin@gmail.com'),
(5, 'Kuruvila', 45, 'jhbhjb', 'jhjhb', '1973-08-15', 'kuruvila@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `savings`
--

CREATE TABLE IF NOT EXISTS `savings` (
  `savingsid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `savings` varchar(50) NOT NULL,
  `source` varchar(50) NOT NULL,
  `sdate` date NOT NULL,
  `amount` bigint(20) NOT NULL,
  PRIMARY KEY (`savingsid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `savings`
--

INSERT INTO `savings` (`savingsid`, `rid`, `savings`, `source`, `sdate`, `amount`) VALUES
(1, 1, 'hjbjhb', 'hjnjhj', '2020-12-17', 20000),
(2, 2, 'ijnhjn', 'jbnh', '2021-01-06', 25000);
