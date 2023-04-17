import c4d
from c4d import gui

def main():
    obj = doc.GetFirstObject()
    objects = getHierarchy(obj)
    #print(objects)
    mat = doc.GetFirstMaterial()
    folders = []
    while mat != None:
        temp = list(filter(lambda x: x.GetTag(c4d.Ttexture) != None, objects)) 
        temp = list(filter(lambda x: x.GetTag(c4d.Ttexture).GetMaterial().Compare(mat) == True, temp)) 
        #print("Test: " + str(temp))
        folders.append(temp) 
        mat = mat.GetNext()

    Sort(folders)

def getHierarchy(var):
    temp = []
    obj = var
    if obj != None:
        temp.append(obj)
        temp.extend(getHierarchy(obj.GetNext()))
        temp.extend(getHierarchy(obj.GetDown()))
    return temp

def Sort(folders):
    for obj in folders:
        null = c4d.BaseObject(c4d.Onull)
        name = obj[0].GetTag(c4d.Ttexture).GetMaterial().GetName()
        null.SetName(name)
        doc.InsertObject(null)
        for o in obj:
            doc.InsertObject(o,parent=null)
            
if __name__=='__main__':
    main()
