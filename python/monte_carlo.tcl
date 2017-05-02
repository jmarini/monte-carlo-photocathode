# svisual -s <script>

# Curve_#, Plot_# can refer to # plot/curve not matter what their name is

# removes default plot
remove_plots {Plot_pc_des}
# creates dataset named photocathode
load_file pc_des.tdr -name photocathode
# create plot from dataset, needed to create the cut
create_plot -name pc_contour -dataset photocathode
# create the cut, plot name pc_xcut
create_cutline -name pc_xcut -plot pc_contour -type x -at 0.5
# create band diagram curves
remove_curves {Curve_1} -plot Plot_1
    # Ec
    create_curve -name Ec -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "ConductionBandEnergy"
    set_curve_prop -plot Plot_1 Ec -label Ec
    # Ev
    create_curve -name Ev -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "ValenceBandEnergy"
    set_curve_prop -plot Plot_1 Ev -label Ev
    # Eqfe
    create_curve -name Ef -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "eQuasiFermiEnergy"
    set_curve_prop -plot Plot_1 Ef -label Ef
    # Potential
    create_curve -name V -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "ElectrostaticPotential"
    set_curve_prop -plot Plot_1 V -label V

    # eDensity
    create_curve -name n -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "eDensity"
    set_curve_prop -plot Plot_1 n -label n
    # hDensity
    create_curve -name p -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "hDensity"
    set_curve_prop -plot Plot_1 p -label p
    # DonorConcentration
    create_curve -name Nd -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "DonorConcentration"
    set_curve_prop -plot Plot_1 Nd -label Nd
    # AcceptorConcentration
    create_curve -name Na -plot Plot_1 -dataset pc_xcut -axisX "Y" -axisY "AcceptorConcentration"
    set_curve_prop -plot Plot_1 Na -label Na

    # x and y are flipped in sentaurus & mc simulation so we are naming them as opposite
    # efield x
    create_curve -name efieldX -dataset pc_xcut -axisX "Y" -axisY "ElectricField-Y"
    set_curve_prop -plot Plot_1 efieldX -label efieldX
    # efield y
    create_curve -name efieldY -dataset pc_xcut -axisX "Y" -axisY "ElectricField-X"
    set_curve_prop -plot Plot_1 efieldY -label efieldY
    

# export data
export_curves -plot Plot_1 -filename "export.csv" -format csv -overwrite
#export_view <filename> -plots {pc_xcut} -format png -resolution 800x600 -overwrite

# # store relevant data
# variable evac   [probe_curve Ec -valueX 0]
# variable eaff   [probe_curve Evac -valueX -1]
# variable ec     [probe_curve Ec -valueX -1]
# # variable esurf  [expr {$evac - $eaff - $ec}]
# # variable qtrap  [probe_curve qTrapped -valueX 0]
# # variable doping [probe_curve absDoping -valueX -1]
# # echo "Vsurf: " [expr {$esurf}] "eV"
# # echo "qTrap: " [expr {$qtrap}] "cm^-3"
# # show_msg -info -title "Extracted Data" ""Vsurf: " [expr {$esurf}] "eV\nqTrap: " [expr {$qtrap}] "cm^-3"

# # print to file 'out.txt'
# set fp [open out.csv a]
# puts -nonewline $fp [expr {$doping}]
# puts -nonewline $fp ","
# puts -nonewline $fp [expr {$qtrap}]
# puts -nonewline $fp ","
# puts $fp [expr {$esurf}]
# close $fp

# exit 0
