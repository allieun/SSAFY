'''
이용권 종류는 4개 : 1일권 / 1개월권 / 3개월권 / 1년 권
각 이용권 요금과 각 달 이용 계획이 주어짐
가장 적은 비용으로 수영장을 이용할 수 있는 방법 찾기
'''

def price(month, current_sum):
    global min_price

    if current_sum >= min_price:
        return
    if month >= 12:
        if current_sum < min_price:
            min_price = current_sum
        return
    
    price(month + 1, current_sum + (month_list[month] * price_list[0]))
    price(month + 1, current_sum + price_list[1])
    price(month + 3, current_sum + price_list[2])




t = int(input())

for tc in range(1, t+1):
    price_list = list(map(int, input().split()))
    month_list = list(map(int, input().split()))

    min_price = price_list[3]

    price(0, 0)

    print(f'#{tc} {min_price}')