DROP TABLE IF EXISTS ads;

CREATE EXTERNAL TABLE ads ( 
    campaign_id STRING, 
    display_date STRING,
    display_time STRING, 
    keyword STRING,
    display_site STRING, 
    placement STRING,
    was_clicked TINYINT,
    cpc INT
  ) 
  PARTITIONED BY (network TINYINT)
  ROW FORMAT 
  DELIMITED FIELDS TERMINATED BY '\t'
  LOCATION '/dualcore/ads';