-- 코드를 입력하세요
SELECT * 
FROM 
(SELECT DATETIME AS 시간 
FROM ANIMAL_INS 
ORDER BY DATETIME ) a 
WHERE ROWNUM = 1 