CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Orders`
(
    `style_id` TEXT NOT NULL ,
    `size_id` INTEGER NOT NULL,
    `metal_id` TEXT NOT NULL,
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` INTEGER NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

INSERT INTO `Metals` VALUES (1, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (2, '14K Gold', 736.4);
INSERT INTO `Metals` VALUES (3, '24K Gold', 1258.9);
INSERT INTO `Metals` VALUES (4, 'Platinum', 795.45);
INSERT INTO `Metals` VALUES (5, 'Palladium', 1241);

INSERT INTO `Orders` VALUES (1, 1, 1, 1);
INSERT INTO `Orders` VALUES (1, 1, 1, 2);
INSERT INTO `Orders` VALUES (1, 1, 1, 3);
INSERT INTO `Orders` VALUES (1, 1, 1, 4);
INSERT INTO `Orders` VALUES (1, 1, 1, 5);

INSERT INTO `Sizes` VALUES (1, 0.5, 405);
INSERT INTO `Sizes` VALUES (2, 0.75, 782);
INSERT INTO `Sizes` VALUES (3, 1, 1470);
INSERT INTO `Sizes` VALUES (4, 1.5, 1997);
INSERT INTO `Sizes` VALUES (5, 2, 43638);

INSERT INTO `Styles` VALUES (1, 'Classic', 500);
INSERT INTO `Styles` VALUES (2, 'Modern', 710);
INSERT INTO `Styles` VALUES (3, 'Vintage', 965);

SELECT
    m.id,
    m.metal,
    m.price
FROM Metals m
WHERE m.id = 2;

SELECT
    o.style_id,
    o.size_id,
    o.metal_id,
    o.id,
    st.style AS style_style,
    st.price AS style_price,
    m.metal AS metal_metal,
    m.price AS metal_price,
    si.carets AS size_carets,
    si.price AS size_price
FROM Orders o
JOIN Styles st ON o.style_id = st.id
JOIN Metals m ON o.metal_id = m.id
JOIN Sizes si ON o.size_id = si.id
ORDER BY o.id DESC;

SELECT
    si.id,
    si.carets,
    si.price
FROM Sizes si
WHERE si.id = 2;

SELECT
    st.id,
    st.style,
    st.price
FROM Styles st
WHERE st.id = 2;


