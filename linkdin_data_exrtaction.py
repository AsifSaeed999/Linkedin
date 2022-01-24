
from linkedin_api import Linkedin
import pandas as pd
api = Linkedin("asifokz365@gmail.com", "Pakistan@1122$")
list1 = ['jamal-ahmad-438187158','atif-alam-78193b210', 'ammara-arshad-141ba7136', 'nehaejaz']
df = pd.DataFrame(columns = ['user_id','firstName','lastName','location','Skills'])
count = 0

for i in list1:
  profile = api.get_profile(i)
    uri = profile["profile_id"]
    skills = profile["skills"]
    k = ''
    for i in range(len(skills)):
        a = list(skills[i].values())
        k = a[0] +','+ k
    data = {
        'user_id' : uri[-7:],
        'firstName':profile["firstName"],
        'lastName':profile["lastName"],
        'location':profile["geoLocationName"],
        'Skills':k,
            }
    df1 = pd.DataFrame(data,index = [0])
    df = df.append(df1)
    count = count + 1

df.to_csv(r"C:\Users\Nexgen\Desktop\Data Extraction\linkdi.csv", index = False)
print(df)
