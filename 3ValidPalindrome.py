class Solution(object):
    def isPalindrome(self, s) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():#Move forward if l<r and characters are not aplhanumeric from left side
                l = l + 1
            while l < r and not s[r].isalnum():#Move forward if l<r and characters are not aplhanumeric from right side
                r = r - 1

            if s[l].upper() != s[r].upper():
                return False
            l = l + 1
            r = r - 1
        return True

s1 = Solution()
print(s1.isPalindrome("A man, a plan, a canal: Panama"))
print((s1.isPalindrome("race a car")))
print(s1.isPalindrome("Dammit I’m mad.Evil is a deed as I live.God, am I reviled? I rise, my bed on a sun, I melt.To be not one man emanating is sad. I piss.Alas, it is so late. Who stops to help?Man, it is hot. I’m in it. I tell.I am not a devil. I level “Mad Dog”.Ah, say burning is, as a deified gulp,In my halo of a mired rum tin.I erase many men. Oh, to be man, a sin.Is evil in a clam? In a trap?No. It is open. On it I was stuck.Rats peed on hope. Elsewhere dips a web.Be still if I fill its ebb.Ew, a spider… eh?We sleep. Oh no!Deep, stark cuts saw it in one position.Part animal, can I live? Sin is a name.Both, one… my names are in it.Murder? I’m a fool.A hymn I plug, deified as a sign in ruby ash.A Goddam level I lived at.On mail let it in. I’m it.Oh, sit in ample hot spots. Oh wet!A loss it is alas (sip). I’d assign it a name.Name not one bottle minus an ode by me:“Sir, I deliver. I’m a dog”Evil is a deed as I live.Dammit I’m mad."))