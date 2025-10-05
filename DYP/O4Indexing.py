num = "343-393-233-3232-9580"
len = len(num)
print(f"index at 7: {num[7]}")
print(f"from 0 to 6: {num[:7]}")
print(f"from 1 to all: {num[1:]}")
print(f"from 0 to all: {num[::]}")
print(f"All but only odd index: {num[1::2]}")

#start from front to back using -ve index
print(f"using -ve index: {num[-len::]}")

#start from back to front (all below will do the same)
print(f"from back: {num[-1:-len-1:-1]}")
print(f"from back: {num[-1::-1]}")
print(f"from back: {num[::-1]}")
