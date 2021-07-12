"""
ID: aarush31
LANG: PYTHON3
TASK: beads
"""

with open('beads.in','r') as filein:
    N = int(filein.readline()) # Number of beads
    beads = filein.readline()[:-1] # Necklace

def canCollect(s):
    return not ('r' in s and 'b' in s) # If r and b are not in the same str,
                                       # then you can collect the string.
beads = beads*3 # Wraparound - r actually can be shown as r r r (wraparound 
                # for the front and back)
max = 0 # The final result

for p in range(N, N*2): # Loop through the 2nd bead string (so you can use
    i = p-1             # wraparounds for the front and back)
    left = []
    while i > 0: # Check if you can collect beads (left)
        if canCollect(left + [beads[i]]): # Can colleect
            left.append(beads[i]) # Add to left
            i -= 1 # Loop through again
        else:
            break # Cannot collect more beads - break

    i = p # You will otherwise have a duplicate bead (left is i=p-1)
    right = []
    while i < 3*N - 1:        # Check if you can collect beads (right) - i has
        #print("righti",i-N)  # to be less than 3*N - 1 b/c that is the length
        # ^ for testing       # of the beads + runarounds.

        if canCollect(right + [beads[i]]): # Can collect
            right.append(beads[i]) # Add to right
            i+=1 # Loop through again
        else:
            break # Cannot collect more beads - break

    result = len(left) + len(right) # Final result
    if result >= N: # The result was greater than N means that the whole
        max = N     # necklace is the same (EX: rwr)
        break # Break - we now know we don't need to go through again b/c the
              # whole string is the same! 
    elif result > max: # The result makes sense
        max = result

with open('beads.out','w') as fileout:
    fileout.write(str(max) + '\n') # Final result
