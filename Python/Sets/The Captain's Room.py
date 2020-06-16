def captains_room(myset, arr, k):
    return (((sum(myset) * k) - (sum(arr))) // (k - 1))

if __name__ == '__main__':
    K           =   int(input())                        # group size
    rooms_arr   =   list(map(int, input().split()))     # rooms list
    rooms_set   =   set(rooms_arr)                      # rooms set
    output      =   captains_room(rooms_set, rooms_arr, K)
    print(output)