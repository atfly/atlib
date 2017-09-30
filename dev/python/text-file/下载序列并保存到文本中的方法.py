
#!/usr/bin/env python

# -*- coding:utf-8 -*-

__date__    = '2008-10-30'


from Bio import Entrez

def read_id(file_name):
    '''从文件中读取GeneID'''
    id_array = []
    fh = open(file_name, 'r')
    lines = fh.readlines()

    for line in lines:
        id = line.strip()
        id_array.append(id)

    fh.close()

    id_array = ','.join(id_array)
    return id_array

def download_seq (id_array):
    '''根据GeneID下载相应格式的序列'''

    result_handle = Entrez.efetch(db="nucleotide", rettype="genbank",  id=id_array)
    result = result_handle.read()

    return result

def write_to_file(file_out_name, content):
    '''将序列写入文件中 '''
    fh = open(file_out_name, 'w')
    fh.write(content)
    fh.close()

def main():
    '''主控制程序'''
    file_name = 'id_list.txt'
    file_out_name = 'sequences.txt'
    id_array = read_id(file_name)
    result = download_seq(id_array)
    write_to_file(file_out_name, result)

#www.iplaypy.com

if __name__ == '__main__':
    main()

