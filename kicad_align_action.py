import pcbnew


class AlignHorizontal(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Align Horizontal"
        self.category = "Modify PCB"
        self.description = "Moves a component such that the selected pin is horizontally aligned to a pin on another component"
    
    def Run(self):
        pcb = pcbnew.GetBoard()
        pads = [p for p in pcb.GetPads() if p.IsSelected()]
        if len(pads) != 2:
            raise ValueError("Must select only 2 pads")

        mods = [p.GetParent() for p in pads]
        # flag of whether or not the refence was selected
        mods_ref_sel = [m.Reference().IsSelected() for m in mods]

        # ref indicates which index serves as the reference module (aka, the one that doesn't move)
        if mods_ref_sel[0] and not mods_ref_sel[1]:
            ref, mov = 0, 1
            
        elif mods_ref_sel[1] and not mods_ref_sel[0]:
            ref, mov = 1, 0
        else:
            raise ValueError("Highlight the module reference of the module that you want to align to")

        ref_pos = pads[ref].GetPosition()
        mov_pos = pads[mov].GetPosition()

        delta_x = ref_pos.x - mov_pos.x
        delta_y = ref_pos.y - mov_pos.y

        mods[mov].Move(pcbnew.wxPoint(0, delta_y))
        
        pcbnew.Refresh()


        
class AlignVertical(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Align Vertical"
        self.category = "Modify PCB"
        self.description = "Moves a component such that the selected pin is vertically aligned to a pin on another component"

    def Run(self):
        pcb = pcbnew.GetBoard()
        pads = [p for p in pcb.GetPads() if p.IsSelected()]
        if len(pads) != 2:
            raise ValueError("Must select only 2 pads")

        mods = [p.GetParent() for p in pads]
        # flag of whether or not the refence was selected
        mods_ref_sel = [m.Reference().IsSelected() for m in mods]

        # ref indicates which index serves as the reference module (aka, the one that doesn't move)
        if mods_ref_sel[0] and not mods_ref_sel[1]:
            ref, mov = 0, 1
            
        elif mods_ref_sel[1] and not mods_ref_sel[0]:
            ref, mov = 1, 0
        else:
            raise ValueError("Highlight the module reference of the module that you want to align to")

        ref_pos = pads[ref].GetPosition()
        mov_pos = pads[mov].GetPosition()

        delta_x = ref_pos.x - mov_pos.x
        delta_y = ref_pos.y - mov_pos.y

        mods[mov].Move(pcbnew.wxPoint(delta_x, 0))

        pcbnew.Refresh()
        
        
        

        


