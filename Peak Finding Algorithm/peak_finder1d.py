def one_D_peak_finder(arr):
    if len(arr) >= 3:
        n = len(arr)//2
        if arr[n-1]<arr[n]>arr[n+1]:
            return arr[n]
        else:
            return one_D_peak_finder(arr[n+1:]) or one_D_peak_finder(arr[:n])

if __name__ == "__main__":
    arr = [10, 20, 25, 2, 23, 90, 67, 24, 65, 74, 87, 12, 98, 23, 67, 83, 86]
    print(one_D_peak_finder(arr))

