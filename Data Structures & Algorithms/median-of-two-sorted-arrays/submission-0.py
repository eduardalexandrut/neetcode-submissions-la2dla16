class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A,B = B, A

        half = (len(A) + len(B)) // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2#Mid of A
            j = half - i - 2 #Size of B left partition (-2 because we have to do -1 from A and -1 from B)

            #We have to check if i and j are in bounds
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #Check if the partition is correct.
            """
            If Aleft is bigger than Bright, then the left partition is wrong, and we have to check
            the new mid in the left section of mid of A(i). Otherwise, we have to check the new mid of A
            (i) to the its right.
            """
            if Aleft <= Bright and Bleft <= Aright:
                #If the sum of the lengths is even, the median will be smallest of Aright,Bright
                if (len(nums1) + len(nums2)) % 2:
                    return min(Aright,Bright)
                #If the sum of the length is odd, the median will be the average of...
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i +1
