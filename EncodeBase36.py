def encode(integer):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    result = ''
    
    while integer > 0:   	
        integer, remainder = divmod(integer, 36)
        result = chars[remainder]+result

    return sign + result


def decode(integer):
	chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	sign = ''
	result = ''
	digits = []
	count = 0

	while count < len(integer):
		if count == 0 and integer[count] == '-':
			sign = '-'
			count += 1
		else:
			digits.append(chars.find(integer[count]))
			count += 1

	count = 0
	num = 0

	while count < len(digits):
		num = num * 36		
		num += digits[count]
		print(num)
		count += 1

		result = num

	return sign + result










print(encode(2018))
