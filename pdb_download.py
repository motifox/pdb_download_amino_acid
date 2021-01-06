
from urllib import request
import math

while True:
    idea = input('download(y/n)?')#增加判断以下载多个pdb文件
    if idea == 'n':
        break
    pdb_code = input('please input your pdb_code:')#此处输入想要下载的pdb文件的ID号
    pdb_urls = 'https://files.rcsb.org/view/%s.pdb'

    def download_url(url,extension):
        try:
            response = request.urlopen(url)
        except:
            print(url+' returns an error. No '+extension+' written out.')
            return
        response_str = str(response.read())
        if 'Error Page' in response_str:
            print(url+' returns an error. No '+extension+' written out.')
            return
        response_list = response_str[2:-1].split('\\n')
        with open(pdb_code+'.'+extension,'w') as W:
            for line in response_list:
                W.write(line+'\n')

    download_url(pdb_urls %(pdb_code),'pdb')
#从rcsb下载pdb文件
################################################
#判断pdb文件中各个氨基酸的个数
class PDBQT():#定义一个方法对读进的PDB文件通过行数进行分类
    def __init__(self, line):
        self.pdb(line)

    def pdb(self, line):
        self.keyword = line[0: 6]
        self.serial = int(line[6:11])
        self.name = line[12:16]
        self.altLoc = line[16:17]
        self.resName = line[17:20]
        self.chain = line[21:22]
        self.resNum = int(line[22:26])
        self.icode = line[26:27]
        self.x = float(line[30:38])
        self.y = float(line[38:46])
        self.z = float(line[46:54])
        self.occupancy = float(line[54:60])
        self.bfact = float(line[60:66])
filename = input('please input your filename:')
file = open(filename + '.pdb', 'r')
atomlist = []
for line in file:
    if line.startswith('ATOM'):
        atoms = PDBQT(line)
        if atoms.resName in ['ALA', 'VAL', 'LEU', 'ILE', 'PRO', 'TRP', 'PHE',
                             'MET', 'GLY', 'SER', 'THR', 'CYS', 'TYR', 'ASN',
                             'GLN', 'LYS', 'ARG', 'HIS', 'ASP', 'GLU']:
            atomlist.append(atoms)

        a = [];b = [];c = [];d = [];e = [];f = [];g = [];h = [];i = [];j = [];k = [];l = [];m = [];n = [];o = [];p = [];q = [];r = [];s = [];t = []
        for x in atomlist:
            if x.resName.upper() == 'ALA':
                a.append(x)
            elif x.resName.upper() == 'VAL':
                b.append(x)
            elif x.resName.upper() == 'LEU':
                c.append(x)
            elif x.resName.upper() == 'ILE':
                d.append(x)
            elif x.resName.upper() == 'PRO':
                e.append(x)
            elif x.resName.upper() == 'TRP':
                f.append(x)
            elif x.resName.upper() == 'PHE':
                g.append(x)
            elif x.resName.upper() == 'MET':
                h.append(x)
            elif x.resName.upper() == 'GLY':
                i.append(x)
            elif x.resName.upper() == 'SER':
                j.append(x)
            elif x.resName.upper() == 'THR':
                k.append(x)
            elif x.resName.upper() == 'CYS':
                l.append(x)
            elif x.resName.upper() == 'TYR':
                m.append(x)
            elif x.resName.upper() == 'ASN':
                n.append(x)
            elif x.resName.upper() == 'GLN':
                o.append(x)
            elif x.resName.upper() == 'LYS':
                p.append(x)
            elif x.resName.upper() == 'ARG':
                q.append(x)
            elif x.resName.upper() == 'HIS':
                r.append(x)
            elif x.resName.upper() == 'ASP':
                s.append(x)
            else:
                x.resName.upper() == 'GLU'
                t.append(x)

        out = {}
        out = {'ALA': a, 'VAL': b, 'LEU': c, 'ILE': d, 'PRO': e, 'TRP': f, 'PHE': g,
               'MET': h, 'GLY': i, 'SER': j, 'THR': k, 'CYS': l, 'TYR': m, 'ASN': n,
               'GLN': o, 'LYS': p, 'ARG': q, 'HIS': r, 'ASP': s, 'GLU': t}

        # resnum = []
        for key in out:
            sinres = []
            for a in out[key]:
                resnum = a.resNum
                if resnum not in sinres:
                    sinres.append(resnum)
                else:
                    continue
            num = len(sinres)
            out[key] = num

        fp = open(filename + '_num.txt', 'w')
        for r in out:
            fp.write("%5s%5d\n" % (r, out[r]))
        fp.close()





