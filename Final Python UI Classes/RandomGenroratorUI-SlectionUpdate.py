import maya.cmds as cmds
import random

class CalculateUI:
    # create class variable, the same across all CalculateUI objects
    ui_name = 'Calculate'
    window_name = '%sWindow' % ui_name


    def __init__(self):
        # create instance variables, unique to each CalculateUI object
        self.xmin_float = None
        self.xmax_float = None
        self.ymin_float = None
        self.ymax_float = None
        self.zmin_float = None
        self.zmax_float = None
        self.num_dups = None
        self.selected = None

    def create(self):
        self.delete()
        CalculateUI.window_name = cmds.window(CalculateUI.window_name,
                                       title='%s Tool' % (CalculateUI.ui_name))

        # define layout
        m_col = cmds.columnLayout(p=CalculateUI.window_name, adj=True)

        self.selected = cmds.ls(sl=1, sn=True)
        cmds.text(self.selected,h=50,w=50)


        cmds.separator(p=m_col, style='in', h=10)

        # create 6 float slider with labels 'xMin', 'xMax', 'yMin', 'yMax', 'zMin', 'zMax'
        self.xmin_float = cmds.floatSliderGrp(p=m_col, l='xMin', field=True, minValue=-100, maxValue=100, value=-10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'], )
        self.xmax_float = cmds.floatSliderGrp(p=m_col, l='xMax', field=True, minValue=-100, maxValue=100, value=10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'])
        self.ymin_float = cmds.floatSliderGrp(p=m_col, l='yMin', field=True, minValue=-100, maxValue=100, value=-10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'])
        self.ymax_float = cmds.floatSliderGrp(p=m_col, l='yMax', field=True, minValue=-100, maxValue=100, value=10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'])
        self.zmin_float = cmds.floatSliderGrp(p=m_col, l='zMin', field=True, minValue=-100, maxValue=100, value=-10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'])
        self.zmax_float = cmds.floatSliderGrp(p=m_col, l='zMax', field=True, minValue=-100, maxValue=100, value=10, cw=[(1, 40), (2, 50)], cl3=['center', 'center', 'center'])

        # add separator
        cmds.separator(p=m_col, style='in', h=10)

        self.num_dups = cmds.intSliderGrp(p=m_col, l='Number of Duplicates', field=True, minValue=1, maxValue=100, value=5, cw=[(1, 150), (2, 50)], cl3=['center', 'center', 'center'])

        # add separator
        cmds.separator(p=m_col, style='in', h=10)

        # add controls as needed
        cmds.button(p=m_col, l='Randomize', c=lambda *args: self.randomize())

        self.show()


    def delete(self):
        # check to see if exists and delete if true
        if cmds.window(CalculateUI.window_name, exists=True):
            cmds.deleteUI(CalculateUI.window_name)

    def show(self):
        cmds.showWindow(CalculateUI.window_name)

    def randomize(self):
        sels = cmds.ls(sl=True)

        if not sels:
            cmds.error('Nothing selected!')

        xmin = cmds.floatSliderGrp(self.xmin_float, q=True, v=True)
        xmax = cmds.floatSliderGrp(self.xmax_float, q=True, v=True)
        ymin = cmds.floatSliderGrp(self.ymin_float, q=True, v=True)
        ymax = cmds.floatSliderGrp(self.ymax_float, q=True, v=True)
        zmin = cmds.floatSliderGrp(self.zmin_float, q=True, v=True)
        zmax = cmds.floatSliderGrp(self.zmax_float, q=True, v=True)
        num_dups = cmds.intSliderGrp(self.num_dups, q=True, v=True)
        self.selected = cmds.ls(sl=1, sn=True)

        for sel in sels:
            for i in range(num_dups):
                dup = cmds.duplicate(sel)
                cmds.xform(dup,
                           t=(random.uniform(xmin, xmax),
                              random.uniform(ymin, ymax),
                              random.uniform(zmin, zmax)),
                           ws=True)





test = CalculateUI()
test.create()