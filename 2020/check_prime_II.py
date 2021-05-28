
def main():




def find_all_primes(n:int):
        primes = []
	for i range(2, n+1):
		j = 2
	
            while j**2 <= i:
	        if i % j == 0:
		    break
		j += 1
	    else:
	        primes.append(i)
	
        return primes
    
