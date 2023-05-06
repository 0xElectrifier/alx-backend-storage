-- Script that creates a trigger that decreases the quantity of
-- an item after adding a new order
-- DELIMITER //;
CREATE TRIGGER dec_quantity
    BEFORE INSERT
    ON `orders` FOR EACH ROW
       UPDATE `items`
          SET `items`.`quantity` = `items`.`quantity` - NEW.number
	WHERE `name` = NEW.item_name;
