SELECT DISTINCT
    Category,
    ProductName,
    Price,
    IIF(Stock = 0, 'Out of Stock',
        IIF(Stock BETWEEN 1 AND 10, 'Low Stock', 'In Stock')) AS InventoryStatus
FROM Products p
WHERE Price = (
    SELECT MAX(Price)
    FROM Products
    WHERE Category = p.Category
)
ORDER BY Price DESC
OFFSET 5 ROWS;
