from modules.controller.controller import Controller


##  Run this script to start the command line interaction
#
#   Example interaction:
#       collect -a 5 -n example_matrices -p modules/shared/data/
#       label -s /home/ugsqo -p /home/ugsqo/home/ugsqo/modules/shared/data/unlabeled_matrices.hdf5 -n okok
#       quit

Controller().start_interaction()
