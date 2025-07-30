import chess
import chess.svg
import argparse
from pathlib import Path
import os # Import os for directory listing

def create_chess_image(fen, output_path, size=800, output_format="svg"):
    """
    Create a chess board image from a FEN string and save it to a specified format.
    
    Args:
        fen (str): FEN string representing the board position
        output_path (str): Base path to save the output image (without extension)
        size (int): Size of the output image in pixels (default: 800)
        output_format (str): Desired output format, 'svg' or 'png' (default: 'svg')
    """
    # Create a board from the FEN string
    board = chess.Board(fen)
    
    # Generate SVG with custom colors (grey and white board) and staunty pieces
    light_square = "#f0f0f0"  # Light grey
    dark_square = "#a0a0a0"    # Dark grey
    
    # Create the SVG with custom colors and staunty piece set
    svg_content = chess.svg.board(
        board=board,
        size=size,
        colors={
            'square light': light_square,
            'square dark': dark_square,
        },
        coordinates=True,
        style='''
            @import url('https://lichess1.org/assets/_QqHRZ/compiled/staunty.css');
            piece {
                background-image: url('https://lichess1.org/assets/_QqHRZ/compiled/staunty/piece-css/staunty.svg');
            }
            .square.light {fill: #f0f0f0;}
            .square.dark {fill: #a0a0a0;}
            .square.light.lastmove {fill: #f7f769;}
            .square.dark.lastmove {fill: #b5b53d;}
        '''
    )
    
    final_output_path = Path(output_path)

    if output_format == "svg":
        final_output_path = final_output_path.with_suffix('.svg')
        with open(final_output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
    else:
        raise ValueError("Unsupported output format. Choose 'svg' or 'png'.")
        
    return str(final_output_path)

def read_fen_from_file(file_path):
    """Read a FEN string from a file."""
    with open(file_path, 'r') as f:
        return f.read().strip()

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Generate chess board images (SVG or PNG) from FEN strings.')
    
    parser.add_argument('input_path', help='Input FEN file or directory containing FEN files.')
    parser.add_argument('output_dir_or_file', nargs='?', default=None,
                        help='Output directory for multiple files or output file for single FEN. '
                             'If not provided, defaults to "output_images" for directory input '
                             'or "chess_board.png" (or .svg) for single file input.')
    parser.add_argument('--size', type=int, default=800, 
                        help='Image size in pixels (default: 800)')
    parser.add_argument('--format', choices=['svg'], default='svg',
                        help='Output image format (default: png)')
    parser.add_argument('--all', action='store_true',
                        help='Process all .fen files in the input_path directory.')
    
    args = parser.parse_args()
    
    input_path = Path(args.input_path)

    if args.all:
        if not input_path.is_dir():
            print(f"Error: When using --all, input_path must be a directory. '{input_path}' is not a directory.")
            return 1
        
        output_base_dir = Path(args.output_dir_or_file) if args.output_dir_or_file else Path("output_images")
        output_base_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Processing all FEN files in '{input_path}' and saving to '{output_base_dir}' as {args.format.upper()}...")
        
        processed_count = 0
        for fen_file in input_path.glob('*.fen'):
            try:
                fen = read_fen_from_file(fen_file)
                output_filename = fen_file.stem # Get filename without extension
                output_file_path = output_base_dir / output_filename
                
                created_path = create_chess_image(fen, str(output_file_path), args.size, args.format)
                print(f"Generated: {created_path}")
                processed_count += 1
            except Exception as e:
                print(f"Error processing '{fen_file}': {e}")
        
        if processed_count > 0:
            print(f"\nSuccessfully created {processed_count} chess board {args.format.upper()} images in '{output_base_dir}'.")
        else:
            print(f"\nNo .fen files found in '{input_path}' or no images were generated.")

    else: # Process a single FEN file
        if not input_path.is_file():
            print(f"Error: When not using --all, input_path must be a file. '{input_path}' is not a file.")
            return 1
            
        try:
            fen = read_fen_from_file(input_path)
            
            output_file_path = Path(args.output_dir_or_file) if args.output_dir_or_file else (Path("chess_board") if args.format == "png" else Path("chess_board"))
            
            created_path = create_chess_image(fen, str(output_file_path), args.size, args.format)
            print(f"Successfully created chess board {args.format.upper()} at: {created_path}")
            print(f"Open this file to view the chess board.")
        except Exception as e:
            print(f"Error: {e}")
            return 1
        
    return 0

if __name__ == "__main__":
    exit(main())