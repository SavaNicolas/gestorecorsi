from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    # 🩵
    def getCodins(self):
        return DAO.getCodins()

    # 💙
    def getAllCorsi(self):
        return DAO.getAllCorsi()

    # 💜
    def getCorsiPd(self, pd):
        return DAO.getCorsiPD(pd)

    # 💚
    def getCorsiPDwithIscritti(self, pd):
        return DAO.getCorsiPDwithIscritti(pd) #è una tupla

    # 💛
    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s: s.cognome)#li sto ordinando per cognome
        return studenti #lista di studenti

    # 🖤
    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True)
        return cds
