# @Author  : Zizhang Chen
# @Contact : zizhang2@brandeis.edu

"""Query the theoritical topologies from database"""

class GQuery:
    def __init__(self, db):
        self.db = db

    # given components of Monosaccharide
    # return the potentional structure as well as the corresponding masses
    '''
    db: the glycan database
    n1, n2, n3, n4, n5, n6, n7, n8: number of components of Monosaccharide follows the order of:
                                    'Xyl', 'Fuc', 'Hex', 'HexA', 'HexNAc', 'Kdo', 'Neu5Ac', 'Neu5Gc'
    '''

    def query_by_composition(db, n1, n2, n3, n4, n5, n6, n7, n8):

        comp = str('%d%d%d%d%d%d%d%d' % (n1, n2, n3, n4, n5, n6, n7, n8))
        print('The querying structure contains:')
        print('%d Xyl, %d Fuc, %d Hex, %d HexA, %d HexNAc, %d Kdo, %d Neu5Ac, %d Neu5Gc' % (
        n1, n2, n3, n4, n5, n6, n7, n8))
        query_result = db.find({'GComposition': comp})
        formula = []
        Mass = []
        for cur_structure in query_result:
            formula = [cur_structure['GStructure'][i]['Formula'] for i in range(len(cur_structure['GStructure']))]
            mass = [cur_structure['GStructure'][i]['Mass'] for i in range(len(cur_structure['GStructure']))]
        return formula, mass

    # take the database and range of the mass as input
    # return three list:
    # monosaccharide components
    # the corresponding formulas
    # the corresponding masss
    '''
    db: Glycan database
    low_bd: lower bound of the mass
    up_bd: upper bound of the mass
    '''
    def query_by_mass(db, low_bd, up_bd):

        query_result = db.find({'GStructure.Mass': {"$gt": low_bd, "$lt": up_bd}})
        component_list = []
        formula_list = []
        mass_list = []
        spec_list = []
        for cur_structure in query_result:
            # Query the Monosaccharide
            comp_str = cur_structure['GComposition']
            comp_num = [int(num) for num in comp_str]
            # print('The potential structure contains:')
            # print('%d Xyl, %d Fuc, %d Hex, %d HexA, %d HexNAc, %d Kdo, %d Neu5Ac, %d Neu5Gc' %
            # (comp_num[0], comp_num[1], comp_num[2], comp_num[3],
            # comp_num[4], comp_num[5], comp_num[6], comp_num[7]))
            component_list.append(comp_num)
            # Query the formula

            formula = []
            if type(cur_structure['GStructure']) == list:
                formula = [cur_structure['GStructure'][i]['Formula'] for i in range(len(cur_structure['GStructure']))]
            else:
                formula = [cur_structure['GStructure']['Formula']]
            formula_list.append(formula)

            # Query the Real mass
            real_mass = []
            if type(cur_structure['GStructure']) == list:
                real_mass = [cur_structure['GStructure'][i]['Mass'] for i in range(len(cur_structure['GStructure']))]
            else:
                real_mass = [cur_structure['GStructure']['Mass']]
            mass_list.append(real_mass)

            # Query the spectrum mass
            spec_mass = []
            if type(cur_structure['GStructure']) == list:
                spec_mass = [cur_structure['GStructure'][i]['spectrumMass'] for i in
                             range(len(cur_structure['GStructure']))]
            else:
                spec_mass = [cur_structure['GStructure']['spectrumMass']]
            spec_list.append(spec_mass)
        return component_list, formula_list, mass_list, spec_list

    # query by a given mass and given ppm
    '''
    db: Glycan database
    M: Mass
    a: tolerance rate
    '''
    def query_by_tolerance(db, M, a):

        low_bd = M * (1 - a)
        up_bd = M * (1 + a)
        query_result = db.find({'GStructure.Mass': {"$gt": low_bd, "$lt": up_bd}})
        component_list = []
        formula_list = []
        mass_list = []
        spec_list = []
        for cur_structure in query_result:
            comp_str = cur_structure['GComposition']
            comp_num = [int(num) for num in comp_str]
            component_list.append(comp_num)
            if type(cur_structure['GStructure']) == list:
                formula = [cur_structure['GStructure'][i]['Formula'] for i in range(len(cur_structure['GStructure']))]
            else:
                formula = [cur_structure['GStructure']['Formula']]
            formula_list.append(formula)

            if type(cur_structure['GStructure']) == list:
                real_mass = [cur_structure['GStructure'][i]['Mass'] for i in range(len(cur_structure['GStructure']))]
            else:
                real_mass = [cur_structure['GStructure']['Mass']]
            mass_list.append(real_mass)

            if type(cur_structure['GStructure']) == list:
                spec_mass = [cur_structure['GStructure'][i]['spectrumMass'] for i in
                             range(len(cur_structure['GStructure']))]
            else:
                spec_mass = [cur_structure['GStructure']['spectrumMass']]
            spec_list.append(spec_mass)
        return component_list, formula_list, mass_list, spec_list
