from numpy import ravel_multi_index
from compare_Imag import runAllImageSimilaryFun
img1='.\\case_demo\\screenshot\\img1.png'
img2='.\\case_demo\\screenshot\\2021_07_03_183031.png'

x=runAllImageSimilaryFun(img1,img2)
print(x)