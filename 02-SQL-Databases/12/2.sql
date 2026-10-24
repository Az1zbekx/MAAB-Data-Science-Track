CREATE OR ALTER PROCEDURE usp_GetProceduresAndFunctions
    @DatabaseName NVARCHAR(128) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @SQL NVARCHAR(MAX) = N'';

    IF @DatabaseName IS NOT NULL
    BEGIN
        SET @SQL = '
        USE [' + @DatabaseName + '];
        SELECT 
            DB_NAME() AS DatabaseName,
            s.name AS SchemaName,
            o.name AS ObjectName,
            o.type_desc AS ObjectType,
            p.name AS ParameterName,
            t.name AS DataType,
            p.max_length AS MaxLength
        FROM sys.objects o
        INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
        LEFT JOIN sys.parameters p ON o.object_id = p.object_id
        LEFT JOIN sys.types t ON p.user_type_id = t.user_type_id
        WHERE o.type IN (''P'', ''FN'', ''TF'', ''IF'')
        ORDER BY s.name, o.name;';
        EXEC sp_executesql @SQL;
    END
    ELSE
    BEGIN
        DECLARE @DB NVARCHAR(128);

        DECLARE db_cursor CURSOR FOR
        SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');

        OPEN db_cursor;
        FETCH NEXT FROM db_cursor INTO @DB;

        WHILE @@FETCH_STATUS = 0
        BEGIN
            SET @SQL = '
            USE [' + @DB + '];
            SELECT 
                DB_NAME() AS DatabaseName,
                s.name AS SchemaName,
                o.name AS ObjectName,
                o.type_desc AS ObjectType,
                p.name AS ParameterName,
                t.name AS DataType,
                p.max_length AS MaxLength
            FROM sys.objects o
            INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
            LEFT JOIN sys.parameters p ON o.object_id = p.object_id
            LEFT JOIN sys.types t ON p.user_type_id = t.user_type_id
            WHERE o.type IN (''P'', ''FN'', ''TF'', ''IF'')
            ORDER BY s.name, o.name;';

            EXEC sp_executesql @SQL;
            FETCH NEXT FROM db_cursor INTO @DB;
        END

        CLOSE db_cursor;
        DEALLOCATE db_cursor;
    END
END;
