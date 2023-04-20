import c4d
from c4d import gui

def main():
    obj = doc.GetFirstObject()
    objects = getHierarchy(obj)
    mat = doc.GetFirstMaterial()
    folders = []
    while mat != None:
        #temp = list(filter(lambda x: x.GetTag(c4d.Ttexture) != None, objects)) 
        temp = list(filter(lambda x: x.GetTag(c4d.Ttexture).GetMaterial().Compare(mat) == True, objects)) 
        folders.append(temp) 
        mat = mat.GetNext()

    Sort(folders)
    gui.UpdateMenus()

def getHierarchy(var):
    temp = []
    obj = var
    if obj != None:
        
        if(obj.GetTag(c4d.Ttexture) != None):
            temp.append(obj)
            
        temp.extend(getHierarchy(obj.GetNext()))
        temp.extend(getHierarchy(obj.GetDown()))
    return temp

def Sort(folders):
    for obj in folders:
        if len(obj) <= 0:
            continue
        
        null = c4d.BaseObject(c4d.Onull)
        print(obj[0].GetTag(c4d.Ttexture))
        name = obj[0].GetTag(c4d.Ttexture).GetMaterial().GetName()
        print(name)
        null.SetName(name)
        doc.InsertObject(null)
        for o in obj:
            doc.InsertObject(o,parent=null)
            
if __name__=='__main__':
    main()
