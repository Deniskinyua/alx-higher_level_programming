-- Converts hbtn_0c_0 DB to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Convert all of the following to UTF8: -> DB hbtn_0c_0, -> table first_table, -> field name in first_table
USE hbtn_0c_0 ALTER TABLE first_table CONVERT T0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
