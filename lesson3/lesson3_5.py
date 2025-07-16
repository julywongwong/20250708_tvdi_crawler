import json
from pprint import pprint

class Site:
    def __init__(self,
                 sitename,
                 county,
                 aqi,
                 pollutant,
                 status,
                 pm2_5,
                 pm2_5_avg,
                 latitude,
                 longitude,
                 datacreationdate):      
        # 初始化站點物件的屬性
        self.sitename = sitename          # 站點名稱
        self.county = county              # 所在縣市
        self.aqi = aqi                    # 空氣品質指數
        self.pollutant = pollutant        # 主要污染物
        self.status = status              # 狀態
        self.pm2_5 = pm2_5                # PM2.5 濃度
        self.pm2_5_avg = pm2_5_avg        # PM2.5 平均濃度
        self.latitude = latitude          # 緯度
        self.longitude = longitude        # 經度
        self.datacreationdate = datacreationdate  # 資料建立日期

def parse_sites_from_json(json_file):
    # 從JSON檔案解析站點資料
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        # 為每個站點建立Site物件
        site = Site(
            sitename=sitename['sitename'],           # 站點名稱
            county=sitename['county'],               # 所在縣市
            aqi=sitename['aqi'],                     # 空氣品質指數
            pollutant=sitename['pollutant'],         # 主要污染物
            status=sitename['status'],               # 狀態
            pm2_5=sitename['pm2.5'],                 # PM2.5 濃度
            pm2_5_avg=sitename['pm2.5_avg'],         # PM2.5 平均濃度
            latitude=sitename['latitude'],           # 緯度
            longitude=sitename['longitude'],         # 經度
            datacreationdate=sitename['datacreationdate']  # 資料建立日期
        )
        site_list.append(site)
    return site_list 

