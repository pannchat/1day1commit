import sys
import simplejson as json
test_dict = {'1':95, '4':77, '3':65,'5':100}

print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))

print(sys.stdin.encoding)
print(sys.stdout.encoding)