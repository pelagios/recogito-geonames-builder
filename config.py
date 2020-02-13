# Filename and path for the output file
outfile = 'geonames_all'

# Provide your own list, or use one of the presets below.
# Leave list empty for a full build with all of GeoNames.
countries = [ 'AT' ] # PRESETS['AFRICA']

# Include continents and natural features
include_non_country_features = True

# Preset country lists (for use with 'countries' property)
PRESETS = {
  'AFRICA'       : ['AO','BF','BI','BJ','BW','CD','CF','CG','CI','CM','CV','DJ','DZ','EG','EH','ER','ET','GA','GH','GM','GN','GQ','GW','KE','KM','LR','LS','LY','MA','MG','ML','MR','MU','MW','MZ','NA','NE','NG','RE','RW','SC','SD','SH','SL','SN','SO','SS','ST','SZ','TD','TG','TN','TZ','UG','YT','ZA','ZM','ZW'],
  'ANTARCTICA'   : ['AQ','BV','GS','HM','TF'],
  'ASIA'         : ['AE','AF','AM','AZ','BD','BH','BN','BT','CC','CN','GE','HK','ID','IL','IN','IO','IQ','IR','JO','JP','KG','KH','KP','KR','KW','KZ','LA','LB','LK','MM','MN','MO','MV','MY','NP','OM','PH','PK','PS','QA','SA','SG','SY','TH','TJ','TM','TR','TW','UZ','VN','YE'],
  'EUROPE'       : ['AD','AL','AT','AX','BA','BE','BG','BY','CH','CS','CY','CZ','DE','DK','EE','ES','FI','FO','FR','GB','GG','GI','GR','HR','HU','IE','IM','IS','IT','JE','LI','LT','LU','LV','MC','MD','ME','MK','MT','NL','NO','PL','PT','RO','RS','RU','SE','SI','SJ','SK','SM','UA','VA','XK'],
  'NORTH_AMERICA': ['AG','AI','AN','AW','BB','BL','BM','BQ','BS','BZ','CA','CR','CU','CW','DM','DO','GD','GL','GP','GT','HN','HT','JM','KN','KY','LC','MF','MQ','MS','MX','NI','PA','PM','PR','SV','SX','TC','TT','US','VC','VG','VI'],
  'OCEANIA'      : ['AS','AU','CK','CX','FJ','FM','GU','KI','MH','MP','NC','NF','NR','NU','NZ','PF','PG','PN','PW','SB','TK','TL','TO','TV','UM','VU','WF','WS'],
  'SOUTH_AMERICA': ['AR','BO','BR','CL','CO','EC','FK','GF','GY','PE','PY','SR','UY','VE']
}


