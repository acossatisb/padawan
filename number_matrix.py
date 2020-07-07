max_a_str = input("Digite o maximo do primeiro numero: ")
max_a_int = int(max_a_str)
max_b_str = input("Digite o maximo do segundo numero: ")
max_b_int = int(max_b_str)
max_c_str = input("Digite o maximo do terceiro numero: ")
max_c_int = int(max_c_str)
max_d_str = input("Digite o maximo do quarto numero: ")
max_d_int = int(max_d_str)
new_file_csv=open("newfile.csv",mode="a",encoding="utf-8")
new_file_txt=open("newfile.txt",mode="a",encoding="utf-8")
new_file_csv.write('valor1'+','+'valor2'+','+'valor3'+','+'valor4'+'\n')
for a in range(max_a_int):
  for b in range(max_b_int):
    for c in range(max_c_int):
      for d in range(max_d_int):
        print (a+1, b+1, c+1, d+1)
        new_file_csv.write(str(a+1)+','+str(b+1)+','+str(c+1)+','+str(d+1)+','+'\n')
        new_file_txt.write(str(a+1)+' '+str(b+1)+' '+str(c+1)+' '+str(d+1)+' '+'\n')
new_file_csv.close()
new_file_txt.close()
