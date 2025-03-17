def merge_sort(A): 
    
   
    def merge(A, l, r):
      
        n = r-l+1
        B = [A[l+i] for i in range(n)]

        mid = (l+r)//2
        a = l
        b = mid+1


       

        for i in range(l, r+1):

            if a <= mid and b <= r:

                if B[a-l] < B[b-l]:
                    A[i] = B[a-l]
                    a+=1

                else:
                    A[i] = B[b-l]
                    b+=1

            else:

                if a > mid:
                    A[i] = B[b-l]
                    b+=1
            
                if b > r:
                    A[i] = B[a-l]
                    a+=1
            
        return A
    #end def



    def divide(A, l, r):
        
        if l == r:
            return [A[l]]

        mid = (l+r)//2

        divide(A,l,mid)
        divide(A,mid+1,r)

        return merge( A, l, r )
    #end def 

    divide( A, 0, len(A)-1)

    return A
#end def
    

print(merge_sort( [4,3,2,1] ) )



