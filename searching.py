import os
import json
import time

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers","ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        seq = json.load(json_file)
    return seq[field]

def linear_search(seq, number):
    slovnik = {}
    positions= []
    for idx, n in enumerate(seq):
        if n == number:
            positions.append(idx)
    slovnik["positions"] = positions
    count = len(positions)
    slovnik["count"] = count
    return slovnik

def pattern_search(sekvence_dna, vzor):
    idx = 0
    idxs_of_vzor= set()
    n = len(vzor)
    while idx <= len(sekvence_dna) -n:
        if sekvence_dna[idx:idx+n] == vzor:
            idxs_of_vzor.add((idx,idx+n-1))
        idx +=1
    return idxs_of_vzor
#da se to zkratit tim ze kdyz se neco nerovna dame breakk

def binary_search(sequence_n, num):
    offset = 0
    while len(sequence_n)> 0:
        delka = len(sequence_n)
        idx = delka // 2
        if num == sequence_n[idx]:
            return offset + idx
        if num > sequence_n[idx]:
            sequence_n = sequence_n[idx+1:]
            offset+= idx+1
        else:
            sequence_n = sequence_n[:idx]
        if idx == 0:
            return None



def main():
    file_name = "sequential.json"
    #read data

    seq = read_data(file_name, field="unordered_numbers")
    sekvence_dna = read_data(file_name, field="dna_sequence")
    sequence_n = read_data(file_name, field="ordered_numbers")
    idxs_of_vzor = pattern_search(sekvence_dna, vzor="ATA")
    print(idxs_of_vzor)
    print(seq)
    start_time = time.time()
    slovnik = linear_search(seq,number=0)
    print(slovnik)
    total_time = time.time() - start_time
    print(f"delka je {total_time}")
    idx_of_num = binary_search(sequence_n, num=-12)
    print(idx_of_num)

if __name__ == '__main__':
    main()