import sys
import join

try:
    join.join(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
except FileNotFoundError:
    print('ERROR! Wrong filepath was given.', file=sys.stderr)
except IndexError:
    try:
        join.join(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print('ERROR! Not enough parameters.', file=sys.stderr)
    except FileNotFoundError:
        print('ERROR! Wrong filepath was given.', file=sys.stderr)
