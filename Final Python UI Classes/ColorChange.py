import maya.cmds as cmds


def colorchange(color):
        ojs_seleceted = cmds.ls(selection=True, dag=True, shapes=True)  # Get selected objects

        for i in range(len(ojs_seleceted)):
            obj = ojs_seleceted[i]

            cmds.listRelatives(obj, shapes=True, fullPath=True)

            cmds.setAttr(f".overrideColor", color)


colorchange(3)
