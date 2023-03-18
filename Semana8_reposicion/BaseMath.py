class BaseMath:
    def __init__(self) -> None:
        self.codUser = None
        self.nameUser = None
        
    def bubbleSort(self,arr) -> list:
        n = len(arr)
        
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]
                    
        return arr