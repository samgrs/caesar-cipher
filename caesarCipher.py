minValue = 32
maxValue = 126


def cod_cesar(text, key):
    encrypt = ""
    for letter in text:
        index = ord(letter)
        encrypt_letter = (index + key - minValue) % 95 + 32
        encrypt += chr(encrypt_letter)

    return encrypt


def decod_cesar(text, key):
    decrypt = ""
    for letter in text:
        index = ord(letter)
        decrypt_letter = (index - key - 32 + 95) % 95 + 32
        decrypt += chr(decrypt_letter)

    return decrypt


def reader(filename, key):
    file = filename + ".txt"
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            crypt_line = cod_cesar(line, key)
            print("Mensagem inserida: " + line.rstrip())
            print("Mensagem criptografada: " + crypt_line.rstrip())
    file.close()


# reader("text", 5)


def writer_file(filename, key):
    output = open(filename + '.txt', 'w+')
    file = 'text.txt'
    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            crypt_line = cod_cesar(line, key)
            output.write(crypt_line + "\n")
    output.close()


def writer_decrypt(filename, key):
    output = open(filename + '.txt', 'w+')
    file = 'text_crypt.txt'
    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            crypt_line = decod_cesar(line, key)
            output.write(crypt_line + "\n")
    output.close()


def reader_decrypt(filename, key):
    file = filename + ".txt"
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            crypt_line = decod_cesar(line, key)
            print("Mensagem inserida: " + line.rstrip())
            print("Mensagem criptografada: " + crypt_line.rstrip())
    file.close()


#  writer_file("output2.txt", 5)

method = str(input("Deseja [E] encriptar ou [D] decriptar? \n")).upper().strip()
question_txt = str(input("Deseja criar um arquivo .txt [S/N]?\n")).upper().strip()

if method == "E":
    k = int(input("Insira a chave: \n"))
    reader("text", k)
    if question_txt == "S":
        writer_file("encrypt", k)
else:
    k = int(input("Insira a chave: \n"))
    reader_decrypt("text_crypt", k)  # chave do arquivo text_crypt.txt é 3
    if question_txt == "S":
        writer_decrypt("decrypt", k)
