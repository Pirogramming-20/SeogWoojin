def palindrome(word):
    start=0
    end=len(word)-1
    while(start<=end):
        if word[start] != word[end]:
            raise NotPalindromeError
        start+=1
        end-=1
    print(word)
class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__("회문이 아닙니다.")


try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)