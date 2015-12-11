#k = 13
#a = [1,3,5,10,12,15,32,91,125,132]


def ternarySearch(a,k):

	n = len(a)
	if(a == 1):
		if(a[0] == k): 
			return True
		else: 
			return False

	mid1 = int(n/3)
	mid2 = int(2*n/3)
	last = int(a[n-1])
	first = int(a[0])

	if(k == a[mid1] or k == a[mid2]):
		return True
	elif(k < a[mid1] and first < a[mid1]):
		return ternarySearch(a[0:mid1],k)
	elif(k > a[mid1] and k < a[mid2]):
		return ternarySearch(a[mid1:mid2],k)
	elif(k > a[mid2] and last > a[mid2]):
		return ternarySearch(a[mid2:last],k)
	else: 
		return False


#if ternarySearch(a,k):
#	print("yeah it's here, man")
#else:
#	print("These aren't the droids you're looking for")



