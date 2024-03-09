list_text=[]
len_texts=[]
for i in range(3):
    with open(f'files/{i+1}.txt', encoding='utf-8' ) as f:
        name = f'{i+1}.txt'
        text=f.readlines()
        len_text=len(text)
        list_text.append([len_text, name, text])
        len_texts.append(len_text)
len_texts.sort()
with open('files/text.txt', 'w', encoding='utf-8') as f:
    for kol_strok in len_texts:
        for texts in list_text:
            if kol_strok == texts[0]:
                f.write(texts[1])
                f.write('\n')
                f.write(str(texts[0]))
                f.write('\n')
                for stroka in texts[2]:
                    f.write(stroka.strip('\n'))
                    f.write('\n')