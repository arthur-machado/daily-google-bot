from pytrends.request import TrendReq

pytrends = TrendReq(hl='pt-BR', tz=180)

data = pytrends.trending_searches(pn='brazil')

data.to_csv('data.csv', index=False)