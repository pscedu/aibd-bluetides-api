# command: mpirun -np 4 python parallel.py
import sys
import os
import mpi4py.MPI as MPI
import numpy as np
import bigfile

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
    # if len(sys.argv) != 2:
    #         sys.stderr.write("Usage: python *.py directoty_with_files\n")
    #         sys.exit(1)
    # path = sys.argv[1]
    path = "/pylon5/as5pi3p/bluetides3/PIG_251/FOFGroups/OffsetByType"
    # pig = utils.get_pig_data(251)
    # data = pig.open('FOFGroups/' + "OffsetByType")[:]
    if comm_rank == 0:
        # file_list = os.listdir(path)
        pig = bigfile.File("/pylon5/as5pi3p/bluetides3/PIG_251/")
        # sys.stderr.write("%d files\n" % len(file_list))
    # file_list = comm.bcast(file_list if comm_rank == 0 else None, root = 0)
    pig = comm.bcast(pig if comm_rank == 0 else None, root = 0)
    num_files = pig.open('FOFGroups/OffsetByType/').size
    local_files_offset = np.linspace(0, num_files, comm_size +1).astype('int')
    # local_files = file_list[local_files_offset[comm_rank] :local_files_offset[comm_rank + 1]]
    len_local = local_files_offset[comm_rank + 1] - local_files_offset[comm_rank]
    sys.stderr.write("%d/%d processor gets %d/%d data \n" %(comm_rank, comm_size, len_local, num_files))
    cnt = 0
    file1 = open("MyFile2.txt", "w") 
    # for file_name in local_files:
    for i in range(len_local):
        # hd = open(os.path.join(path, file_name))
        # pig = bigfile.File("/pylon5/as5pi3p/bluetides3/PIG_251/")
        # data = pig.open('FOFGroups/OffsetByType/' + file_name)
        data = pig.open('FOFGroups/OffsetByType/')[i+local_files_offset[comm_rank]]
        numpy_array_data = np.array(data)
        # file1.write(np.array_str(numpy_array_data))
        # for line in hd:
        #     output = line.strip() + ' process every line here'
        #     print(output)
        cnt += 1
        # sys.stderr.write("processor %d has processed %d/%d files \n" %(comm_rank, cnt, len_local))
        file1.write("processor %d has processed %d/%d files \n" %(comm_rank, cnt, len_local))
    pig.close()
    file1.close() 
