-- Step 1: Gather Index Metadata
DECLARE @HTMLBody NVARCHAR(MAX)

-- Create HTML Table with Styling
SET @HTMLBody = 
N'<html>
<head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #4CAF50;
  color: white;
}
tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
</head>
<body>
<h3>SQL Server Index Metadata Report</h3>
<table>
<tr>
<th>Table Name</th>
<th>Index Name</th>
<th>Index Type</th>
<th>Column Name</th>
</tr>'

-- Append Table Rows
SELECT @HTMLBody = @HTMLBody + 
N'<tr><td>' + t.name + 
N'</td><td>' + i.name +
N'</td><td>' + i.type_desc +
N'</td><td>' + c.name + 
N'</td></tr>'
FROM sys.tables AS t
INNER JOIN sys.indexes AS i ON t.object_id = i.object_id
INNER JOIN sys.index_columns AS ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
INNER JOIN sys.columns AS c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.is_primary_key = 0  -- Optional: exclude PK
  AND i.is_unique_constraint = 0 -- Optional: exclude unique constraints
ORDER BY t.name, i.name

-- Close HTML
SET @HTMLBody = @HTMLBody + N'</table></body></html>'

-- Step 2: Send Email Using Database Mail
EXEC msdb.dbo.sp_send_dbmail
    @profile_name = 'YourMailProfile',      -- Replace with your mail profile
    @recipients = 'recipient@example.com',  -- Replace with your email
    @subject = 'SQL Server Index Metadata Report',
    @body = @HTMLBody,
    @body_format = 'HTML'
