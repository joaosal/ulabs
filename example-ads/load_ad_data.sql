ALTER TABLE ads ADD PARTITION (network=1);
ALTER TABLE ads ADD PARTITION (network=2);

LOAD DATA INPATH '/dualcore/ad_data1' 
  INTO TABLE ads
  PARTITION(network=1);
  
LOAD DATA INPATH '/dualcore/ad_data2' 
  INTO TABLE ads
  PARTITION(network=2);