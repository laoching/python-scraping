#mysql은 기본적으로 유니코드를 처리하지 않기 때문에 기본 문자셋을 utf8mb4_unicode_ci로 바꿔준다.
#이 파일은 직접 db에 쳐줘야 하는 mysql 명령어임

ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE title title VARCAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE  utf8mb4_unicode_ci;