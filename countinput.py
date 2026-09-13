'''
Submitter details: Gayatri Gundawar
'''

def countchars(st):
    cnt = 0 
    for i in st:
        if i not in (' ',',','.','!'):
            cnt+=1
    return cnt

s = input("Enter a string: ")
print(countchars(s))

if __name__ == "__main__":
    assert countchars("Hello world") == 10
    assert countchars("Hello, world!") == 10
    assert countchars("Mr. Jones.") == 7
    assert countchars("1234") == 4
    assert countchars("Hi?") == 3
    assert countchars("!!!...,,,") == 0
    print("All tests passed!")
