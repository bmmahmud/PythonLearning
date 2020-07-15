
------------ NDM WISE MTD SALES
SELECT 
[NDM].[NDMNAME] 
,SUM([OESalesDetails].[EXTINVMISC]) AS SALES
FROM [OESalesDetails]
LEFT JOIN [NDM] ON [OESalesDetails].AUDTORG = [NDM].[BRANCH]
Where 
([TRANSDATE] BETWEEN 
convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112) --- FIRST DAY OF CURRENT MONTH
AND 
convert(varchar(8),DATEADD(D,-1,GETDATE()),112)) --- YESTERDAY
GROUP BY [NDM].[NDMNAME]
ORDER BY [NDM].[NDMNAME]


--SELECT TOP 5 * FROM [NDM]
---------- NDM WISE TARGET
SELECT [NDM].[NDMNAME] 
,SUM([TDCL_BranchTarget].[TARGET]) AS NDM_TARGET
FROM [NDM]
LEFT JOIN [TDCL_BranchTarget] ON 
[NDM].[BRANCH]= [TDCL_BranchTarget].[AUDTORG]
WHERE YEARMONTH =(convert(varchar(6),DATEADD(D,-1,GETDATE()),112))
GROUP BY [NDM].[NDMNAME]
ORDER BY [NDM].[NDMNAME]

------------ BRANCH WISE LIVE SALES

--SELECT 
--AUDTORG AS BRANCH
--,Sum(EXTINVMISC) AS LIVE_SALES
--FROM 
--OESalesDetails
--WHERE TRANSDATE = convert(varchar(8),DATEADD(D,0,GETDATE()),112)
--GROUP BY AUDTORG