CREATE TABLE `metric` (
`datacenter` VARCHAR(256) NOT NULL,
`application` VARCHAR(256) NOT NULL,
`name` VARCHAR(256) NOT NULL,
`value` FLOAT NOT NULL,
`timestamp` TIMESTAMP NOT NULL,
INDEX `Index 1` (`datacenter`),
INDEX `Index 2` (`application`),
INDEX `Index 3` (`timestamp`),
INDEX `Index 4` (`name`)
)
COLLATE='utf8_general_ci'
;