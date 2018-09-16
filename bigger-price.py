from operator import itemgetter

def bigger_price(limit: int, data: list) -> list:
    data = sorted(data, key=itemgetter('price'), reverse=True)[:limit]
    return data
