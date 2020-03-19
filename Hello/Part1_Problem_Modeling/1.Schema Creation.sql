-- MySQL Workbench

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hellofresh
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hellofresh
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hellofresh` DEFAULT CHARACTER SET utf8 ;
USE `hellofresh` ;

-- -----------------------------------------------------
-- Table `hellofresh`.`recipe_ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hellofresh`.`recipe_ratings` (
  `recipe_code` VARCHAR(45) NOT NULL,
  `score` FLOAT NULL,
  `new` TINYINT NULL,
  `price` FLOAT NULL,
  PRIMARY KEY (`recipe_code`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hellofresh`.`ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hellofresh`.`ingredients` (
  `recipe_code` VARCHAR(45) NULL,
  `Recipe_name` VARCHAR(180) NULL,
  `Ingredient` VARCHAR(120) NULL,
  `Unit_weight_amount` FLOAT NULL)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
