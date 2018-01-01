
userlist=[{ 'admin' : True, 'active' : True, 'name' : 'Kevin' },
        { 'admin' : False, 'active' : False, 'name' : 'Alex' },
        { 'admin' : False, 'active' : True, 'name' : 'Katy' },
        { 'admin' : False, 'active' : False, 'name' : 'Ery' }]


for user in userlist:
    print(userlist.index(user)+1, end=' ')
    if user['admin'] and user['active']:
        print("ACTIVE - (ADMIN) %s" % user['name'])
    elif user['admin']:
        print("(ADMIN) %s" % user['name'])
    elif user['active']:
        print("ACTIVE %s" % user['name'])
    else:
        print(user['name'])

