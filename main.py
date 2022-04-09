import sys
import join

#
join = join.Join(sys.argv[1], sys.argv[2], sys.argv[3])
print(join.inner_join())
