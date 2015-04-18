# coding: utf-8

# ある文字列が前後どちらから読んでも同じ回文かどうかを判断するプログラム

def isPalindrome(s):
    u"""sを文字列と仮定
    sが回文ならTrueを返し、それ以外ならFalseを返す
    ただし句読点、空白、大文字・小文字は無視する"""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstubwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

def testIsPalindrome():
    print 'Try dogGod'
    print isPalindrome('dogGod')
    print 'Try doGood'
    print isPalindrome('doGood')
    
def main():
    testIsPalindrome()

if __name__ == '__main__':
    main()
