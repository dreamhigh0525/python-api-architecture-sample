CREATE TABLE IF NOT EXISTS `inference`(
    `id` TEXT NOT NULL,
    `category` TEXT NOT NULL,
    `url` TEXT NOT NULL,
    `label` INTEGER NOT NULL,
    `confidence` REAL NOT NULL
)