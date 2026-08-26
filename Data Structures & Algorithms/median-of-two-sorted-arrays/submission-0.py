class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        x=[]
        while (i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                x.append(nums1[i])
                i+=1
                continue
            else:
                x.append(nums2[j])
                j+=1
                continue
        while (i<len(nums1)):
            x.append(nums1[i])
            i+=1
        while (j<len(nums2)):
            x.append(nums2[j])
            j+=1
        if len(x)%2==0:
            return float((x[int(len(x)/2)]+x[int((len(x)/2)-1)])/2)
        else:
            return float(x[int(len(x)/2)])