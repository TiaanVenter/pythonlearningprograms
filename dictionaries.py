customer = {
    'name': 'Jack Johnson', #key: value pairs
    'age': '999',
    'is_verified': True
}

customer['newkey'] = 'newvalue'
print(customer.get('not in dictionary', 'now it is')) #first key alone would return None object, but value gets added after comma. Get method.
print(customer)

#feels a lot like JS