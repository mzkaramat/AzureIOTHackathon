WITH dev_1
AS (
	SELECT *
	FROM [iniothub]
	WHERE device_id = 'device_1'
	)
	,dev_2
AS (
	SELECT *
	FROM [iniothub]
	WHERE device_id = 'device_2'
	)
	,dev_3
AS (
	SELECT *
	FROM [iniothub]
	WHERE device_id = 'device_3'
	)
	,merging_df
AS (
	SELECT dev_1.Id, dev_1.*, dev_2.*
	FROM dev_1
	JOIN dev_2 
    ON dev_1.Id = dev_2.Id and DATEDIFF(second, dev_1, dev_2) BETWEEN 0 AND 30
	),
    merging_df_1
AS (
	SELECT merging_df.*,dev_3.*
	FROM merging_df
	JOIN dev_3
    ON merging_df.Id = dev_3.Id and DATEDIFF(second, merging_df, dev_3) BETWEEN 0 AND 30
	)
SELECT *
INTO rawdev1
FROM dev_1

SELECT *
INTO rawdev2
FROM dev_2

SELECT *
INTO rawdev3
FROM dev_3


select *
into outblob 
from merging_df_1


select *
into outev
from merging_df_1

select *
into outcosmosdb
from merging_df_1
