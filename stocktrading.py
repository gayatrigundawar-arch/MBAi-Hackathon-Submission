'''
Submitter details: Gayatri Gundawar 
'''

def maxProfit(prices):
    mp = 0
    ln = prices[0]
    for i in prices[1:]:
        if i-ln>mp:
            mp = i-ln
        if i<ln:
            ln = i
    return mp

if __name__ == "__main__":
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0
    assert maxProfit([1,2,3,4,5]) == 4
    assert maxProfit([3,2,6,5,0,3]) == 4
    assert maxProfit([1]) == 0
    print("All tests passed!")
    
