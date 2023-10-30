# soal nomor 1 
# penjumlahan 
import numpy as np
# membuat dua macam matrik 3x3
matrik1 = np.array([[1,3,4], [5,3,7], [9,6,2]])
matrik2 = np.array([[8,7,9], [3,4,6], [1,5,10]])
#penjumlahan 
penjumlahan_matrik = np.add(matrik1, matrik2)
print(penjumlahan_matrik)
    
# pengurangan 
pengurangan_matrik = np.subtract(matrik1, matrik2)
print(pengurangan_matrik)

# soal nomor 2
# perkalian 
import numpy as np 
# membuat dua matriks 2x2
mat1 = np.array([[1,6], [7,8]])
mat2 = np.array([[6,7], [9,7]])
#perkalian matrik 
perkalian_matrik = np.dot(mat1,mat2)
print(perkalian_matrik)

# soal nomor 3
#transpo matrik 
import numpy as np
# membuat matriks 3x2 
matriks = np.array([[1,6], [1,3], [3,2]])
# transpose matrik 
transpose_matrik = np.transpose(matriks)
print(transpose_matrik)

# soal nomor 4
# inverese 
import numpy as np
matrikx = ([[2,3,4], [5,6,8], [9,7,5]])
# invers matriks 
inverse_matrik = np.linalg.inv(matrikx)
print(inverse_matrik)

# soal 5 
# identitas 
import numpy as np
# membuat matrik identitas 4x4 
identitas_matrik = np.eye(4)
print(identitas_matrik)

# soal nomo 6 
# reshape matrik 
import numpy as np 
# membuat matrik 4x4
mat3 = np.array([[2,3,4,5], 
                 [6,7,8,9], 
                 [10,11,12,13], 
                 [14,15,16,17]])

#reshape matrik menjadi 2x8 
reshape_matrik = mat3.reshape(2,8)
print(reshape_matrik)