-- Əsas verilənlər bazası yaradılması
CREATE DATABASE IF NOT EXISTS `InsanDostlari` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `InsanDostlari`;

-- Ev heyvanları cədvəli
CREATE TABLE IF NOT EXISTS `EvHeyvanlari` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `ad` VARCHAR(100) NOT NULL,
    `növ` VARCHAR(50) NOT NULL,
    `dogum_tarixi` DATE NOT NULL,
    `komandalar` TEXT,
    `yaradilma_tarixi` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Yük heyvanları cədvəli
CREATE TABLE IF NOT EXISTS `YukHeyvanlari` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `ad` VARCHAR(100) NOT NULL,
    `növ` VARCHAR(50) NOT NULL,
    `dogum_tarixi` DATE NOT NULL,
    `komandalar` TEXT,
    `yaradilma_tarixi` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Gənc heyvanlar cədvəli
CREATE TABLE IF NOT EXISTS `GencHeyvanlar` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `ad` VARCHAR(100) NOT NULL,
    `növ` VARCHAR(50) NOT NULL,
    `dogum_tarixi` DATE NOT NULL,
    `ay_ile_yas` INT NOT NULL,
    `orijinal_cedvel` VARCHAR(50) NOT NULL,
    `komandalar` TEXT,
    `yaradilma_tarixi` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Atlar və eşşəklər cədvəli
CREATE TABLE IF NOT EXISTS `AtlarVeEshekler` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `ad` VARCHAR(100) NOT NULL,
    `növ` VARCHAR(50) NOT NULL,
    `dogum_tarixi` DATE NOT NULL,
    `komandalar` TEXT,
    `yaradilma_tarixi` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;