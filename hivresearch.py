import sys


class GenericSequence:
    def __init__(self, sequence_dict):
        self._header = sequence_dict["header"]
        self._sequence = sequence_dict["sequence"]

    def get_header(self):
        return self._header

    def get_sequence(self):
        return self._sequence


class NucleotideSequence(GenericSequence):
    def __init__(self, sequence_dict, split_len=10000):
        super(NucleotideSequence, self).__init__(sequence_dict)
        self._split_sequence_list = self.sequence_splitter(self._sequence,
                                                           split_len)
        self._gc_percentage_list = self.gc_percentage(self.
                                                      _split_sequence_list)

    @staticmethod
    def sequence_splitter(sequence, split_len):
        _split_sequence_list = []
        for index in range(0, len(sequence), split_len):
            _split_sequence_list.append(sequence[index: index + split_len])
        return _split_sequence_list

    @staticmethod
    def gc_percentage(sequence_list):
        gc_percentage_list = []
        for element in sequence_list:
            element = element.upper()
            tmp_nuc_dict = {
                "g": element.count("G"),
                "c": element.count("C"),
                "n": element.count("N")
            }
            # Remove N from total count as data is invalid for calc.
            temp_valid_seq_len = len(element) - tmp_nuc_dict["n"]
            gc_tot = tmp_nuc_dict["c"] + tmp_nuc_dict["g"]
            gc_percentage = float(gc_tot / temp_valid_seq_len * 100)
            gc_percentage_list.append(gc_percentage)
        return gc_percentage_list

    def get_gc(self):
        return self._gc_percentage_list


def file_obtaining():
    file_list = sys.argv[1:]
    for element in file_list:
        with open(element) as current_opened_file:
            sequence_dictionary(current_opened_file)


def sequence_dictionary(file):
    _sequence_dict = {}
    current_value = ""
    header_checkpoint = False
    while True:
        line = file.readline()
        if not line:
            break
        elif not line.startswith(">"):
            # Check to see if data is already there.
            if _sequence_dict["sequence"]:
                current_value = _sequence_dict["sequence"]
                current_value += line
                _sequence_dict["sequence"] = current_value
            else:
                _sequence_dict["sequence"] = line
        elif line.startswith(">"):
            if _sequence_dict["header"]:

            else:
                _sequence_dict["header"] = line
            header_checkpoint = True




def main():
    file_obtaining()


main()
