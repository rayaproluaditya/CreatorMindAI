from pytrends.request import TrendReq

pytrends = TrendReq()

def get_trends():

    pytrends.build_payload(
        kw_list=["AI","Machine Learning","ChatGPT"]
    )

    trends = pytrends.related_queries()

    return trends
