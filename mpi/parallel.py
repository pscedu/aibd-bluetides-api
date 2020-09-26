# command: mpirun -np 4 python parallel.py
import sys
import os
import mpi4py.MPI as MPI
import numpy as np
import bigfile
import pickle
import time

#
#  Global variables for MPI
#
 
# instance for invoking MPI relatedfunctions
comm = MPI.COMM_WORLD
# the node rank in the whole community
comm_rank = comm.Get_rank()
# the size of the whole community, i.e.,the total number of working nodes in the MPI cluster
comm_size = comm.Get_size()
 
if __name__ == '__main__':
    path = "/pylon5/as5pi3p/bluetides3/PIG_251/FOFGroups/OffsetByType"
    if comm_rank == 0:
        pig = bigfile.File("/pylon5/as5pi3p/bluetides3/PIG_251/")
    pig = comm.bcast(pig if comm_rank == 0 else None, root = 0)
    t1 = time.time()
    num_files = pig.open('FOFGroups/OffsetByType/').size
    local_files_offset = np.linspace(0, num_files, comm_size +1).astype('int')
    len_local = local_files_offset[comm_rank + 1] - local_files_offset[comm_rank]
    sys.stderr.write("%d/%d processor gets %d/%d data \n" %(comm_rank, comm_size, len_local, num_files))
    file1 = open("fofgroup.pkl", "ab") 
    data = pig.open('FOFGroups/OffsetByType/')[local_files_offset[comm_rank]:len_local+local_files_offset[comm_rank]]
    t2 = time.time()
    pickle.dump(np.array(data), file1)
    pig.close()
    file1.close()
    print('Time to fetch data is : %.2f s'%(t2-t1))
