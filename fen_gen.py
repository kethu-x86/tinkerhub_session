import os

def create_fen_file(filename, fen_string):
    """
    Creates a text file with the given FEN string as its content.

    Args:
        filename (str): The name of the file to create (e.g., "position1.fen").
        fen_string (str): The FEN string to write into the file.
    """
    try:
        with open(filename, 'w') as f:
            f.write(fen_string.strip()) # .strip() to remove any leading/trailing whitespace
        print(f"Successfully created '{filename}'")
    except IOError as e:
        print(f"Error creating file '{filename}': {e}")

if __name__ == "__main__":
    # Define all 20 FEN strings you want to save
    # Each FEN represents a simple bishop fork scenario
    fen_positions = {
        "1_king_rook_fork.fen": "8/6r1/8/8/8/2B5/8/K7 w - - 0 1",
        "2_king_knight_fork.fen": "3k4/1n6/8/8/8/5B2/8/7K w - - 0 1",
        "3_two_rooks_fork.fen": "8/5r2/r7/8/2B5/8/8/6K1 w - - 0 1",
        "4_rook_knight_fork.fen": "8/5r2/1n6/8/3B4/8/8/K7 w - - 0 1",
        "5_two_knights_fork.fen": "8/6n1/2n5/8/8/4B3/8/7K w - - 0 1",
        "6_queen_rook_fork.fen": "2r3q1/8/8/8/4B3/8/1K6/8 w - - 0 1", # Bishop e4 forks Q g6, R c2
        "7_queen_knight_fork.fen": "8/8/5q2/8/3B4/1n6/8/K7 w - - 0 1", # Bishop d4 forks Q f6, N b2
        "8_king_pawn_attack.fen": "8/6p1/8/k7/8/4B3/8/2K5 w - - 0 1", # Bishop e3 attacks K a5, P g5 (less a "fork", more an attack)
        "9_two_pawns_fork.fen": "8/5p2/1p6/8/3B4/8/8/K7 w - - 0 1", # Bishop d4 forks P b5, P f8
        "10_king_queen_discovered.fen": "8/6q1/8/k7/8/8/4B3/4K3 w - - 0 1", # White K moves to d1, Bishop on e2 forks K a5, Q g4
        "11_tight_king_rook_fork.fen": "8/8/1r6/8/8/5B2/8/3k3K w - - 0 1", # Bishop f3 forks K d1, R b3
        "12_open_two_rooks_fork.fen": "3r4/r7/8/8/3B4/8/8/K7 w - - 0 1", # Bishop d4 forks R d8, R a7
        "13_knight_pawn_fork.fen": "6p1/3n4/8/8/8/4B3/8/2K5 w - - 0 1", # Bishop e3 forks N d2, P g6
        "14_king_rook_move_fork.fen": "r7/8/2p5/8/3B4/8/8/2k3K1 w - - 0 1", # (FEN implies position *after* a move to d4). Here, Bishop d4 forks K c8, R a1
        "15_king_knight_pawn_block.fen": "4k3/6n1/8/8/8/2B5/1P6/K7 w - - 0 1", # Bishop c3 forks K e7, N g5 (pawn b2 exists)
        "16_rook_bishop_fork.fen": "6b1/r7/8/8/3B4/8/8/7K w - - 0 1", # Bishop d4 forks R a7, B g7
        "17_knight_bishop_fork.fen": "6b1/8/2n5/8/8/4B3/8/1K6 w - - 0 1", # Bishop e3 forks N c5, B g5
        "18_king_queen_different_colors.fen": "8/6q1/8/4k3/8/2B5/8/K7 w - - 0 1", # Bishop c3 forks K e5, Q g7
        "19_rook_pawn_open_diagonal.fen": "4p3/r7/8/2B5/8/8/8/6K1 w - - 0 1", # Bishop c5 forks R a7, P e7
        "20_two_bishops_fork.fen": "7b/1b6/8/8/8/5B2/8/3K4 w - - 0 1", # Bishop f3 forks B b7, B h5
    }

    # Create a directory to store the FEN files, if it doesn't exist
    output_directory = "fen_files_20_positions"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    # Generate the FEN files
    for filename, fen_string in fen_positions.items():
        file_path = os.path.join(output_directory, filename)
        create_fen_file(file_path, fen_string)

    print(f"\nAll 20 FEN files have been created in the '{output_directory}' directory.")