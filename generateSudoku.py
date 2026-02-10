import matplotlib.pyplot as plt
import random

def create_solved_board():
    """
    Generates a fully solved 9x9 Sudoku board using a randomized
    pattern generator.
    """
    base  = 3
    side  = base * base

    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return board

def create_puzzle(board, difficulty=0.5):
    side = 9
    squares = side * side
    empties = squares * difficulty
    
    puzzle = [row[:] for row in board] # Copy board
    
    for p in random.sample(range(squares), int(empties)):
        puzzle[p // side][p % side] = 0
        
    return puzzle

def draw_sudoku(puzzle, filename="sudoku_puzzle.png"):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    for i in range(10):
        # Thicker lines for the 3x3 boxes
        linewidth = 2.5 if i % 3 == 0 else 0.5
        
        # Horizontal lines
        ax.plot([0, 9], [i, i], color='black', linewidth=linewidth)
        # Vertical lines
        ax.plot([i, i], [0, 9], color='black', linewidth=linewidth)

    # Place the numbers
    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]
            if val != 0:
                ax.text(c + 0.5, 8.5 - r, str(val), 
                        va='center', ha='center', fontsize=16)

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.axis('off') # Hide axes
    
    # Save the figure
    plt.savefig(filename, bbox_inches='tight', dpi=150)
    plt.close()
    print(f"Image saved as {filename}")


solution_board = create_solved_board()

puzzle_board = create_puzzle(solution_board, difficulty=0.6)

print("--- Full Solution (Use this for GTFA) ---")
for row in solution_board:
    print(row)

print("\n--- Puzzle State ---")
for row in puzzle_board:
    print([x if x != 0 else "." for x in row])

draw_sudoku(puzzle_board)
