-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2023 at 09:40 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fingerprint`
--

-- --------------------------------------------------------

--
-- Table structure for table `listfinger`
--

CREATE TABLE `listfinger` (
  `ID` int(11) NOT NULL,
  `HoTen` varchar(255) NOT NULL,
  `QueQuan` varchar(255) NOT NULL,
  `Question1` varchar(255) NOT NULL,
  `Answer1` varchar(255) NOT NULL,
  `Question2` varchar(255) NOT NULL,
  `Answer2` varchar(255) NOT NULL,
  `Question3` varchar(255) NOT NULL,
  `Answer3` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `listfinger`
--

INSERT INTO `listfinger` (`ID`, `HoTen`, `QueQuan`, `Question1`, `Answer1`, `Question2`, `Answer2`, `Question3`, `Answer3`) VALUES
(1, 'Trần Văn Đạt', 'Thái Bình', 'Màu sắc yêu thích của bạn là gì?', 'Trắng', 'Người yêu cũ của bạn tên gì', 'Tuyết', 'Con vật cưng của bạn tên là gì?', 'Chó'),
(2, 'Nguyễn Văn Hiếu', 'Nam Định', 'Tên của người bạn đầu tiên khi lên đại học là gì?', 'Thành', 'Bạn có bao nhiêu anh chị em?', 'Ba', 'Bạn yêu thích môn học nào nhất ở trường?', 'Toán'),
(3, 'Hoàng Thành Lợi', 'Hải Dương', 'Bạn thường xuyên chơi trò gì trong thời gian rảnh?', 'Minecraft', 'Ai là người bạn nghĩa vụ tài chính của bạn?', 'Bố', 'Bạn có sở thích hát nào không?', 'Có'),
(4, 'Lâm Thiên Phong', 'Bắc Giang', 'Bạn đã du lịch đến quốc gia nào gần đây nhất?', 'Mỹ', 'Tên của người giáo viên bạn thích nhất là gì?', 'Quyền', 'Tên người bạn cùng phòng cũ khi bạn ở ký túc xá là gì?', 'Khôi'),
(5, 'Khiếu Minh Quang', 'Thái Bình', 'Thành phố bạn muốn đến hơn cả là đâu?', 'Rome', 'Bạn yêu thích loại nhạc nào nhất?', 'Ballad', 'Bạn thường xuyên gặp bạn bè vào thứ mấy trong tuần?', 'Bảy'),
(6, 'Nguyễn Trí Thành', 'Bắc Ninh', 'Bạn thường xuyên đọc sách của tác giả nào?', 'AynRand', 'Mạng xã hội yêu thích của bạn?', 'Instagram', 'Ngôn ngữ Back-end ưa thích của bạn?', 'JS');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listfinger`
--
ALTER TABLE `listfinger`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listfinger`
--
ALTER TABLE `listfinger`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
