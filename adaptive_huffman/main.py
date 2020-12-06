from Adaptive_huffman import compress,extract
def main():
    filein = 'adaptive_huffman\Lena.raw'
    filecompress = 'compressed'
    fileextract = 'extracted.raw'
    compress(filein, filecompress)
    extract(filecompress, fileextract)
    input("Press ENTER to exit...")
if __name__ == '__main__':
    main()