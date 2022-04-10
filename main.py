import sys
import join

print(join.generate_header(sys.argv[1], sys.argv[2], sys.argv[3]) + join.left_right_join(sys.argv[1], sys.argv[2],
                                                                                         sys.argv[3], sys.argv[4]))
