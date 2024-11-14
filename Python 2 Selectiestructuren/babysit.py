# https://dodona.be/nl/courses/4195/series/46782/activities/1797346540

A = int(input())
B = int(input())
C = int(input())
D = int(input())

begintijd = A+ (B/60)
eindtijd = C+(D/60)

def rekenmachine(begintijd,eindtijd):
        geld = 0
        if begintijd<18 or eindtijd<begintijd:
            return  "ongeldige invoer"
        else: 
   
         if begintijd < 21.5:
            geld += (min(eindtijd, 21.5) - begintijd) * 2
    
   
        if eindtijd > 21.5:
            geld += (eindtijd - max(begintijd, 21.5)) * 4

        return geld                  
print(rekenmachine(begintijd,eindtijd))                     