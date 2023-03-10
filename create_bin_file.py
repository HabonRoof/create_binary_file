output_file = open('output.bin','wb')
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
data_in_binary = bytearray(data)
output_file.write(data_in_binary)

output_file.close()
