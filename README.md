<h2> Тестовое задание </h2>

Сперва для запуска нужно переименовать файль .env_example на .env
для получения SERVICE_KEY, нужно  создать приложение на сайте https://vk.com/editapp?act=create
обязательно выбрать опцию Standalone.
Для TOKEN нужно перейти по ссылке https://vkhost.github.io/


<strong> first_command: docker build --tag 'vk_app:0.0.1' . <br/>
second_command: docker run -p 8000:8000 --name app vk_app:0.0.1 </strong>


SQL 

SELECT
    c.ID,
    CONCAT(c.first_name, ' ', c.last_name) AS Name,
    pr.Category,
    GROUP_CONCAT(pur.ProductName ORDER BY pur.ProductName ASC) AS Products
FROM
    Customers c
JOIN (
    SELECT
        p.customer_id,
        pr.name AS ProductName,
        pr.Category,
        COUNT(DISTINCT p.product_id) AS num_products
    FROM
        Purchases p
    JOIN
        Products pr ON p.product_id = pr.ID
    GROUP BY
        p.customer_id, pr.Category
    HAVING
        num_products = 2
) pur ON c.ID = pur.customer_id
JOIN
    Products pr ON pur.Category = pr.Category
WHERE
    c.age >= 18 AND c.age <= 65
GROUP BY
    c.ID, c.first_name, c.last_name, pr.Category
HAVING
    COUNT(DISTINCT pur.ProductName) = 2
