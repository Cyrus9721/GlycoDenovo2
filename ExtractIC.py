# @Author  : Zizhang Chen
# @Contact : zizhang2@brandeis.edu

import re

"""Extract the Ion Classifier score and corresponding peak of interests"""

class ExtractIC:
    def __init__(self, ICfile):
        self.ICfile = ICfile

    def extract_experiment_peak(self):
        peak_list = []
        for line in self.ICfile:
            if 'Peak ' in line:
                peak_id = re.findall(r'%s(\d+)' % 'Peak ', line)
                peak_id = int(peak_id[0])
                peak_list.append(peak_id)
        return peak_list

    def extract_formula(self):
        formula_list = []
        for line in self.ICfile:
            if '** T:' in line:
                formula = line.split('** T: ', 1)[1]
                formula = formula.split(' [Peak')[0]
                formula_list.append(formula)
        return formula_list

    def extract_mass(self):
        mass_list = []
        for line in range(len(self.ICfile)):
            if 'mass ' in self.ICfile[line]:
                mass = re.findall("\d+\.\d+", self.ICfile[line])[0]

                next_line = self.ICfile[line + 1]
                if 'C-2H' in next_line:
                    mass_list.append(float(mass) + 1.0078250321 * 2)
                else:
                    mass_list.append(float(mass))
        return mass_list

    def extract_score(self):
        score_list = []
        for line in self.ICfile:
            if 'IC' in line:
                score = line.split('[')[1].split("]")[0]
                Bion_score = float(score.split(',')[0])
                Cion_score = float(score.split(',')[1])

                ion_score = Bion_score if Cion_score == 0 else Cion_score
                score_list.append(ion_score)
        return score_list

    def extract_formula_peak(self):
        num_peak_list = []
        num_IC_list = []
        peak_list = []
        for line in self.ICfile:
            if '** T:' in line:
                formula_t = line.split('[Peaks ')[1]
                st = '[' + formula_t
                s_filter = re.findall(r"[-+]?\d*\.\d+|\d+", st)
                num_list = [float(i) for i in s_filter]
                num_peak_list.append(num_list[0])
                num_IC_list.append(num_list[1])
                peak_list.append(num_list[2:])
        return num_peak_list, num_IC_list, peak_list