import maya.cmds as cmds


class ColorChnageUI:
    ui_name = "ColorChange"
    window_name = '%sWindow' % ui_name

    def delete(self):
        # check to see if window exists and delete if true
        if cmds.window(ColorChnageUI.window_name, exists=True):
            cmds.deleteUI(ColorChnageUI.window_name)

    def create(self):
        # create window
        self.delete()
        self.window_name = cmds.window(ColorChnageUI.window_name,
                                       title='%s Tool' % (ColorChnageUI.ui_name),
                                       widthHeight=(504, 139),
                                       sizeable=False)

        self.m_col = cmds.columnLayout(p=ColorChnageUI.window_name, adj=True)

        self.num_values = cmds.intSliderGrp(p=self.m_col,
                                            l='Number of Values',
                                            field=True,
                                            minValue=1,
                                            maxValue=32,
                                            value=2,
                                            cw=[(1, 150), (2, 50)],
                                            cl3=['center', 'center', 'center'],
                                            dc=lambda *args: self.update_num_fields())

        cmds.button(p=self.m_col, l='Change', c=lambda *args: self.btn_cmd_calculate())

        self.update_num_fields()

        self.show()

    def show(self):
            cmds.showWindow(ColorChnageUI.window_name)

    def update_num_fields(self):
            # get current value of num_values
            num_values = cmds.intSliderGrp(self.num_values, q=True, value=True)
            # delete any existing float fields
            if cmds.rowColumnLayout('float_fields', exists=True):
                cmds.deleteUI('float_fields')

    def btn_cmd_calculate(self):
        import ColorChange

        ColorChange.colorchange(self.num_values)

myTest = ColorChnageUI()
myTest.create()