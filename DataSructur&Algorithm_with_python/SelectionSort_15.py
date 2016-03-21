#coding:utf-8
#Attention:max标志需取为seq[0]，我刚开始取了0，这会导致最后一次比较时出问题
def SelectionSort(seq):
    i,j,maxel = 0,0,seq[0]
    while i < len(seq):
        while j < len(seq)-i:
            if seq[j] > maxel:
                maxel = j
            j+=1
        seq[maxel],seq[len(seq)-i-1] = seq[len(seq)-i-1],seq[maxel]
        j,maxel=0,seq[0]
        i+=1

a=[3,4,6,2,1]
SelectionSort(a)
print(a)

