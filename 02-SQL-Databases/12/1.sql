DECLARE @SQL NVARCHAR(MAX) = N'';

SELECT @SQL = @SQL + '
USE [' + name + '];
SELECT
    DB_NAME() AS DatabaseName,
    s.name AS SchemaName,
    t.name AS TableName,
    c.name AS ColumnName,
    ty.name AS DataType
FROM sys.schemas s
JOIN sys.tables t ON s.schema_id = t.schema_id
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id;
'
FROM sys.databases
WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');

EXEC sp_executesql @SQL;
