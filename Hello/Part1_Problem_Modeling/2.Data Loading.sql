#Verify whether hellofresh database is created or not
#
show databases;

-- -----------------------------------------------------
-- use hellofresh
-- -----------------------------------------------------
#use hellofresh schema#

use hellofresh;


#verify the tables#
show tables;


#check for the secure file location to save csv files for loading data.
#
SHOW VARIABLES LIKE "secure_file_priv";



#check the recipe_ratings table structure
#
DESCRIBE recipe_ratings;



-- -----------------------------------------------------
-- Load recipe_ratings from csv file
-- -----------------------------------------------------
#Load data from csv file#
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/recipe_ratings.csv' 

INTO TABLE recipe_ratings 

FIELDS TERMINATED BY ',' 

ENCLOSED BY '"'

LINES TERMINATED BY '\n';



#verfiy loaded data#

SELECT 
    *
FROM
    recipe_ratings;
    


#check ingredients table structure
#
DESCRIBE ingredients;


-- -----------------------------------------------------
-- Load ingredients data
-- -----------------------------------------------------

#Load data

#
#got data truncated error. fixed the value. lets use txt file
#
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ingredients.txt' 

INTO TABLE ingredients 

FIELDS TERMINATED BY '\t' 

ENCLOSED BY '"'

LINES TERMINATED BY '\n';



#verify data
#
SELECT 
    *
FROM
    ingredients;