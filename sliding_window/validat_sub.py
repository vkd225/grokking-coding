arr = [1,2,3,4]
subarr =[4,1]

def validate_sub(subarr, arr):

  subarr_i = 0

  for i in range(len(arr)):
    if arr[i] == subarr[subarr_i]:
      subarr_i += 1

      if subarr_i == len(subarr):
        return True

  return False


print (validate_sub(subarr, arr))

