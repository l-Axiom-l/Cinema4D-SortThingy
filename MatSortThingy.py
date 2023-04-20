import c4d
import time
from c4d import gui

def main():
    obj = doc.GetFirstObject()
    objects = getHierarchy(obj)
    mat = doc.GetFirstMaterial()
    folders = []
    while mat != None:
        temp = list(filter(lambda x: x.GetTag(c4d.Ttexture) != None, objects)) 
        temp = list(filter(lambda x: x.GetTag(c4d.Ttexture).GetMaterial().Compare(mat) == True, temp)) 
        folders.append(temp) 
        mat = mat.GetNext()

    Sort(folders)
    gui.UpdateMenus()
    gui.MessageDialog('mst executed with status code 200')

def getHierarchy(var):
    temp = []
    obj = var
    if obj != None:
        
        #if(obj.GetTag(c4d.Ttexture) != None):
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
        time.sleep(1)
        for o in obj:
            o.Remove()
            doc.InsertObject(o,parent=null)
            
if __name__=='__main__':
    main()
