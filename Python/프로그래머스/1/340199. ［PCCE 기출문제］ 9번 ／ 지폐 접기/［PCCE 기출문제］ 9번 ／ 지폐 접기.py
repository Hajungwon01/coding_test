def solution(wallet, bill):
    answer = 0
    bill_min = min(bill)
    bill_max = max(bill)
    wallet_min = min(wallet)
    wallet_max = max(wallet)
    while bill_min > wallet_min or bill_max > wallet_max:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        bill_min = min(bill)
        bill_max = max(bill)
        wallet_min = min(wallet)
        wallet_max = max(wallet)
        answer += 1
    return answer