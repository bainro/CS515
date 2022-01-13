'''
There is always enough pegs to move all non-bottom START blocks
to non-END (ie TMP) pegs without any stacking. This would leave 
just the bottom/largest block on START, which can be directly 
moved to END. Then just grab each TMP peg's single block and 
place it onto END as well (minding the order!).
'''

def move(src, dest, tmps, top_call=False):
    if len(tmps) > 0:
        move(src, tmps[0], tmps[1:])
        move_top_block(src, dest) # moves top block of src to dest
        if top_call:
            for p in tmps:
                move_top_block(p, dest) # move each tmp peg block to END

def move_top_block(s, d):
    pass

# num_p = 4
# # remove START & END from free pegs
# tmps = range(num_p)[1:-1]
# move(0, num_p-1, tmps, top_call=True)