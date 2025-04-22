RESTORE DATABASE PortfolioProject_MarketingAnalytics
FROM DISK = '/var/opt/mssql/backup/PortfolioProject_MarketingAnalytics.bak'
WITH MOVE 'PortfolioProject_MarketingAnalytics' TO '/var/opt/mssql/data/PortfolioProject_MarketingAnalytics.mdf',
     MOVE 'PortfolioProject_MarketingAnalytics_log' TO '/var/opt/mssql/data/PortfolioProject_MarketingAnalytics_log.ldf',
     REPLACE;
