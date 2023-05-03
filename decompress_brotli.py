import brotli

# Open the Brotli-encoded file in binary mode
with open(r'C:\Users\demo\Desktop\oceanActivistPortal\static\game\Build\game.framework.js.br', 'rb') as file_in:
    # Read the Brotli-encoded data from the file
    compressed_data = file_in.read()

# Decompress the Brotli-encoded data using the brotli.decompress() function
decompressed_data = brotli.decompress(compressed_data)

# Open a new file for writing the decompressed data
with open(r'C:\Users\demo\Desktop\oceanActivistPortal\static\game\Build\game.framework.js', 'wb') as file_out:
    # Write the decompressed data to the new file
    file_out.write(decompressed_data)
