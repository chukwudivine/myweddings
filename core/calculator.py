
def calculator(amount, location, guests, venue):
    if amount == 30000:
        if location == 'popular':
            if guests == 600:
                if venue == 'big_hall':
                    return 'luxury budget'
            elif guests == 400:
                if venue == 'small_hall':
                    return 'standard budget'
                else:
                    return 'luxury budget'
        else:
            return 'standard budget'
    elif amount == 20000:
        if venue == 'medium_hall':
            if guests == 400:
                if location == 'less_popular':
                    return 'standard budget'
            elif guests == 600:
                return 'standard budget'
            else:
                return 'standard budget'
        elif venue == 'big_hall':
            if guests == 400:
                if location == 'popular':
                    return 'luxury budget'
                else:
                    return 'standard budget'
            elif guests == 600:
                if location == 'less_popular':
                    return 'standard budget'
        else:
            return 'economic budget'

    elif amount == 10000:
        return 'economic budget'
    else:
        return 'economic budget'
    
print(calculator(30000,'popular',600,'big_hall'))