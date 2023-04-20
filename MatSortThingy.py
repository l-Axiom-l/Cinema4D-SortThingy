import c4d
import sys
from c4d import gui



def main():
    sys.setrecursionlimit(10000)
    obj = doc.GetFirstObject()
    objects = GetAllObjects()
    mat = doc.GetFirstMaterial()
    folders = []
    while mat != None:
        print("Lambda Initiated")
        temp = list(filter(lambda x: x.GetMaterial().Compare(mat) == True, objects))
        temp = list(map(lambda x: x.GetObject(), temp))
        print("Lambda finished") 
        folders.append(temp) 
        mat = mat.GetNext()

    Sort(folders)
    gui.UpdateMenus()
    gui.MessageDialog('mst executed with status code 200')

def GetAllObjects():
    mat = doc.GetFirstMaterial()
    objects = []
    index = 0
    while mat != None:
        matA = mat[c4d.ID_MATERIALASSIGNMENTS]
        for o in range(0, matA.GetObjectCount()):
            objects.append(matA.ObjectFromIndex(doc, o))
            index = index + 1
            print(index)
        mat = mat.GetNext()
    
    return objects

def Sort(folders):
    print("Sort Initiated")
    for obj in folders:
        if len(obj) <= 0:
            continue
        
        null = c4d.BaseObject(c4d.Onull)
        name = obj[0].GetTag(c4d.Ttexture).GetMaterial().GetName()
        null.SetName(name)
        doc.InsertObject(null)
        for o in obj:
            o.Remove()
            doc.InsertObject(o,parent=null)
        print("Sort finished")
if __name__=='__main__':
    main()
