from gcd import gcd
#testing gcd function in different functions
def test_gcd1():
	assert gcd(48, 64) == 16
	assert gcd(44, 19) == 1
def test_gcd2():
	assert gcd(40000000000000000000000000,40000000000000000000000000) == 40000000000000000000000000
if __name__=='__main__':
	test_gcd1()
	test_gcd2()