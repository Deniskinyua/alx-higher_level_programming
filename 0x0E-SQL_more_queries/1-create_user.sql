-- Create user & grant all priveleges; If they not exists, script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY user_0d_1_pwd; GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY user_0d_1_pwd;
FLUSH PRIVELEGES;
