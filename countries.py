import json
import pygal.maps.world
from country_codes import get_country_code

# 上述的导入方法是网上的 但是没有成功 书本上的方法已经过期了
for country_code in sorted(get_country_code.keys()):
    print(country_code, get_country_code[country_code])