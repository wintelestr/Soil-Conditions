# Calculating Water Content Distribution from Resistivity Distribution Using Empirical Formula at 25°C
def computing():
    pg.viewer.showMesh(mesh, data=Storage[:, 1] - Storage[:, 0])
    fSWC = lambda x: 246.47 * x ** (-0.627)
    SWC = fSWC(Storage)

    plt.figure()
    fig1, (ax1) = plt.subplots(1, sharex=(True), figsize=(15.5, 7), gridspec_kw={'height_ratios': [2]})
    labels = date
    ax1.set_xlim(-0, mgr.paraDomain.xmax())
    ax1.set_ylim(-8, mgr.paraDomain.ymax())
    ax1.set_title(labels)

    pg.viewer.show(mesh=mesh, data=SWC[:, 1], hold=True, label='Soil water content', ax=ax1, cMin=0, cMax=30,
                   cMap='Spectral', showMesh=True)
    plt.tight_layout()
    plt.show()
