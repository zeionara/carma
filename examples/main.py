from karma import push, add, sync

try:
    print(
        push(local_path = 'assets/15.json')
    )
except ValueError as e:
    print(e)

try:
    print(
        add(local_path = 'assets/15.json', remote_dir = 'music/books')
    )
except ValueError as e:
    print(
        e
    )

for result in sync(local_dir = 'assets/foo', remote_dir = 'music/books'):
    print(result)
