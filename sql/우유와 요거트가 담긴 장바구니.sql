-- 코드를 입력하세요
SELECT DISTINCT A.CART_ID
FROM CART_PRODUCTS A, CART_PRODUCTS B
WHERE A.CART_ID = B.CART_ID
AND (A.NAME = 'MILK' AND B.NAME = 'YOGURT'
OR A.NAME = 'YOGURT' AND B.NAME = 'MILK')
ORDER BY A.CART_ID;

-- 코드를 입력하세요 서브쿼리
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'MILK'
AND CART_ID IN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'YOGURT')
ORDER BY CART_ID;

-- 코드를 입력하세요
SELECT DISTINCT A.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'YOGURT') A,
(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'MILK') B
WHERE A.CART_ID = B.CART_ID;

-- 코드를 입력하세요 셀프 조인
SELECT DISTINCT A.CART_ID
FROM CART_PRODUCTS A, CART_PRODUCTS B
WHERE A.CART_ID = B.CART_ID
AND A.NAME = 'MILK' AND B.NAME = 'YOGURT'
ORDER BY A.CART_ID;

SELECT DISTINCT(CART_ID) 
FROM CART_PRODUCTS
WHERE CART_ID IN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk')
AND CART_ID IN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt')
ORDER BY CART_ID;
