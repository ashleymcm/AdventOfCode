set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23








a = 1
b = 109900
c = 126900
    set f 1
    set d 2
        set e 2
            set g d
            mul g e
            sub g b
            
            jnz g 2
            set f 0
            
            sub e -1
            set g e
            sub g b
            jnz g -8
        sub d -1
        set g d
        sub g b
        jnz g -13
    jnz f 2
    sub h -1
    
    set g b
    sub g c
    
    jnz g 2
    jnz 1 3 ////// END CONDITION
    sub b -17
    jnz 1 -23
    












a = 1
b = 109900
c = 126900
    f = 1
    d = 2
        while (g != 0) {
        e = 2
            while (e != b) {
                if (d * e == b) {
                    f = 0 
                }
                
                e++
            }
        g = 0
        d = d + 1
        g = d - b
        }
    
    if (f == 0) {
        h = h + 1
    }
    
    g = b - c
    
    if (b == c) {
        jnz 1 3 ////// END CONDITION
    }

    b = b + 17
    jnz 1 -23
    
    





import math

b = 109900
c = 126900

def is_prime(n): // taken from StackOverflow thxman
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 
        
        
h = 0
for x in range(b, c + 1, 17):
    if not is_prime(x):
        h += 1
        
        
print h