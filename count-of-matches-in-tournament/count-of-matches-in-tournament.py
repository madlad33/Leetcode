class Solution:
    def numberOfMatches(self, n: int) -> int:
        self.match_ = 0 
        def count(n):
            if n == 1:
                return 

            if n % 2 == 0:
                self.match_ += n/2
                team_adv = n / 2
                count(team_adv)
            else:

                self.match_  += (n - 1) / 2 + 1
                team_adv = (n - 1) / 2
                count(team_adv)
            

        count(n)
        return int(self.match_)
